---
symbol: "HCG20"
type: "gene"
col: 13620
ensembl_id: "ENSG00000228022"
name: "HLA complex group 20"
location: "6p21"
module: 101
arm: "+"
pooled_cpm: 5.26
n_lines_expressing: 50
n_dd_up: 25
n_dd_down: 11
n_dd_up_clean: 17
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/101"]
generated_by: "tahoemap"
---

# HCG20

*HLA complex group 20* — 6p21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 25 drug-doses (8 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.35× (z +21.5, q 0e+00, up in 37 of 39 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.595× (z -5.4, q 5e-05, down in 20 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[DELEC1]] (+0.71, fdr 1e-05), [[NOP14-AS1]] (+0.70, fdr 7e-06), [[ITGA2-AS1]] (+0.69, fdr 2e-05); moves opposite to [[CAPN7]] (-0.58, fdr 6e-05), [[WRAP73]] (-0.54, fdr 3e-04), [[MRPS34]] (-0.53, fdr 2e-04).
> It is in [[Module 101]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[ZNF341-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 8 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 25 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13620.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.35×** | +21.5 | 0e+00 | 37/39 (HOP62, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.49×** | +11.9 | 2e-30 | 12/15 (HS-578T, SW48, …) | all doses, flat | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.93×** | +11.1 | 3e-26 | 17/28 (NCI-H460, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.76×** | +10.1 | 9e-22 | 5/10 (HS-578T, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~2% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.71×** | +7.9 | 4e-13 | 26/46 (SNU-423, HOP62, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.64×** | +7.2 | 6e-11 | 28/45 (HOP62, HS-578T, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.90×** | +6.6 | 3e-09 | 26/42 (HOP62, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.42×** | +5.2 | 2e-05 | 15/37 (AsPC-1, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.46×** | +4.9 | 7e-05 | 14/41 (SW48, C32, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[Auranofin (drug)]] 5 µM |  | **1.53×** | +4.4 | 6e-04 | 16/43 (AN3 CA, HEC-1-A, …) | top dose only |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.53×** | +4.2 | 0.001 | 14/41 (HOP62, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.48×** | +3.9 | 0.004 | 8/30 (SW1417, AsPC-1, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.43×** | +3.7 | 0.010 | 5/27 (HOP62, A498, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.42×** | +3.6 | 0.011 | 10/46 (PANC-1, CFPAC-1, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.05 µM |  | **1.45×** | +3.6 | 0.011 | 5/41 (PANC-1, Hs 766T, …) | inconsistent across doses | position effect removed |
| [[Tolcapone (drug)]] 0.5 µM |  | **1.41×** | +3.5 | 0.015 | 9/43 (NCI-H460, A498, …) | inconsistent across doses | position effect removed |
| [[Methylprednisolone succinate (drug)]] 0.5 µM |  | **1.56×** | +3.3 | 0.031 | 1/40 (SNU-423) | inconsistent across doses | low cells (technical?); noisy plate (z scaled); position effect removed |
| [[Omeprazole (sodium) (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.045 | 5/45 (NCI-H2030, RPMI-7951, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.086 | 12/37 (HS-578T, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | **1.33×** | +2.9 | 0.086 | 7/45 (NCI-H2030, SNU-423, …) | inconsistent across doses | low cells (technical?) |
| [[Infigratinib (drug)]] 0.05 µM |  | **1.35×** | +2.9 | 0.086 | 2/43 (MIA PaCa-2, Hs 766T) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 13620.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.595×** | -5.4 | 5e-05 | 20/46 (C32, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Radotinib (drug)]] 5 µM |  | **0.713×** | -4.9 | 2e-04 | 21/44 (LoVo, HS-578T, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.687×** | -4.5 | 0.001 | 13/44 (NCI-H23, NCI-H2030, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Ponatinib (drug)]] 5 µM |  | **0.669×** | -4.1 | 0.005 | 15/46 (NCI-H2030, LoVo, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **0.751×** | -4.1 | 0.005 | 12/45 (SW480, NCI-H1573, …) | all doses, flat | position effect removed |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.743×** | -3.9 | 0.009 | 11/44 (SW480, NCI-H1573, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (drug)]] 5 µM |  | **0.716×** | -3.5 | 0.039 | 11/46 (SW480, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **0.759×** | -3.3 | 0.054 | 12/46 (CFPAC-1, SW480, …) | two highest doses | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | **0.706×** | -3.3 | 0.054 | 10/46 (SW480, CHP-212, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.725×** | -3.3 | 0.054 | 11/42 (SNU-423, AN3 CA, …) | two highest doses |  |
| [[Medroxyprogesterone acetate (drug)]] 5 µM |  | **0.801×** | -3.2 | 0.063 | 10/44 (NCI-H1573, A-172, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13620. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 4.65 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.02× (z +10.5) | — |
| [[CFPAC-1 (line)]] | alt | 4.67 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.43× (z +9.8) | [[Thymol (drug)]] 0.5 µM 0.0952× (z -8.6) |
| [[A498 (line)]] | wt | 1.98 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.34× (z +8.7) | — |
| [[HOP62 (line)]] | alt | 4.94 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.8× (z +14.3) | — |
| [[LoVo (line)]] | wt | 7.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.92× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 3.58 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.34× (z +9.0) | — |
| [[LS 180 (line)]] | wt | 5.72 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.05 µM 0.0760× (z -8.9) |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.597× (z -9.3) ⚠ position not correctable |
| [[NCI-H460 (line)]] | wt | 3.63 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.76× (z +8.5) | — |
| [[NCI-H661 (line)]] | alt | 1.75 | 1 | 0 | [[Filgotinib (drug)]] 5 µM 2.18× (z +33.6) | — |
| [[PANC-1 (line)]] | alt | 3.33 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.82× (z +8.6) | — |
| [[SK-MEL-2 (line)]] | alt | 8.40 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +8.6) | — |
| [[A-172 (line)]] | wt | 2.29 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 1.81 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 2.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 1.72 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.19 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.74 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 2.83 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.40 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.95 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 8.16 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.34 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.71 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 4.95 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.98 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.56 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.15 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.79 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.87 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.81 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 2.33 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.89 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.57 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.73 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.64 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 7.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13620), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[DELEC1]] | +0.71 | +0.53 / +0.68 | both halves | 1e-05 | same gene group |
| [[NOP14-AS1]] | +0.70 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[ITGA2-AS1]] | +0.69 | +0.47 / +0.69 | both halves | 2e-05 |  |
| [[RALY-AS1]] | +0.68 | +0.50 / +0.56 | both halves | 1e-05 |  |
| [[BHLHE40-AS1]] | +0.67 | +0.46 / +0.61 | both halves | 2e-05 |  |
| [[LIF]] | +0.66 | +0.66 / +0.67 | both halves | 7e-06 |  |
| [[KDM7A-DT]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 |  |
| [[LINC00243]] | +0.65 | +0.58 / +0.67 | both halves | 7e-06 | ⚠ same locus (6.0 kb: neighbours can correlate without regulation) |
| [[UBE2R2-AS1]] | +0.65 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[CCDC26]] | +0.64 | +0.37 / +0.59 | both halves | 8e-05 | same gene group |
| [[LPXN]] | +0.63 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[FEZ1]] | +0.62 | +0.35 / +0.57 | both halves | 1e-04 |  |
| [[LETM2]] | +0.62 | +0.45 / +0.55 | both halves | 3e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CAPN7]] | -0.58 | -0.39 / -0.55 | both halves | 6e-05 |  |
| [[WRAP73]] | -0.54 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[MRPS34]] | -0.53 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[PPP1R12B]] | -0.53 | -0.51 / -0.37 | both halves | 8e-05 |  |
| [[ZYG11B]] | -0.53 | -0.38 / -0.47 | both halves | 7e-05 |  |
| [[RHOT1]] | -0.53 | -0.37 / -0.49 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ZNF341-AS1]] | B | ZNF341-AS1 activity raises HCG20's level | lines that do not express ZNF341-AS1 (7) vs lines expressing it (43) | 1.56× lower at baseline in the lines without ZNF341-AS1 | 0.049 | ⚠ within organs, on part of the lines; also absent: ABTB2, CD59, CLCF1; maybe low, not absent |
| [[IER3]] | B | IER3 activity raises HCG20's level | lines that do not express IER3 (5) vs lines expressing it (45) | 2.14× lower at baseline in the lines without IER3 | 0.062 | ⚠ within organs, on part of the lines; also absent: ARHGAP18, SLC2A1, SHB |
| [[MAP2K2]] | B | MAP2K2 activity raises HCG20's level | compounds that target MAP2K2: 2 of 2 lower it (Binimetinib, Trametinib) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 101]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.684). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.8, -3.8); signed map (3.8, 31.6). **Vector** length 78.2, 14.4% of its response variance represented; |z| ≥ 3 in 953 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.2 | +21.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.0 | +7.2 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +11.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.6 | +6.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +5.1 | +11.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +7.9 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.9 | +4.4 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +2.0 | +0.9 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.8 | +2.5 |
| fall | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -3.2 | -2.3 |
|  | [[Radotinib (drug)]] 5 µM |  | -3.1 | -4.9 |
|  | [[Belinostat (drug)]] 5 µM |  | -2.4 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -2.3 | -2.9 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -3.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -2.0 | -4.5 |

## What is on record

|  |  |
|---|---|
| Name | HLA complex group 20 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 6p21 — chr6:30,743,790-30,792,250 (+) |
| Ensembl biotype | lncRNA |
| Also known as | AB023051.1, NCRNA00149 |
| Gene groups (HGNC) | Long non-coding RNAs with non-systematic symbols |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:31334](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:31334) · Entrez [105375013](https://www.ncbi.nlm.nih.gov/gene/105375013) · Ensembl [ENSG00000228022](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000228022)

## Data

Gene col 13620: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13620); `tables/drug_effects.parquet` (36 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13620, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13620]; `tensor/DDL_lfc|DDL_z.npy` [13620]; `embed/gene_vectors.npy` [13620]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13620 or target_col == 13620). Every well: [[HCG20 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HCG20.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
