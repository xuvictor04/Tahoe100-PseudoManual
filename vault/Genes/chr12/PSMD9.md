---
symbol: "PSMD9"
type: "gene"
col: 3166
ensembl_id: "ENSG00000110801"
name: "proteasome 26S subunit, non-ATPase 9"
location: "12q24.31"
module: 30
arm: "+"
pooled_cpm: 30.34
n_lines_expressing: 50
n_dd_up: 20
n_dd_down: 9
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/030"]
generated_by: "tahoemap"
---

# PSMD9

*proteasome 26S subunit, non-ATPase 9* — 12q24.31

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 20 drug-doses (8 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 1.85× (z +9.9, q 2e-20, up in 40 of 47 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 1.70× (z +8.6, q 3e-15, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.737× (z -7.0, q 2e-09, down in 34 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[E4F1]] (+0.79, fdr 7e-06), [[SNTA1]] (+0.72, fdr 1e-05), [[RNF41]] (+0.70, fdr 1e-05); moves opposite to [[LEKR1]] (-0.63, fdr 5e-05), [[MPDU1]] (-0.63, fdr 1e-04), [[SLC16A9]] (-0.62, fdr 1e-04).
> It sits in the **+** arm of [[Module 030]].
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 8 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 20 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3166.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +9.9 | 2e-20 | 40/47 (KATO III, SW480, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **1.70×** | +8.6 | 3e-15 | 34/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.54×** | +7.0 | 5e-10 | 37/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.53×** | +6.9 | 8e-10 | 35/47 (SW480, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.51×** | +6.6 | 3e-09 | 34/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.47×** | +6.2 | 4e-08 | 33/48 (SW480, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.41×** | +5.3 | 7e-06 | 27/47 (LoVo, KATO III, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.36×** | +4.9 | 5e-05 | 28/47 (MIA PaCa-2, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~24% of this change | **1.35×** | +4.8 | 8e-05 | 25/48 (NCI-H460, SW480, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.37×** | +4.8 | 9e-05 | 24/48 (LoVo, PANC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change | **1.35×** | +4.7 | 1e-04 | 23/43 (NCI-H23, PANC-1, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 18/48 (PANC-1, HT-29, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **1.27×** | +3.8 | 0.007 | 16/47 (NCI-H460, LoVo, …) | rises with dose |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~52% of this change | **1.25×** | +3.6 | 0.014 | 17/46 (H4, CFPAC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | 1.17× | +3.5 | 0.015 | 16/48 (CFPAC-1, HT-29, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.31×** | +3.1 | 0.068 | 10/45 (HT-29, A-427, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.069 | 11/48 (Panc 03.27, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.21×** | +3.0 | 0.086 | 11/47 (A-172, CFPAC-1, …) | all doses, flat |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3166.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.737×** | -7.0 | 2e-09 | 34/47 (HS-578T, SW48, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.753×** | -4.6 | 0.001 | 24/48 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.823×** | -4.4 | 0.001 | 23/48 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.825×** | -4.4 | 0.001 | 18/48 (HOP62, LOX-IMVI, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **0.826×** | -4.4 | 0.001 | 24/48 (NCI-H2347, HOP62, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.847× | -3.8 | 0.015 | 21/47 (HS-578T, SK-MEL-2, …) | top dose only | composition shift |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **0.801×** | -3.6 | 0.027 | 18/48 (SNU-1, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.807×** | -3.5 | 0.039 | 9/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.804×** | -3.4 | 0.044 | 19/47 (SNU-423, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.812×** | -3.2 | 0.068 | 19/48 (NCI-H23, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, +0.26 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3166. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 43.0 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -9.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 38.7 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -12.9) |
| [[NCI-H460 (line)]] | wt | 29.2 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.74× (z +9.6) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 2.61× (z +9.2) | — |
| [[SK-MEL-2 (line)]] | alt | 31.5 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.378× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SW480 (line)]] | alt | 22.7 | 2 (1 ⚠) | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 2.57× (z +9.9) | — |
| [[A-172 (line)]] | wt | 33.7 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.428× (z -10.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[C-33 A (line)]] | alt | 23.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.201× (z -8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~32% of this change |
| [[hTERT-HPNE (line)]] | wt | 25.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.161× (z -10.3) |
| [[KATO III (line)]] | alt | 20.6 | 1 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 3.78× (z +9.9) ⚠ toxic; transcription drop | — |
| [[LS 180 (line)]] | wt | 27.4 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.55× (z +8.9) | — |
| [[SNU-423 (line)]] | alt | 29.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.252× (z -10.8) |
| [[SW48 (line)]] | wt | 32.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.357× (z -8.6) |
| [[A-427 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 50.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 34.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 31.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 27.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 20.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 25.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 34.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 27.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 19.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 42.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 33.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 26.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 25.4 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 31.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 39.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 29.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 48.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 30.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 36.1 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 26.3 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 23.1 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 25.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 27.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 27.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 32.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 27.5 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3166), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*84 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[E4F1]] | +0.79 | +0.77 / +0.69 | both halves | 7e-06 |  |
| [[SNTA1]] | +0.72 | +0.66 / +0.57 | both halves | 1e-05 | same gene group |
| [[RNF41]] | +0.70 | +0.63 / +0.51 | both halves | 1e-05 |  |
| [[SPSB3]] | +0.70 | +0.71 / +0.54 | both halves | 1e-05 |  |
| [[PCMT1]] | +0.69 | +0.70 / +0.37 | both halves | 9e-05 |  |
| [[LCMT1]] | +0.69 | +0.58 / +0.58 | both halves | 8e-06 |  |
| [[MIGA2]] | +0.68 | +0.42 / +0.61 | both halves | 4e-05 |  |
| [[ANKRD27]] | +0.68 | +0.67 / +0.38 | both halves | 7e-05 |  |
| [[WRAP73]] | +0.67 | +0.54 / +0.41 | both halves | 4e-05 |  |
| [[CCZ1B]] | +0.66 | +0.66 / +0.61 | both halves | 7e-06 |  |
| [[TECPR1]] | +0.66 | +0.48 / +0.47 | both halves | 2e-05 |  |
| [[SERAC1]] | +0.66 | +0.56 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*16 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEKR1]] | -0.63 | -0.64 / -0.39 | both halves | 5e-05 |  |
| [[MPDU1]] | -0.63 | -0.57 / -0.36 | both halves | 1e-04 |  |
| [[SLC16A9]] | -0.62 | -0.63 / -0.35 | both halves | 1e-04 |  |
| [[ZNF462]] | -0.62 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[EIF4G2]] | -0.62 | -0.53 / -0.38 | both halves | 7e-05 |  |
| [[DDX39B]] | -0.62 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[WAKMAR2]] | -0.61 | -0.59 / -0.27 | both halves | 3e-04 |  |
| [[CYREN]] | -0.60 | -0.65 / -0.35 | both halves | 1e-04 |  |
| [[STPG4]] | -0.60 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TASOR]] | -0.60 | -0.63 / -0.36 | both halves | 1e-04 |  |
| [[LINC00880]] | -0.60 | -0.60 / -0.21 | both halves | 6e-04 |  |
| [[LINC02955]] | -0.60 | -0.55 / -0.32 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises PSMD9's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.0% of all compounds | 0.005 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[SNTA1]] | B | SNTA1 activity raises PSMD9's level | lines that do not express SNTA1 (5) vs lines expressing it (45) | 1.32× lower at baseline in the lines without SNTA1 | 0.034 | ⚠ within organs, on part of the lines; also absent: SACS, CLTCL1, MXRA7; maybe low, not absent |
| [[TOP2B]] | B | TOP2B activity raises PSMD9's level | compounds that target TOP2B: 2 of 2 lower it (Doxorubicin, Mitoxantrone) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 030]]; 146 genes; this gene is in the **+** arm (projection on the module's main direction 0.726). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.37).
- **Nodal map** (x, y) = (1.9, -1.9); signed map (-36.2, -0.2). **Vector** length 94.5, 22.0% of its response variance represented; |z| ≥ 3 in 796 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +6.1 | +7.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | +6.0 | +6.6 |
|  | [[Belinostat (drug)]] 5 µM |  | +5.9 | +6.2 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +2.8 | +3.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +2.7 | +1.7 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.4 | +3.1 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +0.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -6.0 | -3.8 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -7.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.7 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.6 | -3.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -4.5 | -1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.7 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.3 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -0.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.3 | -3.5 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -1.9 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | proteasome 26S subunit, non-ATPase 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.31 — chr12:121,888,732-121,918,297 (+) |
| Ensembl biotype | protein_coding |
| Also known as | p27, Rpn4 |
| Gene groups (HGNC) | Proteasome; PDZ domain containing |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 1 pathways, smallest: Proteasome assembly |
| Matched by | ensembl_id |

**Function**, from UniProt [O00233](https://www.uniprot.org/uniprotkb/O00233) (26S proteasome non-ATPase regulatory subunit 9):

> Acts as a chaperone during the assembly of the 26S proteasome, specifically of the base subcomplex of the PA700/19S regulatory complex (RC). During the base subcomplex assembly is part of an intermediate PSMD9:PSMC6:PSMC3 module, also known as modulator trimer complex; PSMD9 is released during the further base assembly process.

**Summary**, from NCBI Gene [5715](https://www.ncbi.nlm.nih.gov/gene/5715):

> The 26S proteasome is a multicatalytic proteinase complex with a highly ordered structure composed of 2 complexes, a 20S core and a 19S regulator. The 20S core is composed of 4 rings of 28 non-identical subunits; 2 rings are composed of 7 alpha subunits and 2 rings are composed of 7 beta subunits. The 19S regulator is composed of a base, which contains 6 ATPase subunits and 2 non-ATPase subunits, and a lid, which contains up to 10 non-ATPase subunits. Proteasomes are distributed throughout …

**Accessions** — [HGNC:9567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9567) · Entrez [5715](https://www.ncbi.nlm.nih.gov/gene/5715) · UniProt [O00233](https://www.uniprot.org/uniprotkb/O00233) · Ensembl [ENSG00000110801](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000110801)

## Data

Gene col 3166: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3166); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3166, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3166]; `tensor/DDL_lfc|DDL_z.npy` [3166]; `embed/gene_vectors.npy` [3166]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3166 or target_col == 3166). Every well: [[PSMD9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PSMD9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
