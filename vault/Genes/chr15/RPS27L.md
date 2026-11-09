---
symbol: "RPS27L"
type: "gene"
col: 11622
ensembl_id: "ENSG00000185088"
name: "ribosomal protein S27 like"
location: "15q22.2"
module: 62
arm: "+"
pooled_cpm: 63.76
n_lines_expressing: 50
n_dd_up: 6
n_dd_down: 1
n_dd_up_clean: 1
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 9
direction_downstream: 2
tags: ["gene", "module/062", "written"]
generated_by: "tahoemap"
---

# RPS27L

*ribosomal protein S27 like* — 15q22.2

> [!summary] In one line
> RPS27L encodes a p53-induced paralogue of ribosomal protein S27 that differs from it by only three amino acids, incorporates into the 40S subunit, and binds MDM2 — placing it at the junction between p53 and the ribosome.

## What it is

RPS27L is an 84-residue small-subunit ribosomal protein at 15q22.2, very nearly a duplicate of RPS27: in human and mouse the proteins differ at just three positions. The gene's name records the resemblance, which is both why it is interesting and why it is awkward to measure.

What distinguishes RPS27L from an ordinary ribosomal protein gene is its regulation. It is a direct p53 target, with a response element demonstrated in the first intron. Which way it tips cell fate was reported in both directions in the same year: the group that identified it as a p53 target found RPS27L *promotes* etoposide-induced apoptosis, so silencing it reduces apoptosis; an independent group found that depleting it defeats the damage checkpoints and converts the p53 response from arrest to apoptosis. It also engages the p53 machinery as protein. RPS27L binds the central acidic domain of MDM2, competes with p53 for that interaction, and is itself ubiquitylated by MDM2 — target, substrate and regulator of the same axis.

The mouse genetics complicate the picture. Germline inactivation of *Rps27l* stabilises Mdm2, which degrades Mdm4 and unbalances the Mdm2–Mdm4 ligase, activating p53 strongly enough to deplete haematopoietic stem cells and kill the animals after birth. On a *Trp53*-heterozygous background the same loss instead produces lymphoma with loss of the remaining p53 allele and marked aneuploidy. Separately, work on paralogue retention found that Rps27- and Rps27l-containing ribosomes associate preferentially with different transcripts, and that the two loss-of-function alleles are lethal at different developmental stages — evidence for subfunctionalised expression rather than interchangeable proteins.

## What is uncertain

The direction of RPS27L's effect on p53 is genuinely contested. The cell-based work has it sequestering MDM2 and so stabilising p53 — an activator; the mouse knockout has p53 going *up* when RPS27L is removed — a restraint. Both come from the same laboratory and are not obviously reconcilable by one mechanism; the resolution probably involves Mdm2/Mdm4 stoichiometry and differs between acute perturbation and germline loss, but that is interpretation, not an established answer. Whether RPS27L has a function distinct from RPS27, as opposed to a different expression pattern, remains open; the paralogue-retention work favours divergent expression over divergent protein chemistry. Given a three-residue difference from a far more abundant paralogue, read assignment between RPS27L and RPS27 rests on a handful of distinguishing positions, so modest apparent changes here deserve more caution than in a gene with no close relative. Ribosomal protein transcripts are also dominated by growth- and translation-coupled regulation, so a p53 signal read off this gene competes with a much larger source of variation.

## References

