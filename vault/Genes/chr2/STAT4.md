---
symbol: "STAT4"
type: "gene"
col: 6162
ensembl_id: "ENSG00000138378"
name: "signal transducer and activator of transcription 4"
location: "2q32.2-q32.3"
module: 150
arm: "+"
pooled_cpm: 7.12
n_lines_expressing: 43
n_dd_up: 35
n_dd_down: 9
n_dd_up_clean: 32
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 9
direction_downstream: 4
tags: ["gene", "module/150", "written"]
generated_by: "tahoemap"
---

# STAT4

*signal transducer and activator of transcription 4* — 2q32.2-q32.3

> [!note] Written for the earlier MG53/p53 study
> The written section below was written for an earlier study on the same data (MG53/TRIM72 and p53). Where it mentions a score, a rank, a regulon, an association or "this batch", it refers to that study's analysis (transcription-factor activity inferred from target sets, and MG53 as the exposure), which tahoemap does not compute. This run's own numbers are in the generated sections below.

> [!summary] In one line
> STAT4 is the signal transducer downstream of interleukin-12 that drives T helper 1 differentiation and interferon-gamma production.

## What it is

STAT4 is one of seven mammalian STATs. After IL-12 engages its receptor, JAK2 and TYK2 phosphorylate a single C-terminal tyrosine; STAT4 then dimerises through reciprocal SH2-phosphotyrosine contacts, enters the nucleus and binds GAS elements. Its output is the Th1 programme — IFNG induction in T and NK cells, with TBX21 as lineage partner — and Stat4-null mice lose essentially all IL-12 responses. Expression is largely confined to lymphoid and myeloid cells. STAT4 is also one of the better-replicated autoimmunity loci, with risk variants in rheumatoid arthritis, lupus and Sjogren's syndrome.

## What is uncertain

A factor whose own transcript is near-absent across most of this panel cannot have had meaningful activity, so the score reports the regulon, not STAT4. That regulon is among the smallest scored, and its members are cytokine- and interferon-inducible genes shared with STAT1 and STAT2 — genes that move under many cytotoxic compounds through interferon responses unrelated to IL-12. The score cannot be separated from generic interferon tone.

## References

