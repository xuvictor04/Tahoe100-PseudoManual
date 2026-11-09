---
symbol: "FOXO6"
type: "gene"
col: 12808
ensembl_id: "ENSG00000204060"
name: "forkhead box O6"
location: "1p34.2"
module: 100
arm: "+"
pooled_cpm: 2.13
n_lines_expressing: 48
n_dd_up: 21
n_dd_down: 4
n_dd_up_clean: 17
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 8
direction_downstream: 0
tags: ["gene", "module/100"]
generated_by: "tahoemap"
---

# FOXO6

*forkhead box O6* — 1p34.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 21 drug-doses (4 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 6.05× (z +16.8, q 0e+00, up in 39 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Ribociclib (drug)]] 0.05 µM: 0.647× (z -4.1, q 0.014, down in 9 of 39 measured lines) ⚠ unreliable plate only; position not correctable. The strongest without an alert is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.648× (z -4.1, q 0.014, down in 12 of 41 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[USP2]] (+0.73, fdr 7e-06), [[AHDC1]] (+0.73, fdr 1e-05), [[DNAAF3]] (+0.68, fdr 1e-05); moves opposite to [[ENOX2]] (-0.70, fdr 1e-05), [[GPATCH2]] (-0.65, fdr 7e-05), [[DPH5-DT]] (-0.65, fdr 8e-05).
> It is in [[Module 100]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 8 arrows point to it, the strongest [[MAN1C1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 21 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 21 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12808.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **6.05×** | +16.8 | 0e+00 | 39/42 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.38×** | +15.7 | 0e+00 | 37/39 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **5.09×** | +15.2 | 0e+00 | 37/40 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **3.33×** | +11.2 | 6e-27 | 35/41 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **2.05×** | +9.5 | 3e-19 | 26/40 (SNU-423, PANC-1, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.86×** | +8.2 | 3e-14 | 14/30 (A-172, CFPAC-1, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Belinostat (drug)]] 0.5 µM |  | **2.18×** | +7.3 | 3e-11 | 15/27 (PANC-1, J82, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.94×** | +6.2 | 5e-08 | 17/37 (HEC-1-A, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Brivudine (drug)]] 5 µM |  | **3.39×** | +5.9 | 2e-07 | 12/38 (PANC-1, J82, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.90×** | +5.7 | 5e-07 | 0/0 | inconsistent across doses | cell-cycle shift (explains ~7% here); composition shift |
| [[Cytarabine (drug)]] 5 µM |  | **1.55×** | +3.9 | 0.005 | 5/34 (LoVo, PANC-1, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.40×** | +3.6 | 0.012 | 4/38 (SW480, A-427, …) | all doses, flat | noisy plate (z scaled); position effect removed |
| [[Glycyrrhizic acid (drug)]] 0.05 µM |  | **1.48×** | +3.2 | 0.053 | 3/22 (HT-29, HS-578T, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.28×** | +3.2 | 0.053 | 5/40 (SK-MEL-2, Hs 766T, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.43×** | +3.2 | 0.053 | 1/8 (SW480) | inconsistent across doses | cell-cycle shift (explains ~21% here); position effect removed |
| [[Binimetinib (drug)]] 5 µM |  | **1.40×** | +3.2 | 0.053 | 2/45 (A-427, SW480) | rises with dose | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.2 | 0.053 | 5/36 (SW 900, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12808.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.647×** | -4.1 | 0.014 | 9/39 (LS 180, SK-MEL-2, …) | inconsistent across doses |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.648×** | -4.1 | 0.014 | 12/41 (A-172, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.656×** | -3.9 | 0.015 | 13/35 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~1% here); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.662×** | -3.9 | 0.015 | 12/38 (A-172, H4, …) | two highest doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | 0.704× | -3.1 | 0.22 | 6/34 (CFPAC-1, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.16 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12808. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 2.68 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.0414× (z -8.7) ⚠ unreliable plate only |
| [[PANC-1 (line)]] | alt | 1.09 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 17.2× (z +8.5) | — |
| [[RKO (line)]] | wt | 3.94 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.0550× (z -9.3) |
| [[A-172 (line)]] | wt | 3.66 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 4.88 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.16 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.24 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.758 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.50 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 0.843 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 2.25 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.651 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.22 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 2.10 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 0.275 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.63 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 2.75 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 0.404 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.18 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.77 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.87 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 1.02 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.10 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 0.932 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 0.989 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 1.05 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 1.67 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 2.43 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.55 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 0.805 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 2.82 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.69 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.69 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 0.579 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 2.91 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.919 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.12 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 3.84 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.73 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 4.62 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12808), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*68 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[USP2]] | +0.73 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[AHDC1]] | +0.73 | +0.51 / +0.64 | both halves | 1e-05 |  |
| [[DNAAF3]] | +0.68 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[RAB3A]] | +0.68 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[CDON]] | +0.68 | +0.44 / +0.70 | both halves | 3e-05 |  |
| [[ATP1A3]] | +0.67 | +0.51 / +0.62 | both halves | 1e-05 |  |
| [[SLC29A4]] | +0.66 | +0.40 / +0.65 | both halves | 5e-05 |  |
| [[SMARCD3]] | +0.65 | +0.39 / +0.67 | both halves | 5e-05 |  |
| [[MPND]] | +0.65 | +0.60 / +0.40 | both halves | 5e-05 |  |
| [[NRTN]] | +0.65 | +0.58 / +0.64 | both halves | 7e-06 |  |
| [[SLC17A7]] | +0.65 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[CFD]] | +0.65 | +0.42 / +0.53 | both halves | 4e-05 |  |

## Genes that move opposite

*32 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ENOX2]] | -0.70 | -0.54 / -0.50 | both halves | 1e-05 |  |
| [[GPATCH2]] | -0.65 | -0.52 / -0.37 | both halves | 7e-05 |  |
| [[DPH5-DT]] | -0.65 | -0.37 / -0.45 | both halves | 8e-05 |  |
| [[ALG8]] | -0.64 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PRR14L]] | -0.63 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[AVEN]] | -0.62 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[CSTF3]] | -0.62 | -0.39 / -0.39 | both halves | 6e-05 |  |
| [[KRR1]] | -0.61 | -0.41 / -0.50 | both halves | 4e-05 |  |
| [[CDK12]] | -0.61 | -0.35 / -0.54 | both halves | 1e-04 |  |
| [[GABPB1-AS1]] | -0.60 | -0.34 / -0.37 | both halves | 1e-04 |  |
| [[EPM2A]] | -0.60 | -0.42 / -0.32 | both halves | 2e-04 |  |
| [[IREB2]] | -0.60 | -0.51 / -0.47 | both halves | 2e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*8 arrows, 8 of them with an alert ⚠; grade A 0, B 8, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MAN1C1]] | B | MAN1C1 activity raises FOXO6's level | lines that do not express MAN1C1 (11) vs lines expressing it (39) | 1.32× lower at baseline in the lines without MAN1C1 | 0.029 | ⚠ within organs, on part of the lines; also absent: DHRS2; maybe low, not absent |
| [[JAG2]] | B | JAG2 activity raises FOXO6's level | lines that do not express JAG2 (10) vs lines expressing it (40) | 1.50× lower at baseline in the lines without JAG2 | 0.030 | ⚠ within organs, on part of the lines; also absent: CRACD, RHPN1, PTP4A3; maybe low, not absent |
| [[SLC29A4]] | B | SLC29A4 activity raises FOXO6's level | lines that do not express SLC29A4 (6) vs lines expressing it (44) | 1.72× lower at baseline in the lines without SLC29A4 | 0.049 | ⚠ within organs, on part of the lines; also absent: DPF1, DNMT3B, CNTNAP1; maybe low, not absent |
| [[ADGRB2]] | B | ADGRB2 activity raises FOXO6's level | lines that do not express ADGRB2 (7) vs lines expressing it (43) | 1.64× lower at baseline in the lines without ADGRB2 | 0.074 | ⚠ within organs, on part of the lines; also absent: IRX5, CAMKK1, CNTNAP1 |
| [[EPHB3]] | B | EPHB3 activity raises FOXO6's level | lines that do not express EPHB3 (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without EPHB3 | 0.094 | ⚠ within organs, on part of the lines; also absent: SLC7A8, MCF2L, ENPP5; maybe low, not absent |
| [[KREMEN2]] | B | KREMEN2 activity raises FOXO6's level | lines that do not express KREMEN2 (13) vs lines expressing it (37) | 1.34× lower at baseline in the lines without KREMEN2 | 0.094 | ⚠ within organs, on part of the lines; also absent: SRRM3, KIF26A, ACHE; maybe low, not absent |
| [[MAP2K1]] | B | MAP2K1 activity lowers FOXO6's level | compounds that target MAP2K1: 3 of 4 raise it (Binimetinib, Cobimetinib, Trametinib) | 75% of the class's compounds vs 4.5% of all compounds | 0.095 | ⚠ off-target possible; 3 compounds |
| [[SEMA6B]] | B | SEMA6B activity raises FOXO6's level | lines that do not express SEMA6B (14) vs lines expressing it (36) | 1.16× lower at baseline in the lines without SEMA6B | 0.098 | ⚠ within organs, on part of the lines; also absent: FAM78B, BOLA3-DT, SLC4A3; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 100]]; 46 genes; every member is in the + arm (projection on the module's main direction 0.757). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (8.1, -3.4); signed map (-28.4, 21.0). **Vector** length 50.1, 6.79% of its response variance represented; |z| ≥ 3 in 1,030 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +4.1 | +9.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.1 | +6.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.9 | +16.8 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +2.9 | +15.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.7 | +5.7 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.6 | +5.9 |
|  | [[Radotinib (drug)]] 5 µM |  | +1.4 | +3.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +1.5 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.2 | +1.5 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.7 | +0.5 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -2.6 | -3.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.2 | -0.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.0 | -2.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -3.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -1.4 |
|  | [[GSK1059615 (drug)]] 5 µM |  | -1.2 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | forkhead box O6 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p34.2 — chr1:41,361,922-41,383,590 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Forkhead boxes |
| Reactome | 9 pathways, smallest: AKT phosphorylates targets in the nucleus; Regulation of localization of FOXO transcription factors; FOXO-mediated transcription of oxidative stress, metabolic and neuronal genes |
| Matched by | ensembl_id |

**Function**, from UniProt [A8MYZ6](https://www.uniprot.org/uniprotkb/A8MYZ6) (Forkhead box protein O6):

> Transcriptional activator.

**Summary**, from NCBI Gene [100132074](https://www.ncbi.nlm.nih.gov/gene/100132074):

> Predicted to enable DNA-binding transcription factor activity, RNA polymerase II-specific and RNA polymerase II cis-regulatory region sequence-specific DNA binding activity. Predicted to be involved in positive regulation of dendritic spine development and regulation of transcription by RNA polymerase II. Predicted to be located in chromatin and cytoplasm. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24814](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24814) · Entrez [100132074](https://www.ncbi.nlm.nih.gov/gene/100132074) · UniProt [A8MYZ6](https://www.uniprot.org/uniprotkb/A8MYZ6) · Ensembl [ENSG00000204060](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000204060)

## Data

Gene col 12808: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12808); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12808, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12808]; `tensor/DDL_lfc|DDL_z.npy` [12808]; `embed/gene_vectors.npy` [12808]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12808 or target_col == 12808). Every well: [[FOXO6 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FOXO6.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
