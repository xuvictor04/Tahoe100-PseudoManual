---
symbol: "CCDC127"
type: "gene"
col: 8939
ensembl_id: "ENSG00000164366"
name: "coiled-coil domain containing 127"
location: "5p15.33"
module: 24
arm: "+"
pooled_cpm: 14.93
n_lines_expressing: 50
n_dd_up: 7
n_dd_down: 18
n_dd_up_clean: 5
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/024"]
generated_by: "tahoemap"
---

# CCDC127

*coiled-coil domain containing 127* — 5p15.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 7 drug-doses (2 with an alert ⚠); the strongest is [[Adagrasib (drug)]] 0.05 µM: 1.15× (z +7.1, q 7e-10, up in 8 of 48 measured lines) ⚠ position not correctable. The strongest without an alert is [[Selinexor (drug)]] 5 µM: 1.20× (z +3.6, q 0.038, up in 14 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 18 drug-doses (5 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.559× (z -11.3, q 8e-27, down in 36 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CYB561D1]] (+0.71, fdr 1e-05), [[MED10]] (+0.68, fdr 7e-06), [[PCGF1]] (+0.68, fdr 1e-05, ⚠ PCGF1 in the vector space only through flagged drug-doses), [[ZCCHC9]] (+0.67, fdr 1e-05); moves opposite to [[SEPTIN11]] (-0.65, fdr 1e-05), [[IL13RA1]] (-0.64, fdr 1e-05), [[DARS2]] (-0.61, fdr 1e-05).
> It sits in the **+** arm of [[Module 024]] (Aerobic respiration and respiratory electron transport).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 3 with an alert ⚠. 7 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.15× | +7.1 | 7e-10 | 8/48 (NCI-H1792, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +5.7 | 3e-06 | 24/43 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +5.1 | 5e-05 | 23/44 (Panc 03.27, NCI-H2347, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~12% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.20×** | +3.6 | 0.038 | 14/48 (J82, KATO III, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.042 | 15/48 (AsPC-1, PANC-1, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.27×** | +3.5 | 0.049 | 17/48 (BT-474, SHP-77, …) | two highest doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.29×** | +3.4 | 0.053 | 12/46 (LoVo, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **1.40×** | +3.3 | 0.058 | 12/47 (MIA PaCa-2, CHP-212, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | 1.23× | +3.0 | 0.15 | 10/48 (A-172, KATO III, …) | rises with dose | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 5 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.559×** | -11.3 | 8e-27 | 36/47 (SNU-423, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.372×** | -7.4 | 4e-11 | 34/48 (NCI-H1792, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.602×** | -7.0 | 6e-10 | 30/46 (HOP62, A-172, …) | rises with dose | cell-cycle shift (explains ~14% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.708×** | -6.6 | 4e-09 | 28/45 (CFPAC-1, HOP62, …) | top dose only | cell-cycle shift (explains ~17% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.619×** | -6.6 | 6e-09 | 29/44 (HOP62, SW480, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.663×** | -5.9 | 4e-07 | 26/48 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.475×** | -5.6 | 2e-06 | 21/45 (RKO, RPMI-7951, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.676×** | -5.4 | 5e-06 | 26/43 (Panc 03.27, HOP62, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.694×** | -5.2 | 1e-05 | 21/48 (NCI-H460, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.695×** | -5.2 | 1e-05 | 22/48 (A498, NCI-H1792, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **0.717×** | -4.5 | 3e-04 | 23/47 (hTERT-HPNE, SNU-423, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.789×** | -4.4 | 4e-04 | 22/48 (HOP62, Hs 766T, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.738×** | -4.0 | 0.003 | 16/33 (NCI-H460, MIA PaCa-2, …) | all doses, flat | composition shift |
| [[Pemetrexed (drug)]] 0.5 µM |  | **0.771×** | -3.7 | 0.009 | 9/47 (A498, A549, …) | inconsistent across doses | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.772×** | -3.7 | 0.009 | 18/46 (SW1417, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.775×** | -3.6 | 0.011 | 17/46 (H4, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.781×** | -3.5 | 0.015 | 15/47 (HOP62, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~1% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.24 per unit of S-phase module lfc, +0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HOP62 (line)]] | alt | 22.7 | 0 | 4 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.250× (z -11.3) |
| [[hTERT-HPNE (line)]] | wt | 14.0 | 0 | 3 | — | [[Harringtonine (drug)]] 5 µM 0.0960× (z -10.3) |
| [[A-172 (line)]] | wt | 19.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.324× (z -11.0) |
| [[CFPAC-1 (line)]] | alt | 18.4 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -10.0) |
| [[SW 900 (line)]] | alt | 27.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.320× (z -10.3) |
| [[C-33 A (line)]] | alt | 12.2 | 0 | 1 | — | [[Topotecan (hydrochloride) (drug)]] 0.05 µM 0.0712× (z -10.2) |
| [[H4 (line)]] | wt | 17.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.100× (z -10.2) |
| [[Hs 766T (line)]] | wt | 24.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.151× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change |
| [[LoVo (line)]] | wt | 12.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.135× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change |
| [[MIA PaCa-2 (line)]] | alt | 16.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H1792 (line)]] | alt | 23.2 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -13.1) |
| [[NCI-H460 (line)]] | wt | 10.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0916× (z -15.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[SNU-423 (line)]] | alt | 14.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -14.7) |
| [[A-427 (line)]] | wt | 17.1 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 24.0 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 12.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 11.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.8 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 8.26 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.85 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.80 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 6.34 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 20.3 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 12.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 26.6 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.7 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.15 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 5 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYB561D1]] | +0.71 | +0.53 / +0.69 | both halves | 1e-05 |  |
| [[MED10]] | +0.68 | +0.62 / +0.69 | both halves | 7e-06 |  |
| [[PCGF1]] ⚠ | +0.68 | +0.55 / +0.69 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZCCHC9]] | +0.67 | +0.55 / +0.70 | both halves | 1e-05 |  |
| [[MRPL43]] | +0.65 | +0.44 / +0.64 | both halves | 3e-05 |  |
| [[TIMM29]] | +0.65 | +0.40 / +0.75 | both halves | 5e-05 |  |
| [[SMIM26]] ⚠ | +0.64 | +0.47 / +0.70 | both halves | 2e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ZNHIT3]] | +0.64 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[HAUS3]] | +0.64 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[PIGH]] | +0.63 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[R3HCC1]] | +0.63 | +0.47 / +0.63 | both halves | 2e-05 |  |
| [[PRUNE1]] | +0.63 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[CAMLG]] | +0.63 | +0.48 / +0.64 | both halves | 2e-05 |  |
| [[RPP21]] | +0.62 | +0.44 / +0.64 | both halves | 3e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SEPTIN11]] | -0.65 | -0.57 / -0.63 | both halves | 1e-05 |  |
| [[IL13RA1]] | -0.64 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[DARS2]] | -0.61 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[PTPRG]] | -0.60 | -0.52 / -0.55 | both halves | 1e-05 |  |
| [[TRIP12]] | -0.59 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[PSME3]] | -0.58 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[ATP11C]] | -0.58 | -0.46 / -0.54 | both halves | 3e-05 |  |
| [[ILF3]] | -0.58 | -0.49 / -0.53 | both halves | 1e-05 |  |
| [[RCC2]] | -0.58 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[LAMB1]] | -0.56 | -0.40 / -0.60 | both halves | 5e-05 |  |
| [[EPB41L2]] | -0.56 | -0.62 / -0.56 | both halves | 1e-05 |  |
| [[GSPT1]] | -0.56 | -0.41 / -0.66 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises CCDC127's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 3.9% of all compounds | 0.020 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 024]] — Aerobic respiration and respiratory electron transport; 179 genes; this gene is in the **+** arm (projection on the module's main direction 0.607). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-39.4, -13.7); signed map (-16.2, -3.5). **Vector** length 79.6, 14.8% of its response variance represented; |z| ≥ 3 in 838 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM |  | +3.9 | +3.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +5.7 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +3.3 | +2.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +3.6 |
|  | [[Selinexor (drug)]] 5 µM |  | +3.1 | +3.6 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.2 | +3.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | +1.8 | +3.4 |
|  | [[Auranofin (drug)]] 5 µM |  | +1.6 | +1.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +1.6 | +2.6 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~42% of this change | -6.3 | -3.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~64% of this change | -5.7 | -2.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | -5.5 | -4.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -7.0 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -4.9 | -6.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.5 | -4.4 |
|  | [[Clobetasol propionate (drug)]] 0.05 µM |  | -1.8 | -1.1 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -1.4 | -1.9 |
|  | [[Demeclocycline (drug)]] 5 µM |  | -1.4 | -1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -1.3 | -5.6 |

## What is on record

|  |  |
|---|---|
| Name | coiled-coil domain containing 127 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5p15.33 — chr5:196,868-218,153 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ25701 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96BQ5](https://www.uniprot.org/uniprotkb/Q96BQ5) (Coiled-coil domain-containing protein 127):

> Regulates lipid droplet homeostasis. May be involved in the adipocyte differentiation.

**Summary**, from NCBI Gene [133957](https://www.ncbi.nlm.nih.gov/gene/133957):

> Involved in lipid homeostasis. Located in mitochondrial outer membrane. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:30520](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:30520) · Entrez [133957](https://www.ncbi.nlm.nih.gov/gene/133957) · UniProt [Q96BQ5](https://www.uniprot.org/uniprotkb/Q96BQ5) · Ensembl [ENSG00000164366](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000164366)

## Data

Gene col 8939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8939); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8939]; `tensor/DDL_lfc|DDL_z.npy` [8939]; `embed/gene_vectors.npy` [8939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8939 or target_col == 8939). Every well: [[CCDC127 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CCDC127.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