- He & Sun, 2007, Oncogene — RPS27L is a direct p53 target, with a p53-binding site in its first intron; overexpression promoted and silencing inhibited etoposide-induced apoptosis.
- Li et al., 2007, Cancer Research — RPS27L as a p53-inducible modulator of cell fate: its depletion causes checkpoint deficiency and converts the damage response from arrest to apoptosis, the opposite direction to He & Sun.
- Xiong et al., 2011, Oncogene — RPS27L and RPS27 interplay with the p53–MDM2 axis as a target, a substrate and a regulator; maps binding to MDM2's central acidic domain.
- Xiong et al., 2014, eLife — germline *Rps27l* loss activates p53 via Mdm2 stabilisation and Mdm4 degradation, and promotes lymphoma with aneuploidy on a *Trp53*-heterozygous background.
- Xu et al., 2023, eLife — subfunctionalised expression, not protein divergence, accounts for retention of Rps27 and Rps27l in vertebrates.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.39× (z +6.8, q 8e-09, up in 41 of 49 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.47× (z +4.2, q 0.003, up in 32 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.85×, MIA PaCa-2 3.47×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.18×, C32 2.79×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 5.43×; ⚠ toxic).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[c-Kit-IN-1 (drug)]] 0.05 µM: 0.518× (z -5.1, q 2e-04, down in 41 of 48 measured lines) ⚠ unreliable plate only.
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ANKRA2]] (+0.78, fdr 7e-06), [[PHLDA3]] (+0.73, fdr 7e-06), [[TP53INP1]] (+0.72, fdr 7e-06); moves opposite to [[PRKDC]] (-0.64, fdr 1e-05), [[NUP188]] (-0.62, fdr 3e-05), [[CS]] (-0.60, fdr 2e-05).
> It is in [[Module 062]], a single-armed module (p53 targets up).
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[PINCR]] → it (grade B ⚠); 2 go from it, the strongest it → [[MDM2]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 5 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11622.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 3 with an alert ⚠; the 3 shown; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 2 lines (LoVo 3.85×, MIA PaCa-2 3.47×; ⚠ cell-cycle shift, explains ~0% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 2 lines (RKO 3.18×, C32 2.79×); [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (RKO 5.43×; ⚠ toxic).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +6.8 | 8e-09 | 41/49 (PANC-1, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.22×** | +6.0 | 7e-07 | 46/47 (RKO, LS 180, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.19×** | +5.8 | 9e-07 | 29/38 (HS-578T, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.47×** | +4.2 | 0.003 | 32/48 (LoVo, SNU-1, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +3.9 | 0.011 | 29/44 (HS-578T, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~43% of this change | **1.57×** | +3.5 | 0.048 | 34/46 (KATO III, HT-29, …) | inconsistent across doses | low cells (technical?) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | 1.32× | +3.1 | 0.17 | 24/49 (RKO, C32, …) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 1 with an alert ⚠. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11622.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.518×** | -5.1 | 2e-04 | 41/48 (SW 1088, A549, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM |  | 0.662× | -3.2 | 0.38 | 24/48 (SW480, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Baicalin (drug)]] 5 µM |  | 0.756× | -3.1 | 0.38 | 33/49 (C32, LOX-IMVI, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11622. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 70.0 | 2 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.18× (z +9.5) | — |
| [[C32 (line)]] | wt | 101 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.79× (z +8.8) | — |
| [[LoVo (line)]] | wt | 167 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.85× (z +13.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 21.8 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.47× (z +9.0) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[PANC-1 (line)]] | alt | 32.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.17× (z +9.0) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 103 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 54.3 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 136 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 193 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 23.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 50.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 37.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 99.8 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.3 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 83.1 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 37.3 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 30.0 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 132 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 57.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 83.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 118 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 52.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 87.4 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 53.9 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 73.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 70.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 42.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 60.6 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 43.5 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 65.3 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 47.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 40.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 59.4 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 40.6 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 87.0 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 33.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11622), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*75 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ANKRA2]] | +0.78 | +0.78 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PHLDA3]] | +0.73 | +0.62 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[TP53INP1]] | +0.72 | +0.64 / +0.73 | both halves | 7e-06 |  |
| [[DNAI3]] | +0.71 | +0.67 / +0.70 | both halves | 7e-06 |  |
| [[XPC]] | +0.70 | +0.70 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[PPM1D]] | +0.70 | +0.63 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY |
| [[FDXR]] | +0.69 | +0.65 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 440 |
| [[DCP1B]] | +0.68 | +0.68 / +0.69 | both halves | 7e-06 |  |
| [[ISCU]] | +0.68 | +0.55 / +0.74 | both halves | 1e-05 | pathway: HALLMARK_P53_PATHWAY |
| [[DDB2]] | +0.68 | +0.63 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_P53_PATHWAY; STRING 471 |
| [[SPATA18]] | +0.66 | +0.63 / +0.66 | both halves | 7e-06 |  |
| [[RRM2B]] | +0.66 | +0.69 / +0.62 | both halves | 7e-06 |  |

## Genes that move opposite

*25 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRKDC]] | -0.64 | -0.55 / -0.65 | both halves | 1e-05 |  |
| [[NUP188]] | -0.62 | -0.45 / -0.68 | both halves | 3e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[CS]] | -0.60 | -0.48 / -0.63 | both halves | 2e-05 | pathway: Protein localization |
| [[TUBB]] | -0.59 | -0.57 / -0.57 | both halves | 1e-05 |  |
| [[RRM2]] | -0.57 | -0.55 / -0.52 | both halves | 1e-05 |  |
| [[TUBA1B]] | -0.56 | -0.58 / -0.55 | both halves | 1e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[MTHFD1]] | -0.56 | -0.50 / -0.58 | both halves | 1e-05 |  |
| [[SLC19A1]] | -0.56 | -0.58 / -0.49 | both halves | 1e-05 |  |
| [[EFTUD2]] | -0.56 | -0.59 / -0.54 | both halves | 1e-05 | STRING 558 |
| [[SLC25A10]] | -0.56 | -0.44 / -0.57 | both halves | 3e-05 | pathway: Metabolism of amino acids and derivatives |
| [[SAE1]] | -0.56 | -0.37 / -0.61 | both halves | 8e-05 |  |
| [[PAICS]] | -0.55 | -0.48 / -0.62 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PINCR]] | B | PINCR activity raises RPS27L's level | lines that do not express PINCR (29) vs lines expressing it (21) | 1.88× lower at baseline in the lines without PINCR | 0.011 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1 |
| [[EDA2R]] | B | EDA2R activity raises RPS27L's level | lines that do not express EDA2R (28) vs lines expressing it (22) | 1.58× lower at baseline in the lines without EDA2R | 0.025 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000253503, SLC6A15, WNK3 |
| [[PTCHD4]] | B | PTCHD4 activity strengthens RPS27L's drug response | lines that do not express PTCHD4 (33) vs lines expressing it (16) | the lines without PTCHD4 respond 1.08× as strongly (z diff +0.06); strongest at Idarubicin (hydrochloride) 5 µM: 1.17x vs 1.54x (z diff +3.2) | 0.026 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1; target measured in part of the lines; both ways; artifact flags |
| [[ACTA2]] | B | ACTA2 activity raises RPS27L's level | lines that do not express ACTA2 (11) vs lines expressing it (39) | 1.62× lower at baseline in the lines without ACTA2 | 0.052 | ⚠ within organs, on part of the lines; also absent: FAS; maybe low, not absent |
| [[PINCR]] | B | PINCR activity strengthens RPS27L's drug response | lines that do not express PINCR (29) vs lines expressing it (20) | the lines without PINCR respond 0.97× as strongly (z diff +0.13); strongest at Selinexor 5 µM: 1.31x vs 1.81x (z diff +2.6) | 0.068 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PTCHD4, ENSG00000269729, PCK1; target measured in part of the lines; both ways; artifact flags |
| [[PTCHD4]] | B | PTCHD4 activity raises RPS27L's level | lines that do not express PTCHD4 (33) vs lines expressing it (17) | 1.78× lower at baseline in the lines without PTCHD4 | 0.071 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: PINCR, MIR99AHG, NETO1 |
| [[FAS]] | B | FAS activity raises RPS27L's level | lines that do not express FAS (8) vs lines expressing it (42) | 1.62× lower at baseline in the lines without FAS | 0.086 | ⚠ within organs, on part of the lines; also absent: ACTA2, RGS10; maybe low, not absent |
| [[TP53]] | C | TP53 activity strengthens RPS27L's drug response | recorded loss-of-function mutation of TP53 in 32 lines vs 17 not recorded | the TP53-altered lines respond 0.83× as strongly (z diff +0.48); strongest at Idarubicin (hydrochloride) 5 µM: 1.08x vs 1.74x (z diff +3.8) | 0.312 over the table, 0.012 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines; target measured in part of the lines; lower baseline (lost expression?); both ways; artifact flags |
| [[TP53]] | C | TP53 activity raises RPS27L's level | recorded loss-of-function mutation of TP53 in 33 lines vs 17 not recorded | 2.11× lower at baseline in the TP53-altered lines | 0.501 over the table, 0.013 within its group | ⚠ within its group only (a lead); within organs, on part of the lines; TP53 not expressed in 3 of the 33 altered lines |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MDM2]] | C | RPS27L's natural level strengthens MDM2's drug response | RPS27L's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.67, reverse +0.24; direction not clear | 0.033 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |
| [[ANKRA2]] | C | RPS27L's natural level strengthens ANKRA2's drug response | RPS27L's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.65, reverse +0.16; direction not clear | 0.052 | ⚠ tissue can mimic it; precision caveat; rises at some drug-doses, falls at others; direction unclear |

