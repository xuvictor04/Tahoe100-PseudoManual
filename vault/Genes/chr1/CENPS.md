---
symbol: "CENPS"
type: "gene"
col: 10589
ensembl_id: "ENSG00000175279"
name: "centromere protein S"
location: "1p36.22"
module: 16
arm: "+"
pooled_cpm: 6.66
n_lines_expressing: 49
n_dd_up: 17
n_dd_down: 3
n_dd_up_clean: 3
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/016"]
generated_by: "tahoemap"
---

# CENPS

*centromere protein S* — 1p36.22

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (14 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 6.09× (z +16.1, q 0e+00, up in 25 of 25 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change. The strongest without an alert is [[Belumosudil (drug)]] 5 µM: 1.74× (z +4.8, q 1e-04, up in 17 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.570× (z -5.1, q 2e-04, down in 25 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 4 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DYNC2I2]] (+0.64, fdr 7e-06), [[LRRCC1]] (+0.63, fdr 7e-06), [[CEP41]] (+0.62, fdr 1e-05); moves opposite to [[PPP1R32]] (-0.56, fdr 1e-05), [[TMED7-TICAM2]] (-0.55, fdr 2e-05), [[RPL38]] (-0.55, fdr 6e-05).
> It sits in the **+** arm of [[Module 016]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ZNF681]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 14 with an alert ⚠; shown: the 15 strongest. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10589.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | **6.09×** | +16.1 | 0e+00 | 25/25 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **6.02×** | +15.6 | 0e+00 | 12/12 (PANC-1, A498, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **4.01×** | +11.6 | 9e-29 | 16/16 (HEC-1-A, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **2.08×** | +6.6 | 7e-09 | 33/46 (SW480, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.93×** | +5.7 | 2e-06 | 26/45 (PANC-1, MIA PaCa-2, …) | rises with dose | composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~26% of this change | **1.78×** | +5.0 | 6e-05 | 15/31 (CFPAC-1, PANC-1, …) | rises with dose | position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.74×** | +4.8 | 1e-04 | 17/43 (SNU-423, NCI-H1792, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.70×** | +4.8 | 1e-04 | 26/46 (SW480, KATO III, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.44×** | +4.6 | 2e-04 | 15/45 (HS-578T, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | **1.43×** | +4.5 | 3e-04 | 19/40 (PANC-1, A549, …) | all doses, stronger at high dose | composition shift; position effect removed |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.59×** | +4.2 | 0.002 | 25/46 (LoVo, HepG2/C3A, …) | top dose only |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **1.35×** | +3.8 | 0.006 | 17/42 (BT-474, A498, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~61% of this change | **1.51×** | +3.6 | 0.014 | 11/35 (SNU-423, PANC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **1.46×** | +3.3 | 0.034 | 15/45 (NCI-H460, A498, …) | rises with dose |  |
| [[Pralsetinib (drug)]] 5 µM |  | **1.99×** | +3.2 | 0.046 | 6/31 (PANC-1, SHP-77, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 10589.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.570×** | -5.1 | 2e-04 | 25/46 (HT-29, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.604×** | -4.6 | 0.001 | 25/44 (NCI-H23, LoVo, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.663×** | -3.7 | 0.037 | 20/44 (SW48, COLO 205, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | 0.691× | -3.3 | 0.14 | 9/43 (A-172, LoVo, …) | inconsistent across doses | low cells (technical?) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.62 per unit of S-phase module lfc, +0.22 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10589. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 9.97 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.34× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[PANC-1 (line)]] | alt | 14.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.09× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[SW480 (line)]] | alt | 8.51 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.14× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-172 (line)]] | wt | 4.36 | 0 | 1 | — | [[Talc (drug)]] 0.5 µM 0.0674× (z -9.7) |
| [[A498 (line)]] | wt | 4.57 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.34× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[BT-474 (line)]] | alt | 4.59 | 0 | 1 | — | [[Fulvestrant (drug)]] 0.05 µM 0.0694× (z -8.5) |
| [[HOP62 (line)]] | alt | 8.43 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.98× (z +8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[HS-578T (line)]] | alt | 7.71 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 8.64× (z +8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[J82 (line)]] | alt | 7.77 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0895× (z -11.6) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 5.90 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.0× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[NCI-H23 (line)]] | alt | 11.3 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.112× (z -10.6) |
| [[NCI-H460 (line)]] | wt | 5.92 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 8.76× (z +10.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | — |
| [[A-427 (line)]] | wt | 11.5 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.99 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.46 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.51 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.50 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.89 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 6.31 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 7.00 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.41 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.48 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.69 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.72 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.64 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.27 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.43 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.19 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 3.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 7.82 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 4.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.70 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.23 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.96 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.77 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 6.13 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.50 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.49 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 5.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 6.88 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10589), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DYNC2I2]] | +0.64 | +0.63 / +0.65 | both halves | 7e-06 |  |
| [[LRRCC1]] | +0.63 | +0.60 / +0.63 | both halves | 7e-06 |  |
| [[CEP41]] | +0.62 | +0.66 / +0.50 | both halves | 1e-05 | pathway: Mitotic Prometaphase |
| [[DHX9]] | +0.61 | +0.62 / +0.44 | both halves | 3e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[DCLRE1A]] | +0.61 | +0.71 / +0.54 | both halves | 1e-05 | pathway: Fanconi Anemia Pathway; STRING 674 |
| [[SLX4IP]] | +0.61 | +0.68 / +0.44 | both halves | 3e-05 |  |
| [[COMMD8]] | +0.61 | +0.63 / +0.57 | both halves | 1e-05 |  |
| [[ZNF252P-1]] | +0.58 | +0.67 / +0.52 | both halves | 1e-05 |  |
| [[DHRS4L2]] | +0.57 | +0.62 / +0.60 | both halves | 7e-06 |  |
| [[RBBP9]] | +0.57 | +0.57 / +0.49 | both halves | 1e-05 |  |
| [[HIRIP3]] | +0.57 | +0.63 / +0.54 | both halves | 1e-05 |  |
| [[ZNF678]] | +0.57 | +0.63 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP1R32]] | -0.56 | -0.58 / -0.53 | both halves | 1e-05 |  |
| [[TMED7-TICAM2]] | -0.55 | -0.58 / -0.48 | both halves | 2e-05 |  |
| [[RPL38]] | -0.55 | -0.62 / -0.38 | both halves | 6e-05 |  |
| [[RPL28]] | -0.54 | -0.62 / -0.42 | both halves | 4e-05 |  |
| [[RPS11]] | -0.54 | -0.64 / -0.40 | both halves | 5e-05 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[RPS13]] ⚠ | -0.51 | -0.61 / -0.31 | both halves | 2e-04 | pathway: Antimicrobial mechanism of IFN-stimulated genes; ⚠ in the vector space only through flagged drug-doses |
| [[GUK1]] | -0.51 | -0.67 / -0.36 | both halves | 9e-05 |  |
| [[FAU]] | -0.51 | -0.46 / -0.34 | both halves | 1e-04 | pathway: Antimicrobial mechanism of IFN-stimulated genes |
| [[DRD4]] | -0.51 | -0.53 / -0.49 | both halves | 1e-05 |  |
| [[BET1L]] | -0.51 | -0.56 / -0.49 | both halves | 1e-05 |  |
| [[RPLP2]] | -0.50 | -0.64 / -0.35 | both halves | 1e-04 |  |
| [[TPT1]] | -0.50 | -0.51 / -0.42 | both halves | 4e-05 |  |
| [[RPL27A]] | -0.50 | -0.51 / -0.45 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF681]] | B | ZNF681 activity raises CENPS's level | lines that do not express ZNF681 (16) vs lines expressing it (34) | 1.32× lower at baseline in the lines without ZNF681 | 0.067 | ⚠ within organs, on part of the lines; also absent: RPSAP58, ZNF649, ZNF793 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 016]]; 206 genes; this gene is in the **+** arm (projection on the module's main direction 0.479). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-26.7, -37.5); signed map (4.9, -36.3). **Vector** length 52.2, 7.62% of its response variance represented; |z| ≥ 3 in 783 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~31% of this change | +5.1 | +16.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +4.7 | +15.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | +4.4 | +11.6 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +3.8 | +5.7 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~70% of this change | +3.4 | +4.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +2.0 | +4.8 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.5 | +1.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.4 | +2.2 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.9 |
|  | [[Pralsetinib (drug)]] 5 µM |  | +1.3 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -2.3 | -4.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.0 | -5.1 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.4 | -1.6 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -1.4 | -2.7 |
|  | [[Posaconazole (drug)]] 5 µM |  | -1.1 | -2.3 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.1 | -2.1 |
|  | [[Berbamine (dihydrochloride) (drug)]] 5 µM |  | -1.0 | -1.0 |
|  | [[Tirabrutinib (hydrochloride) (drug)]] 0.5 µM |  | -0.9 | -1.7 |
|  | [[Auranofin (drug)]] 5 µM |  | -0.9 | +0.4 |

