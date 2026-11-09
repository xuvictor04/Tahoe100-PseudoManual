---
symbol: "ARHGEF19"
type: "gene"
col: 6639
ensembl_id: "ENSG00000142632"
name: "Rho guanine nucleotide exchange factor 19"
location: "1p36.13"
module: 2
arm: "+"
pooled_cpm: 3.66
n_lines_expressing: 47
n_dd_up: 4
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 3
tags: ["gene", "module/002"]
generated_by: "tahoemap"
---

# ARHGEF19

*Rho guanine nucleotide exchange factor 19* — 1p36.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (2 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 1.85× (z +6.3, q 2e-07, up in 0 of 8 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Clobetasol propionate (drug)]] 0.5 µM: 1.46× (z +4.0, q 0.010, up in 10 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.574× (z -8.4, q 2e-14, down in 21 of 32 measured lines) ⚠ cell-cycle shift, explains ~34% of this change. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.469× (z -8.1, q 1e-13, down in 25 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGEF1]] (+0.56, fdr 3e-05), [[MIER2]] (+0.54, fdr 4e-05), [[SIPA1]] (+0.53, fdr 2e-05); moves opposite to [[LEPROT]] (-0.48, fdr 1e-04), [[ZBTB20]] (-0.44, fdr 7e-05), [[ATP6V1C1]] (-0.44, fdr 9e-05).
> It sits in the **+** arm of [[Module 002]].
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[PXYLP1]] → it (grade C ⚠); 3 go from it, the strongest it → [[OSBPL5]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6639.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.85×** | +6.3 | 2e-07 | 0/8 | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.61×** | +5.1 | 1e-04 | 8/20 (AsPC-1, NCI-H460, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **1.46×** | +4.0 | 0.010 | 10/33 (NCI-H1792, SNU-423, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 0.5 µM |  | **1.39×** | +3.5 | 0.071 | 9/27 (PANC-1, HT-29, …) | two highest doses | position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | 1.54× | +3.3 | 0.11 | 4/18 (NCI-H2030, NCI-H460, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 1.39× | +3.2 | 0.11 | 0/9 | all doses, stronger at high dose | cell-cycle shift (explains ~15% here); composition shift |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 1.35× | +3.2 | 0.11 | 3/42 (HS-578T, NCI-H460, …) | inconsistent across doses |  |
| [[Hydroxyurea (drug)]] 0.05 µM |  | 1.38× | +3.1 | 0.12 | 4/28 (KATO III, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | 1.35× | +3.0 | 0.15 | 4/20 (SW480, NCI-H1792, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 2 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6639.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.574×** | -8.4 | 2e-14 | 21/32 (AsPC-1, A498, …) | inconsistent across doses | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.469×** | -8.1 | 1e-13 | 25/42 (PANC-1, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.498×** | -7.2 | 1e-10 | 20/36 (HS-578T, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.531×** | -6.8 | 2e-09 | 22/38 (NCI-H460, NCI-H1792, …) | two highest doses | cell-cycle shift (explains ~5% here); position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **0.385×** | -5.4 | 1e-05 | 12/36 (AsPC-1, MIA PaCa-2, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.636×** | -4.9 | 1e-04 | 15/27 (AsPC-1, NCI-H2030, …) | two highest doses | cell-cycle shift (explains ~10% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.718×** | -3.6 | 0.029 | 11/35 (NCI-H2347, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.730×** | -3.4 | 0.049 | 15/37 (HS-578T, SK-MEL-2, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.738×** | -3.3 | 0.063 | 5/41 (HS-578T, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.738×** | -3.3 | 0.063 | 10/42 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here) |
| [[Adenine (drug)]] 0.5 µM |  | 0.756× | -3.0 | 0.13 | 6/38 (NCI-H460, NCI-H2347, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.35 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6639. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[AsPC-1 (line)]] | alt | 15.1 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.7) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A498 (line)]] | wt | 5.75 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -11.6) ⚠ cell-cycle shift, explains ~34% of this change |
| [[NCI-H2030 (line)]] | alt | 3.60 | 0 | 2 (1 ⚠) | — | [[Belinostat (drug)]] 0.5 µM 0.0737× (z -10.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Quinidine (15% dihydroquinidine) (drug)]] 5 µM 0.0901× (z -8.8) |
| [[HS-578T (line)]] | alt | 6.58 | 0 | 1 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0698× (z -10.8) ⚠ cell-cycle shift, explains ~0% of this change |
| [[LoVo (line)]] | wt | 2.70 | 0 | 1 | — | [[Benproperine (phosphate) (drug)]] 0.05 µM 0.0498× (z -9.8) |
| [[NCI-H23 (line)]] | alt | 9.33 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -9.0) ⚠ cell-cycle shift, explains ~34% of this change |
| [[A-172 (line)]] | wt | 0.777 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 3.98 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 2.21 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 1.26 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 0.717 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.735 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 3.50 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 0.957 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.21 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.23 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.44 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 6.35 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.53 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 2.94 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.67 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 4.07 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.95 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.67 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 3.90 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 3.08 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.84 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 2.99 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 4.74 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 1.24 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 3.29 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.71 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.36 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 3.42 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.28 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.82 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 3.38 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.55 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.12 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6639), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*88 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGEF1]] | +0.56 | +0.59 / +0.46 | both halves | 3e-05 | same gene group; pathway: Cell death signalling via NRAGE, NRIF and NADE; STRING 496 |
| [[MIER2]] | +0.54 | +0.51 / +0.40 | both halves | 4e-05 |  |
| [[SIPA1]] | +0.53 | +0.52 / +0.47 | both halves | 2e-05 |  |
| [[RAPGEF3]] | +0.52 | +0.53 / +0.39 | both halves | 5e-05 |  |
| [[MFSD2A]] | +0.52 | +0.47 / +0.49 | both halves | 2e-05 |  |
| [[APBB3]] | +0.52 | +0.45 / +0.42 | both halves | 4e-05 |  |
| [[GPSM1]] | +0.51 | +0.56 / +0.37 | both halves | 8e-05 |  |
| [[MSTO2P]] | +0.51 | +0.48 / +0.43 | both halves | 3e-05 |  |
| [[AP1M1]] | +0.51 | +0.55 / +0.40 | both halves | 5e-05 |  |
| [[SLC46A1]] | +0.50 | +0.45 / +0.45 | both halves | 3e-05 |  |
| [[TRIM3]] | +0.50 | +0.48 / +0.45 | both halves | 3e-05 |  |
| [[PLA2G4B]] | +0.50 | +0.47 / +0.40 | both halves | 5e-05 |  |

## Genes that move opposite

*12 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEPROT]] | -0.48 | -0.33 / -0.51 | both halves | 1e-04 |  |
| [[ZBTB20]] | -0.44 | -0.38 / -0.42 | both halves | 7e-05 |  |
| [[ATP6V1C1]] | -0.44 | -0.45 / -0.37 | both halves | 9e-05 |  |
| [[GULP1]] | -0.44 | -0.37 / -0.44 | both halves | 8e-05 |  |
| [[GMDS-DT]] | -0.43 | -0.43 / -0.31 | both halves | 2e-04 |  |
| [[PTPRK]] | -0.42 | -0.34 / -0.44 | both halves | 1e-04 |  |
| [[UBL3]] | -0.42 | -0.28 / -0.44 | both halves | 3e-04 |  |
| [[C11orf58]] | -0.42 | -0.30 / -0.44 | both halves | 2e-04 |  |
| [[MTUS1-DT]] | -0.42 | -0.39 / -0.31 | both halves | 2e-04 |  |
| [[PSENEN]] | -0.42 | -0.36 / -0.36 | both halves | 1e-04 | pathway: Cell death signalling via NRAGE, NRIF and NADE |
| [[KTN1]] | -0.41 | -0.42 / -0.50 | both halves | 4e-05 | pathway: CDC42 GTPase cycle |
| [[DST]] | -0.41 | -0.36 / -0.47 | both halves | 1e-04 | same gene group |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PXYLP1]] | C | PXYLP1 activity lowers ARHGEF19's level | lines that do not express PXYLP1 (3) vs lines expressing it (47) | 2.26× higher at baseline in the lines without PXYLP1 | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: PDE4C, ZFHX2, PDE5A; maybe low, not absent |

### Downstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 0, C 3.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OSBPL5]] | C | ARHGEF19 activity strengthens OSBPL5's drug response | lines that do not express ARHGEF19 (3) vs lines expressing it (43) | the lines without ARHGEF19 respond 0.33× as strongly (z diff +3.78); strongest at Homoharringtonine 5 µM: 1.21x vs 0.41x (z diff +9.2) | 0.064 | ⚠ few lines (3 vs 47); across organs; also absent: SLC35F2, ENSG00000274213; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[KLHL17]] | C | ARHGEF19 activity weakens KLHL17's drug response | lines that do not express ARHGEF19 (3) vs lines expressing it (43) | the lines without ARHGEF19 respond 1.31× as strongly (z diff -0.38); strongest at Harringtonine 0.5 µM: 0.24x vs 0.55x (z diff -2.4) | 0.088 | ⚠ few lines (3 vs 47); across organs; also absent: SLC35F2, ENSG00000274213; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[FOXRED1]] | C | ARHGEF19 activity raises FOXRED1's level | lines that do not express ARHGEF19 (3) vs lines expressing it (47) | 1.94× lower at baseline in the lines without ARHGEF19 | 0.089 | ⚠ few lines (3 vs 47); across organs; also absent: SLC35F2, ENSG00000274213; maybe low, not absent |