## Where it sits

- **Module**: [[Module 062]] — p53 targets up; 78 genes; every member is in the + arm (projection on the module's main direction 0.775). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.4, 36.0); signed map (41.8, -24.2). **Vector** length 104, 39.0% of its response variance represented; |z| ≥ 3 in 626 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TP53 Regulates Transcription of Cell Death Genes* (reactome, mean cos +0.55 to 6); *apoptosis* (hallmark, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Selinexor (drug)]] 5 µM |  | +6.6 | +4.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.8 | +1.2 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.4 |
|  | [[Amsacrine (drug)]] 5 µM |  | +3.8 | +2.8 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.5 | -0.3 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.7 | +2.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.4 | +2.1 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +1.6 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | +2.2 | +2.5 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -6.8 | -5.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.4 | -0.5 |
|  | [[TAK-733 (drug)]] 5 µM |  | -3.5 | -1.6 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | -3.4 | -1.6 |
|  | [[Abemaciclib (drug)]] 5 µM |  | -3.3 | -1.0 |
|  | [[EX229 (drug)]] 5 µM |  | -3.0 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | ribosomal protein S27 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q22.2 — chr15:63,125,872-63,158,021 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | S ribosomal proteins |
| Hallmark sets | P53_PATHWAY |
| Reactome | 51 pathways, smallest: SARS-CoV-1 modulates host translation machinery; SARS-CoV-2 modulates host translation machinery; Formation of the ternary complex, and subsequently, the 43S complex |
| Matched by | ensembl_id |

UniProt [Q71UM5](https://www.uniprot.org/uniprotkb/Q71UM5) carries no function annotation.

**Summary**, from NCBI Gene [51065](https://www.ncbi.nlm.nih.gov/gene/51065):

> This gene encodes a protein sharing 96% amino acid similarity with ribosomal protein S27, which suggests the encoded protein may be a component of the 40S ribosomal subunit. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:18476](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:18476) · Entrez [51065](https://www.ncbi.nlm.nih.gov/gene/51065) · UniProt [Q71UM5](https://www.uniprot.org/uniprotkb/Q71UM5) · Ensembl [ENSG00000185088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000185088)

## Data

Gene col 11622: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11622); `tables/drug_effects.parquet` (10 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11622, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11622]; `tensor/DDL_lfc|DDL_z.npy` [11622]; `embed/gene_vectors.npy` [11622]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11622 or target_col == 11622). Every well: [[RPS27L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/RPS27L.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