## What is on record

|  |  |
|---|---|
| Name | centromere protein S |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.22 — chr1:10,430,433-10,442,808 (+) |
| Ensembl biotype | protein_coding |
| Also known as | CENP-S, FAAP16; previously APITD1, MHF1 |
| Gene groups (HGNC) | Constitutive centromere associated network |
| Reactome | 26 pathways, smallest: Fanconi Anemia Pathway; Deposition of new CENPA-containing nucleosomes at the centromere; Nucleosome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8N2Z9](https://www.uniprot.org/uniprotkb/Q8N2Z9) (Centromere protein S):

> DNA-binding component of the Fanconi anemia (FA) core complex. Required for the normal activation of the FA pathway, leading to monoubiquitination of the FANCI-FANCD2 complex in response to DNA damage, cellular resistance to DNA cross-linking drugs, and prevention of chromosomal breakage. In complex with CENPX (MHF heterodimer), crucial cofactor for FANCM in both binding and ATP-dependent remodeling of DNA. Stabilizes FANCM. In complex with CENPX and FANCM (but not other FANC proteins), rapidly …

**Summary**, from NCBI Gene [378708](https://www.ncbi.nlm.nih.gov/gene/378708):

> This gene was identified in the neuroblastoma tumor suppressor candidate region on chromosome 1p36. It contains a TFIID-31 domain, similar to that found in TATA box-binding protein-associated factor, TAF(II)31, which is required for p53-mediated transcription activation. This gene was expressed at very low levels in neuroblastoma tumors, and was shown to reduce cell growth in neuroblastoma cells, suggesting that it may have a role in a cell death pathway. The protein is a component of multiple …

**Accessions** — [HGNC:23163](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23163) · Entrez [378708](https://www.ncbi.nlm.nih.gov/gene/378708) · UniProt [Q8N2Z9](https://www.uniprot.org/uniprotkb/Q8N2Z9) · Ensembl [ENSG00000175279](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000175279)

## Data

Gene col 10589: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10589); `tables/drug_effects.parquet` (21 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10589, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10589]; `tensor/DDL_lfc|DDL_z.npy` [10589]; `embed/gene_vectors.npy` [10589]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10589 or target_col == 10589). Every well: [[CENPS — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CENPS.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