## Where it sits

- **Module**: [[Module 002]]; 248 genes; this gene is in the **+** arm (projection on the module's main direction 0.450). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.21).
- **Nodal map** (x, y) = (-2.8, -26.1); signed map (-49.3, 20.3). **Vector** length 49.4, 6.34% of its response variance represented; |z| ≥ 3 in 965 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | +2.0 | +5.1 |
|  | [[LY-2584702 (tosylate salt) (drug)]] 5 µM | ⚠ toxic | +1.8 | +2.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~45% of this change | +1.7 | +3.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +1.6 | -0.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | +2.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.4 | +2.6 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.4 | +2.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | +1.2 | +3.5 |
|  | [[Budesonide (drug)]] 5 µM |  | +1.1 | +1.7 |
| fall | [[Ouabain (Octahydrate) (drug)]] 5 µM |  | -2.8 | -8.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.1 | -7.2 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -1.8 | -3.6 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift | -1.6 | -2.1 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -1.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.2 | -0.6 |
|  | [[AZD-8055 (drug)]] 0.5 µM |  | -1.1 | -1.7 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -1.0 | -2.6 |
|  | [[Bimiralisib (drug)]] 5 µM |  | -1.0 | -2.1 |

## What is on record

|  |  |
|---|---|
| Name | Rho guanine nucleotide exchange factor 19 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.13 — chr1:16,197,854-16,212,652 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ33962, WGEF |
| Gene groups (HGNC) | Dbl family Rho GEFs; SH3 domain containing |
| Reactome | 13 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; Cell death signalling via NRAGE, NRIF and NADE |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IW93](https://www.uniprot.org/uniprotkb/Q8IW93) (Rho guanine nucleotide exchange factor 19):

> Acts as a guanine nucleotide exchange factor (GEF) for RhoA GTPase.

**Summary**, from NCBI Gene [128272](https://www.ncbi.nlm.nih.gov/gene/128272):

> Guanine nucleotide exchange factors (GEFs) such as ARHGEF19 accelerate the GTPase activity of Rho GTPases (see RHOA, MIM 165390).[supplied by OMIM, Dec 2008]

**Accessions** — [HGNC:26604](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26604) · Entrez [128272](https://www.ncbi.nlm.nih.gov/gene/128272) · UniProt [Q8IW93](https://www.uniprot.org/uniprotkb/Q8IW93) · Ensembl [ENSG00000142632](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142632)

## Data

Gene col 6639: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6639); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6639, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6639]; `tensor/DDL_lfc|DDL_z.npy` [6639]; `embed/gene_vectors.npy` [6639]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6639 or target_col == 6639). Every well: [[ARHGEF19 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ARHGEF19.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