- Thierfelder et al., 1996, Nature — Stat4-deficient mice fail to mount IL-12-mediated responses in NK and T cells.
- Kaplan et al., 1996, Nature — an independent Stat4 knockout showing impaired IL-12 responses and enhanced Th2 development.
- Remmers et al., 2007, New England Journal of Medicine — a STAT4 haplotype confers risk of rheumatoid arthritis and systemic lupus erythematosus.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 35 drug-doses (3 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.64× (z +25.6, q 0e+00, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 0.615× (z -5.7, q 6e-06, down in 21 of 37 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SAA4]] (+0.55, fdr 1e-05), [[MEF2C-AS1]] (+0.54, fdr 3e-05), [[SHOC1]] (+0.54, fdr 1e-05); moves opposite to [[FN3K]] (-0.41, fdr 4e-04).
> It is in [[Module 150]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 9 arrows point to it, the strongest [[HSD11B1]] → it (grade B ⚠); 4 go from it, the strongest it → [[IL32]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 35 in all, 3 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 35 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6162.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.64×** | +25.6 | 0e+00 | 30/33 (Hs 766T, HOP62, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.79×** | +17.1 | 0e+00 | 32/39 (NCI-H460, SW 900, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.74×** | +11.9 | 2e-30 | 28/37 (NCI-H460, Panc 03.27, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.65×** | +11.1 | 3e-26 | 23/32 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.33×** | +10.0 | 2e-21 | 22/38 (PANC-1, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.21×** | +9.4 | 7e-19 | 26/38 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.16×** | +9.1 | 8e-18 | 23/38 (NCI-H2347, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~1% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +8.2 | 2e-14 | 21/39 (Hs 766T, A498, …) | rises with dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.04×** | +8.1 | 5e-14 | 19/32 (HOP62, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.07×** | +7.8 | 4e-13 | 21/37 (PANC-1, CFPAC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.77×** | +6.7 | 1e-09 | 17/37 (PANC-1, SW 900, …) | top dose only | cell-cycle shift (explains ~13% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.63×** | +5.5 | 1e-06 | 2/15 (SNU-423, A498) | inconsistent across doses | cell-cycle shift (explains ~5% here); composition shift |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.53×** | +5.0 | 3e-05 | 15/37 (A549, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.48×** | +4.5 | 3e-04 | 14/36 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.43×** | +4.2 | 9e-04 | 15/37 (A-172, RPMI-7951, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.45×** | +4.2 | 0.001 | 9/36 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6162.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.615×** | -5.7 | 6e-06 | 21/37 (LOX-IMVI, H4, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.598×** | -5.5 | 1e-05 | 15/37 (LOX-IMVI, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.633×** | -5.4 | 1e-05 | 16/38 (NCI-H2030, A549, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -5.2 | 4e-05 | 20/32 (LOX-IMVI, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.664×** | -4.4 | 0.001 | 14/38 (Panc 03.27, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.693×** | -4.2 | 0.003 | 13/28 (hTERT-HPNE, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **0.543×** | -3.8 | 0.013 | 11/32 (C32, NCI-H1573, …) | rises with dose | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.734×** | -3.6 | 0.019 | 12/38 (Panc 03.27, AsPC-1, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.756×** | -3.3 | 0.061 | 9/38 (BT-474, NCI-H2030, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.46 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6162. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LOX-IMVI (line)]] | wt | 35.6 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0786× (z -17.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.138× (z -9.8) |
| [[NCI-H1573 (line)]] | alt | 20.7 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.36× (z +12.1) | [[Dinaciclib (drug)]] 0.5 µM 0.103× (z -13.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[A549 (line)]] | wt | 21.2 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.158× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~8% of this change |
| [[CFPAC-1 (line)]] | alt | 13.2 | 2 | 0 | [[Tucidinostat (drug)]] 5 µM 3.51× (z +8.8) | — |
| [[HOP62 (line)]] | alt | 8.87 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.61× (z +12.5) | — |
| [[Hs 766T (line)]] | wt | 7.36 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.2× (z +14.1) | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0831× (z -9.4) |
| [[NCI-H1792 (line)]] | alt | 9.25 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.01× (z +9.3) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0815× (z -10.2) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 2.82 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.00× (z +10.2) | — |
| [[A498 (line)]] | wt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.13× (z +9.4) | — |
| [[BT-474 (line)]] | alt | 9.25 | 0 | 1 (1 ⚠) | — | [[Neratinib (maleate) (drug)]] 0.5 µM 0.0501× (z -11.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C32 (line)]] | wt | 8.67 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.23× (z +8.6) | — |
| [[HepG2_C3A (line)]] | wt | 3.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.7× (z +9.0) | — |
| [[HS-578T (line)]] | alt | 6.70 | 0 | 1 | — | [[Radotinib (drug)]] 0.5 µM 0.0498× (z -10.8) |
| [[hTERT-HPNE (line)]] | wt | 25.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0797× (z -9.5) ⚠ toxic |
| [[LoVo (line)]] | wt | 3.38 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.35× (z +9.8) | — |
| [[LS 180 (line)]] | wt | 2.86 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 8.41× (z +8.8) | — |
| [[NCI-H2030 (line)]] | alt | 9.77 | 0 | 1 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0157× (z -19.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 13.5 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 3.06× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 11.2 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.43× (z +10.4) | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 4.04× (z +8.9) | — |
| [[SW 900 (line)]] | alt | 7.91 | 1 | 0 | [[Tucidinostat (drug)]] 5 µM 6.25× (z +9.3) | — |
| [[A-172 (line)]] | wt | 2.42 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.43 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.94 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.37 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.64 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.68 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 8.91 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.97 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.82 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.72 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.4 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.12 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.26 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.75 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 1.68 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6162), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SAA4]] | +0.55 | +0.51 / +0.60 | both halves | 1e-05 |  |
| [[MEF2C-AS1]] | +0.54 | +0.52 / +0.45 | both halves | 3e-05 |  |
| [[SHOC1]] | +0.54 | +0.51 / +0.50 | both halves | 1e-05 |  |
| [[DCC]] | +0.54 | +0.45 / +0.56 | both halves | 3e-05 |  |
| [[PPFIA2]] | +0.52 | +0.48 / +0.52 | both halves | 2e-05 |  |
| [[SYNPO2]] | +0.52 | +0.55 / +0.42 | both halves | 4e-05 |  |
| [[ST8SIA1]] | +0.51 | +0.47 / +0.54 | both halves | 2e-05 |  |
| [[SAA2-SAA4]] | +0.50 | +0.50 / +0.53 | both halves | 1e-05 |  |
| [[FAP]] | +0.50 | +0.55 / +0.27 | both halves | 3e-04 |  |
| [[THSD7B]] | +0.50 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SOCS3-DT]] | +0.49 | +0.38 / +0.46 | both halves | 7e-05 |  |
| [[PTPRO]] | +0.49 | +0.43 / +0.49 | both halves | 3e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FN3K]] | -0.41 | -0.26 / -0.40 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*9 arrows, 9 of them with an alert ⚠; grade A 0, B 7, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSD11B1]] | B | HSD11B1 activity raises STAT4's level | lines that do not express HSD11B1 (34) vs lines expressing it (16) | 2.18× lower at baseline in the lines without HSD11B1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC01411, NID2, EDNRA |
| [[CFH]] | B | CFH activity raises STAT4's level | lines that do not express CFH (28) vs lines expressing it (22) | 2.10× lower at baseline in the lines without CFH | 0.030 | ⚠ within organs, on part of the lines; also absent: HSD11B1, ADAMTS9-AS2, COL22A1 |
| [[TOP2A]] | B | TOP2A activity lowers STAT4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 5.6% of all compounds | 0.041 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MSC-AS1]] | B | MSC-AS1 activity raises STAT4's level | lines that do not express MSC-AS1 (27) vs lines expressing it (23) | 2.11× lower at baseline in the lines without MSC-AS1 | 0.055 | ⚠ within organs, on part of the lines; also absent: ADAM12, CNRIP1, FMN2 |
| [[RNF217-AS1]] | B | RNF217-AS1 activity raises STAT4's level | lines that do not express RNF217-AS1 (9) vs lines expressing it (41) | 2.39× lower at baseline in the lines without RNF217-AS1 | 0.058 | ⚠ within organs, on part of the lines; also absent: RNF217, LRP12, CCDC149; maybe low, not absent |
| [[TNIP3]] | B | TNIP3 activity raises STAT4's level | lines that do not express TNIP3 (33) vs lines expressing it (17) | 2.29× lower at baseline in the lines without TNIP3 | 0.060 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: SERPINB11, TMPRSS15, INHBA |
| [[SLC9A9]] | B | SLC9A9 activity raises STAT4's level | lines that do not express SLC9A9 (5) vs lines expressing it (45) | 2.13× lower at baseline in the lines without SLC9A9 | 0.077 | ⚠ within organs, on part of the lines; also absent: CNN3, SLC35F1, HACE1; maybe low, not absent |
| [[PLSCR2]] | C | PLSCR2 activity raises STAT4's level | lines that do not express PLSCR2 (6) vs lines expressing it (44) | 2.85× lower at baseline in the lines without PLSCR2 | 0.023 | ⚠ within organs, on part of the lines; also absent: TRIB1, SLC2A1, CEMIP2; maybe low, not absent; co-absent with the target |
| [[YBX3]] | C | YBX3 activity raises STAT4's level | lines that do not express YBX3 (4) vs lines expressing it (46) | 1.60× lower at baseline in the lines without YBX3 | 0.089 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: SPATA13, RNF103-CHMP3; maybe low, not absent; its own permutation p |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IL32]] | B | STAT4 activity raises IL32's level | lines that do not express STAT4 (7) vs lines expressing it (43) | 2.71× lower at baseline in the lines without STAT4 | 0.057 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent |
| [[PKIA-AS1]] | B | STAT4 activity raises PKIA-AS1's level | lines that do not express STAT4 (7) vs lines expressing it (43) | 2.34× lower at baseline in the lines without STAT4 | 0.067 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent |
| [[SOCS3-DT]] | B | STAT4 activity strengthens SOCS3-DT's drug response | lines that do not express STAT4 (7) vs lines expressing it (35) | the lines without STAT4 respond 1.07× as strongly (z diff -0.09); strongest at Doxorubicin (hydrochloride) 5 µM: 2.18x vs 3.97x (z diff +2.5) | 0.081 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[RNF217-AS1]] | B | STAT4 activity raises RNF217-AS1's level | lines that do not express STAT4 (7) vs lines expressing it (43) | 3.12× lower at baseline in the lines without STAT4 | 0.089 | ⚠ within organs, on part of the lines; also absent: PLSCR2, ZPLD1, SMAD7; maybe low, not absent |

## Where it sits

- **Module**: [[Module 150]]; 30 genes; every member is in the + arm (projection on the module's main direction 0.559). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (25.8, 26.9); signed map (36.5, 15.4). **Vector** length 71.1, 13.2% of its response variance represented; |z| ≥ 3 in 1,047 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.5 | +25.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +8.1 | +17.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +6.8 | +11.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.1 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.9 | +5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.8 | +8.2 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.4 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.9 | +4.5 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.8 | +3.1 |
| fall | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -2.6 | -3.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -2.0 | -0.5 |
|  | [[Tofacitinib (drug)]] 5 µM |  | -1.9 | -0.3 |
|  | [[Belinostat (drug)]] 5 µM |  | -1.7 | +6.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.6 | -1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.0 |

## What is on record

|  |  |
|---|---|
| Name | signal transducer and activator of transcription 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q32.2-q32.3 — chr2:191,029,576-191,178,435 (-) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; Signal transducer and activator of transcription family |
| Hallmark sets | ALLOGRAFT_REJECTION, INTERFERON_GAMMA_RESPONSE |
| Reactome | 12 pathways, smallest: Interleukin-23 signaling; Differentiation of naive CD4+ T cells to T helper 1 cells (Th1 cells); Interleukin-21 signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q14765](https://www.uniprot.org/uniprotkb/Q14765) (Signal transducer and activator of transcription 4):

> Transcriptional regulator mainly expressed in hematopoietic cells that plays a critical role in cellular growth, differentiation and immune response. Plays a key role in the differentiation of T-helper 1 cells and the production of interferon-gamma. Also participates in multiple neutrophil functions including chemotaxis and production of the neutrophil extracellular traps (By similarity). After IL12 binding to its receptor IL12RB2, STAT4 interacts with the intracellular domain of IL12RB2 and …

**Summary**, from NCBI Gene [6775](https://www.ncbi.nlm.nih.gov/gene/6775):

> The protein encoded by this gene is a member of the STAT family of transcription factors. In response to cytokines and growth factors, STAT family members are phosphorylated by the receptor associated kinases, and then form homo- or heterodimers that translocate to the cell nucleus where they act as transcription activators. This protein is essential for mediating responses to IL12 in lymphocytes, and regulating the differentiation of T helper cells. Mutations in this gene may be associated …

**Accessions** — [HGNC:11365](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11365) · Entrez [6775](https://www.ncbi.nlm.nih.gov/gene/6775) · UniProt [Q14765](https://www.uniprot.org/uniprotkb/Q14765) · Ensembl [ENSG00000138378](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138378)

## Data

Gene col 6162: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6162); `tables/drug_effects.parquet` (44 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6162, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6162]; `tensor/DDL_lfc|DDL_z.npy` [6162]; `embed/gene_vectors.npy` [6162]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6162 or target_col == 6162). Every well: [[STAT4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/STAT4.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
