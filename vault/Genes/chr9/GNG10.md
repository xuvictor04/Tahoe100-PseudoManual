---
symbol: "GNG10"
type: "gene"
col: 14324
ensembl_id: "ENSG00000242616"
name: "G protein subunit gamma 10"
location: "9q31.3"
module: 29
arm: "+"
pooled_cpm: 17.46
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 7
n_dd_up_clean: 4
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/029"]
generated_by: "tahoemap"
---

# GNG10

*G protein subunit gamma 10* — 9q31.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.15× (z +18.9, q 0e+00, up in 38 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Vinblastine (sulfate) (drug)]] 0.5 µM: 1.22× (z +3.5, q 0.033, up in 12 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[GSK1059615 (drug)]] 5 µM: 0.469× (z -6.9, q 2e-09, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (94 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AK3]] (+0.54, fdr 3e-05), [[EMB]] (+0.52, fdr 5e-05), [[TMEM64]] (+0.50, fdr 4e-05); moves opposite to [[CDT1]] (-0.49, fdr 1e-04), [[SAP30BP]] (-0.46, fdr 9e-05), [[SDE2]] (-0.46, fdr 2e-04).
> It sits in the **+** arm of [[Module 029]] (Neutrophil degranulation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PSMB5]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 9 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14324.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.15×** | +18.9 | 0e+00 | 38/42 (HOP62, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.91×** | +18.0 | 0e+00 | 27/28 (NCI-H460, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +13.7 | 2e-40 | 26/32 (HOP62, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.14× | +8.1 | 9e-14 | 8/48 (PANC-1, NCI-H2030, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~32% of this change | **1.37×** | +5.5 | 4e-06 | 19/43 (SW 900, RPMI-7951, …) | inconsistent across doses | low cells (technical?) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.6 | 0.033 | 8/26 (A-172, HOP62, …) | top dose only | noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.22×** | +3.5 | 0.033 | 12/47 (HOP62, A-172, …) | two highest doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.21×** | +3.4 | 0.049 | 14/47 (A498, SW 900, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Pralsetinib (drug)]] 5 µM |  | **1.44×** | +3.3 | 0.054 | 7/45 (A498, RKO, …) | top dose only | noisy plate (z scaled) |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.30×** | +3.3 | 0.060 | 13/44 (NCI-H460, NCI-H1573, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.21×** | +3.2 | 0.078 | 14/44 (MIA PaCa-2, SW1417, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **1.25×** | +3.1 | 0.089 | 4/47 (SNU-423, SW 900, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | 1.19× | +3.1 | 0.089 | 7/47 (HOP62, PANC-1, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 4 with an alert ⚠. 7 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14324.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[GSK1059615 (drug)]] 5 µM |  | **0.469×** | -6.9 | 2e-09 | 32/46 (HEC-1-A, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Panobinostat (drug)]] 5 µM |  | **0.683×** | -6.7 | 6e-09 | 27/48 (RKO, SW480, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.685×** | -6.6 | 6e-09 | 25/48 (RKO, BT-474, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.799×** | -5.5 | 4e-06 | 23/47 (RKO, COLO 205, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.786×** | -3.8 | 0.018 | 16/48 (C32, SK-MEL-2, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 5 µM |  | **0.809×** | -3.6 | 0.033 | 12/47 (NCI-H460, C-33 A, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.830×** | -3.3 | 0.089 | 9/47 (PANC-1, NCI-H460, …) | rises with dose |  |
| [[Ralimetinib dimesylate (drug)]] 0.05 µM | ⚠ unreliable plate only | 0.799× | -3.1 | 0.13 | 4/48 (COLO 205, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~6% of this change | 0.839× | -3.1 | 0.13 | 14/47 (RKO, BT-474, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14324. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 39.8 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.229× (z -15.2) |
| [[HOP62 (line)]] | alt | 19.5 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.08× (z +11.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1792 (line)]] | alt | 15.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.23× (z +9.6) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 18.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.84× (z +11.2) ⚠ toxic; transcription drop | — |
| [[SNU-423 (line)]] | alt | 24.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.53× (z +10.6) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 20.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.62× (z +9.3) ⚠ toxic; transcription drop | — |
| [[A498 (line)]] | wt | 18.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.08× (z +8.8) ⚠ toxic; transcription drop | — |
| [[BT-474 (line)]] | alt | 11.9 | 0 | 1 | — | [[Panobinostat (drug)]] 0.5 µM 0.137× (z -8.5) |
| [[C-33 A (line)]] | alt | 23.3 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.195× (z -8.6) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[COLO 205 (line)]] | alt | 9.36 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -13.3) |
| [[J82 (line)]] | alt | 30.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.420× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 16.4 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.47× (z +10.4) ⚠ toxic; transcription drop | — |
| [[NCI-H1573 (line)]] | alt | 9.96 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.22× (z +8.5) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 19.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.64× (z +11.0) ⚠ toxic; transcription drop | — |
| [[Panc 03.27 (line)]] | alt | 20.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.52× (z +8.6) ⚠ toxic; transcription drop | — |
| [[SNU-1 (line)]] | wt | 23.0 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.141× (z -10.0) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.47× (z +9.1) ⚠ toxic; transcription drop | — |
| [[A-427 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 14.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 27.9 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 9.01 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 14.9 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 16.3 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.6 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 14.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14324), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*80 of its nearest partners move with it, 4 of them with an alert (⚠; 4 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AK3]] | +0.54 | +0.49 / +0.45 | both halves | 3e-05 |  |
| [[EMB]] | +0.52 | +0.39 / +0.52 | both halves | 5e-05 |  |
| [[TMEM64]] | +0.50 | +0.41 / +0.42 | both halves | 4e-05 |  |
| [[PPIC]] | +0.50 | +0.52 / +0.38 | both halves | 6e-05 |  |
| [[LEPROT]] | +0.49 | +0.42 / +0.46 | both halves | 4e-05 |  |
| [[GNG12]] | +0.49 | +0.43 / +0.42 | both halves | 4e-05 | same gene group; pathway: ADORA2B mediated anti-inflammatory cytokines production; STRING 726 |
| [[USP46]] | +0.49 | +0.44 / +0.39 | both halves | 6e-05 |  |
| [[TMEM38B]] | +0.49 | +0.40 / +0.36 | both halves | 1e-04 |  |
| [[TWSG1]] | +0.49 | +0.42 / +0.57 | both halves | 4e-05 |  |
| [[IL13RA1]] | +0.48 | +0.46 / +0.45 | both halves | 3e-05 |  |
| [[RHOBTB3]] | +0.47 | +0.44 / +0.37 | both halves | 8e-05 |  |
| [[ADAM9]] | +0.47 | +0.32 / +0.49 | both halves | 2e-04 |  |

## Genes that move opposite

*20 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CDT1]] | -0.49 | -0.33 / -0.52 | both halves | 1e-04 |  |
| [[SAP30BP]] | -0.46 | -0.36 / -0.43 | both halves | 9e-05 |  |
| [[SDE2]] | -0.46 | -0.32 / -0.43 | both halves | 2e-04 |  |
| [[PHRF1]] | -0.46 | -0.24 / -0.49 | both halves | 5e-04 |  |
| [[NUP214]] | -0.42 | -0.42 / -0.30 | both halves | 2e-04 |  |
| [[EVA1A-AS]] | -0.42 | -0.36 / -0.45 | both halves | 9e-05 |  |
| [[HAUS8]] | -0.41 | -0.26 / -0.46 | both halves | 3e-04 |  |
| [[GTF3C5]] | -0.41 | -0.32 / -0.41 | both halves | 2e-04 |  |
| [[GPATCH1]] | -0.41 | -0.29 / -0.44 | both halves | 2e-04 |  |
| [[LENG1]] | -0.41 | -0.36 / -0.37 | both halves | 1e-04 |  |
| [[CWC25]] | -0.41 | -0.44 / -0.31 | both halves | 2e-04 |  |
| [[HAUS3]] | -0.40 | -0.34 / -0.35 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMB5]] | B | PSMB5 activity raises GNG10's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 029]] — Neutrophil degranulation; 148 genes; this gene is in the **+** arm (projection on the module's main direction 0.436). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (-27.8, -20.5); signed map (-14.0, -40.1). **Vector** length 56.6, 8.41% of its response variance represented; |z| ≥ 3 in 676 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.2 | +18.9 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +4.1 | +18.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.0 | +13.7 |
|  | [[Belinostat (drug)]] 0.5 µM |  | +2.4 | +3.4 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +2.1 | -0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.6 | +2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.4 | +1.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.3 | +3.5 |
| fall | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | -2.2 | -3.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.0 | -6.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -1.9 | -6.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.7 | -6.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.7 | -2.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.2 | -0.5 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -1.0 | -0.8 |
|  | [[TAK-733 (drug)]] 5 µM |  | -1.0 | -0.3 |

## What is on record

|  |  |
|---|---|
| Name | G protein subunit gamma 10 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 9q31.3 — chr9:111,661,605-111,670,226 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | G protein subunits gamma |
| Reactome | 66 pathways, smallest: G beta:gamma signalling through BTK; Prostacyclin signalling through prostacyclin receptor; G beta:gamma signalling through PLC beta |
| Matched by | ensembl_id |

**Function**, from UniProt [P50151](https://www.uniprot.org/uniprotkb/P50151) (Guanine nucleotide-binding protein G(I)/G(S)/G(O) subunit gamma-10):

> Guanine nucleotide-binding proteins (G proteins) are involved as a modulator or transducer in various transmembrane signaling systems. The beta and gamma chains are required for the GTPase activity, for replacement of GDP by GTP, and for G protein-effector interaction. Interacts with beta-1 and beta-2, but not with beta-3.

**Summary**, from NCBI Gene [2790](https://www.ncbi.nlm.nih.gov/gene/2790):

> Predicted to enable G-protein beta-subunit binding activity. Predicted to be involved in G protein-coupled receptor signaling pathway. Predicted to be located in plasma membrane. Predicted to be part of heterotrimeric G-protein complex. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:4402](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4402) · Entrez [2790](https://www.ncbi.nlm.nih.gov/gene/2790) · UniProt [P50151](https://www.uniprot.org/uniprotkb/P50151) · Ensembl [ENSG00000242616](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000242616)

## Data

Gene col 14324: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14324); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14324, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14324]; `tensor/DDL_lfc|DDL_z.npy` [14324]; `embed/gene_vectors.npy` [14324]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14324 or target_col == 14324). Every well: [[GNG10 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GNG10.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
