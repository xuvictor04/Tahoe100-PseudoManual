---
symbol: "WNT3"
type: "gene"
col: 2939
ensembl_id: "ENSG00000108379"
name: "Wnt family member 3"
location: "17q21.31-q21.32"
module: 35
arm: "+"
pooled_cpm: 3.17
n_lines_expressing: 45
n_dd_up: 17
n_dd_down: 8
n_dd_up_clean: 12
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 6
direction_downstream: 1
tags: ["gene", "module/035"]
generated_by: "tahoemap"
---

# WNT3

*Wnt family member 3* — 17q21.31-q21.32

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 17 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 3.21× (z +16.2, q 0e+00, up in 26 of 28 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 0.5 µM: 0.399× (z -9.0, q 1e-16, down in 22 of 38 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GCNT4]] (+0.71, fdr 4e-05), [[POU6F1]] (+0.70, fdr 2e-05), [[PRDM11]] (+0.69, fdr 1e-04); moves opposite to [[IFT172]] (-0.70, fdr 1e-05), [[ALAD]] (-0.64, fdr 6e-05), [[GUSBP18]] (-0.60, fdr 5e-04).
> It sits in the **+** arm of [[Module 035]].
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[MSI1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[SUMO2P17]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 17 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2939.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **3.21×** | +16.2 | 0e+00 | 26/28 (SW480, NCI-H460, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **3.10×** | +10.7 | 3e-24 | 3/4 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.62×** | +9.5 | 5e-19 | 11/15 (J82, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.18×** | +7.4 | 3e-11 | 7/14 (SW480, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.21×** | +7.2 | 6e-11 | 5/6 (NCI-H2347, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **1.65×** | +6.9 | 4e-10 | 15/41 (SW480, Panc 03.27, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~15% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.72×** | +5.3 | 9e-06 | 14/36 (HEC-1-A, SK-MEL-2, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.41×** | +4.8 | 1e-04 | 11/31 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +4.1 | 0.003 | 8/40 (SW480, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.32×** | +3.8 | 0.007 | 6/38 (SW480, HOP62, …) | inconsistent across doses | position effect removed |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.44×** | +3.4 | 0.029 | 8/25 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.41×** | +3.4 | 0.030 | 10/27 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Palmatine (chloride) (drug)]] 0.5 µM |  | **1.39×** | +3.2 | 0.051 | 4/21 (A-427, SW1417, …) | inconsistent across doses |  |
| [[Neratinib (drug)]] 0.05 µM |  | **1.38×** | +3.2 | 0.051 | 5/32 (A549, SW480, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.051 | 5/21 (LoVo, J82, …) | inconsistent across doses | low cells (technical?) |
| [[Peretinoin (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.051 | 2/35 (HOP62, NCI-H1573) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 2939.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 0.5 µM |  | **0.399×** | -9.0 | 1e-16 | 22/38 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.550×** | -5.9 | 1e-06 | 19/41 (A-427, RKO, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.557×** | -5.7 | 2e-06 | 17/38 (NCI-H23, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.854× | -5.4 | 1e-05 | 21/42 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.581×** | -5.3 | 1e-05 | 13/39 (A-427, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.656×** | -4.1 | 0.003 | 14/42 (A-172, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~13% here); composition shift |
| [[Ciclopirox (drug)]] 5 µM |  | **0.757×** | -3.8 | 0.010 | 8/37 (AsPC-1, PANC-1, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.687×** | -3.7 | 0.017 | 12/23 (A-172, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.714×** | -3.3 | 0.061 | 11/34 (CFPAC-1, Hs 766T, …) | rises with dose | cell-cycle shift (explains ~10% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.15 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2939. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A-172 (line)]] | wt | 7.45 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.150× (z -11.4) |
| [[A-427 (line)]] | wt | 12.4 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.124× (z -10.9) |
| [[LoVo (line)]] | wt | 5.38 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.122× (z -9.5) |
| [[SW480 (line)]] | alt | 4.21 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.40× (z +9.2) | [[Belinostat (drug)]] 5 µM 0.178× (z -9.2) |
| [[NCI-H23 (line)]] | alt | 4.59 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0431× (z -11.1) |
| [[A498 (line)]] | wt | 7.83 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 4.47 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.88 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.57 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.03 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.54 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.521 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.21 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.02 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.17 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.80 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.73 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.09 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.590 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 4.29 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 0.321 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.882 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 0.312 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 2.63 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.844 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 1.40 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 3.51 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.62 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 4.08 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.74 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.77 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.90 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 3.33 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 2.09 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 5.54 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.886 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.76 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.373 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 1.51 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.11 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 3.61 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2939), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 13 of them with an alert (⚠; 13 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GCNT4]] | +0.71 | +0.56 / +0.41 | both halves | 4e-05 |  |
| [[POU6F1]] | +0.70 | +0.48 / +0.57 | both halves | 2e-05 |  |
| [[PRDM11]] | +0.69 | +0.61 / +0.35 | both halves | 1e-04 |  |
| [[ANKRD18B]] | +0.68 | +0.59 / +0.34 | both halves | 1e-04 |  |
| [[PJVK]] | +0.64 | +0.53 / +0.38 | both halves | 6e-05 |  |
| [[PIGW]] | +0.64 | +0.41 / +0.51 | both halves | 4e-05 |  |
| [[KRT8P12]] | +0.64 | +0.58 / +0.46 | both halves | 2e-05 |  |
| [[CFAP54]] | +0.63 | +0.60 / +0.30 | both halves | 2e-04 |  |
| [[SUMO2P17]] | +0.63 | +0.43 / +0.48 | both halves | 3e-05 |  |
| [[CCDC73]] | +0.63 | +0.43 / +0.47 | both halves | 3e-05 |  |
| [[EIF5]] | +0.63 | +0.51 / +0.30 | both halves | 2e-04 |  |
| [[MYLK4]] | +0.63 | +0.43 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFT172]] | -0.70 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[ALAD]] | -0.64 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[GUSBP18]] | -0.60 | -0.55 / -0.23 | both halves | 5e-04 |  |
| [[ARL3]] | -0.59 | -0.52 / -0.25 | both halves | 4e-04 |  |
| [[RALGAPA2]] | -0.59 | -0.51 / -0.26 | both halves | 4e-04 |  |
| [[PIN1]] | -0.59 | -0.33 / -0.35 | both halves | 1e-04 |  |
| [[CABIN1]] | -0.58 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[GUSBP1]] | -0.58 | -0.50 / -0.32 | both halves | 2e-04 |  |
| [[PJA2]] | -0.58 | -0.58 / -0.27 | both halves | 3e-04 |  |
| [[TMEM256]] | -0.57 | -0.54 / -0.19 | ⚠ one half (not replicated) | 8e-04 |  |
| [[EFHC1]] | -0.56 | -0.45 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MSI1]] | B | MSI1 activity raises WNT3's level | lines that do not express MSI1 (26) vs lines expressing it (24) | 1.59× lower at baseline in the lines without MSI1 | 0.034 | ⚠ within organs, on part of the lines; also absent: KCNQ2, KIF1A, LMX1B |
| [[MRAS]] | B | MRAS activity raises WNT3's level | lines that do not express MRAS (11) vs lines expressing it (39) | 1.66× lower at baseline in the lines without MRAS | 0.044 | ⚠ within organs, on part of the lines; also absent: RAB6B, ZNF618, DZIP1L |
| [[STOX1]] | B | STOX1 activity raises WNT3's level | lines that do not express STOX1 (9) vs lines expressing it (41) | 1.80× lower at baseline in the lines without STOX1 | 0.070 | ⚠ within organs, on part of the lines; also absent: CACNA2D2, RIMS3, VASH2; maybe low, not absent |
| [[HDAC6]] | B | HDAC6 activity raises WNT3's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.4% of all compounds | 0.071 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PLEKHA6]] | B | PLEKHA6 activity raises WNT3's level | lines that do not express PLEKHA6 (16) vs lines expressing it (34) | 1.01× lower at baseline in the lines without PLEKHA6 | 0.082 | ⚠ within organs, on part of the lines; also absent: KCNK1, ELF3, TNK1; maybe low, not absent |
| [[NKAIN1]] | C | NKAIN1 activity raises WNT3's level | lines that do not express NKAIN1 (4) vs lines expressing it (46) | 2.15× lower at baseline in the lines without NKAIN1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; co-absent genes; co-occurs with CTNNB1; also absent: TPST1, CPLANE1, SOAT1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SUMO2P17]] | B | WNT3 activity raises SUMO2P17's level | lines that do not express WNT3 (5) vs lines expressing it (45) | 1.40× lower at baseline in the lines without WNT3 | 0.073 | ⚠ within organs, on part of the lines; also absent: KIF3C, TBKBP1, PIK3CD; its own permutation p |

## Where it sits

- **Module**: [[Module 035]]; 137 genes; this gene is in the **+** arm (projection on the module's main direction 0.625). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-5.3, 9.4); signed map (23.8, -26.6). **Vector** length 55.8, 8.36% of its response variance represented; |z| ≥ 3 in 990 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +16.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.5 | +10.7 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.5 | +9.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +4.5 | +7.2 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.0 | +6.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +3.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.3 | +5.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +1.1 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.5 | +1.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.4 | +2.9 |
| fall | [[Belinostat (drug)]] 5 µM |  | -2.9 | -5.7 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.7 | -9.0 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.4 | -5.9 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -2.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -1.5 | -4.1 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | -1.3 | -2.7 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.3 | -1.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.3 | -0.8 |
|  | [[Cloxacillin (sodium) (drug)]] 0.05 µM |  | -1.0 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | Wnt family member 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q21.31-q21.32 — chr17:46,762,506-46,833,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC131950, MGC138321, MGC138323; previously INT4 |
| Gene groups (HGNC) | Wnt family |
| Reactome | 6 pathways, smallest: WNT ligand biogenesis and trafficking; Class B/2 (Secretin family receptors); GPCR ligand binding |
| Matched by | ensembl_id |

**Function**, from UniProt [P56703](https://www.uniprot.org/uniprotkb/P56703) (Proto-oncogene Wnt-3):

> Ligand for members of the frizzled family of seven transmembrane receptors (Probable). Functions in the canonical Wnt signaling pathway that results in activation of transcription factors of the TCF/LEF family. Required for normal gastrulation, formation of the primitive streak, and for the formation of the mesoderm during early embryogenesis. Required for normal formation of the apical ectodermal ridge (By similarity). Required for normal embryonic development, and especially for limb …

**Summary**, from NCBI Gene [7473](https://www.ncbi.nlm.nih.gov/gene/7473):

> The WNT gene family consists of structurally related genes which encode secreted signaling proteins. These proteins have been implicated in oncogenesis and in several developmental processes, including regulation of cell fate and patterning during embryogenesis. This gene is a member of the WNT gene family. It encodes a protein which shows 98% amino acid identity to mouse Wnt3 protein, and 84% to human WNT3A protein, another WNT gene product. The mouse studies show the requirement of Wnt3 in …

**Accessions** — [HGNC:12782](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12782) · Entrez [7473](https://www.ncbi.nlm.nih.gov/gene/7473) · UniProt [P56703](https://www.uniprot.org/uniprotkb/P56703) · Ensembl [ENSG00000108379](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000108379)

## Data

Gene col 2939: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2939); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2939, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2939]; `tensor/DDL_lfc|DDL_z.npy` [2939]; `embed/gene_vectors.npy` [2939]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2939 or target_col == 2939). Every well: [[WNT3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/WNT3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
