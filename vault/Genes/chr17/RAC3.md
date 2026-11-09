---
symbol: "RAC3"
type: "gene"
col: 9849
ensembl_id: "ENSG00000169750"
name: "Rac family small GTPase 3"
location: "17q25.3"
module: 58
arm: "+"
pooled_cpm: 5.41
n_lines_expressing: 43
n_dd_up: 5
n_dd_down: 10
n_dd_up_clean: 1
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 4
tags: ["gene", "module/058"]
generated_by: "tahoemap"
---

# RAC3

*Rac family small GTPase 3* — 17q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 5 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.07× (z +7.9, q 1e-12, up in 18 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Arbutin (drug)]] 5 µM: 1.71× (z +3.6, q 0.033, up in 15 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.355× (z -10.0, q 8e-21, down in 31 of 36 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 6 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NME3]] (+0.69, fdr 7e-06), [[DUSP23]] (+0.69, fdr 2e-05), [[SPATC1L]] (+0.68, fdr 4e-05); moves opposite to [[TUG1]] (-0.68, fdr 1e-05), [[ZNF655]] (-0.66, fdr 5e-05), [[ELK4]] (-0.64, fdr 4e-05).
> It is in [[Module 058]], a single-armed module (oxidative phosphorylation).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CAMKK1]] → it (grade C ⚠); 4 go from it, the strongest it → [[PAFAH1B3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 4 with an alert ⚠. 5 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9849.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.07×** | +7.9 | 1e-12 | 18/21 (NCI-H460, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.40×** | +5.7 | 3e-06 | 11/12 (SW480, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.17×** | +5.2 | 3e-05 | 6/8 (NCI-H2347, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~15% here); composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **2.09×** | +5.2 | 3e-05 | 16/26 (PANC-1, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~21% here) |
| [[Arbutin (drug)]] 5 µM |  | **1.71×** | +3.6 | 0.033 | 15/37 (HepG2/C3A, A498, …) | top dose only | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, none with an alert. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 9849.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.355×** | -10.0 | 8e-21 | 31/36 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.272×** | -9.2 | 7e-18 | 25/31 (LOX-IMVI, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.486×** | -5.1 | 5e-05 | 28/39 (HOP62, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **0.526×** | -4.6 | 7e-04 | 22/39 (LOX-IMVI, CHP-212, …) | two highest doses | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.509×** | -4.5 | 7e-04 | 21/38 (LOX-IMVI, BT-474, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.568×** | -4.0 | 0.005 | 18/38 (HS-578T, RPMI-7951, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.573×** | -4.0 | 0.005 | 16/40 (C32, BT-474, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.310×** | -4.0 | 0.005 | 13/33 (RKO, NCI-H460, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.673×** | -3.7 | 0.014 | 19/40 (C-33 A, MIA PaCa-2, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.615×** | -3.5 | 0.030 | 16/39 (BT-474, C32, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 0.640× | -3.1 | 0.10 | 13/31 (PANC-1, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Diphenhydramine (drug)]] 0.05 µM |  | 0.631× | -3.0 | 0.10 | 10/40 (PANC-1, A549, …) | inconsistent across doses |  |
| [[Erlotinib (drug)]] 0.05 µM |  | 0.633× | -3.0 | 0.10 | 10/39 (HEC-1-A, RPMI-7951, …) | inconsistent across doses | position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | 0.412× | -3.0 | 0.10 | 12/38 (RKO, HEC-1-A, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.03 per unit of S-phase module lfc, +0.34 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9849. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HT-29 (line)]] | alt | 3.75 | 0 | 3 | — | [[Temsirolimus (drug)]] 0.5 µM 0.0524× (z -9.7) |
| [[RKO (line)]] | wt | 16.0 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -11.8) |
| [[LOX-IMVI (line)]] | wt | 10.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0301× (z -14.0) |
| [[NCI-H2030 (line)]] | alt | 4.09 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.107× (z -10.9) |
| [[PANC-1 (line)]] | alt | 12.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.171× (z -10.3) |
| [[BT-474 (line)]] | alt | 10.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -9.1) |
| [[C-33 A (line)]] | alt | 10.3 | 0 | 1 | — | [[Imiquimod (maleate) (drug)]] 5 µM 0.0827× (z -8.6) |
| [[HepG2_C3A (line)]] | wt | 9.77 | 0 | 1 | — | [[Citalopram (hydrobromide) (drug)]] 0.5 µM 0.0774× (z -8.9) |
| [[HOP62 (line)]] | alt | 5.28 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 6.21 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -9.2) |
| [[SW480 (line)]] | alt | 4.65 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.194× (z -9.8) |
| [[A-172 (line)]] | wt | 1.59 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 8.01 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 11.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.90 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.64 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.24 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 7.67 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.22 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 3.49 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.14 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 1.85 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.92 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 8.58 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 4.00 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.02 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 2.60 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.88 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 2.50 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 7.28 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 2.92 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.05 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 5.70 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 9.24 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.59 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 2.28 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 5.91 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.16 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.691 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.54 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 2.27 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.48 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 3.20 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.00 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 7.11 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9849), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 6 of them with an alert (⚠; 3 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NME3]] | +0.69 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[DUSP23]] | +0.69 | +0.48 / +0.68 | both halves | 2e-05 |  |
| [[SPATC1L]] | +0.68 | +0.41 / +0.62 | both halves | 4e-05 |  |
| [[TMEM160]] | +0.67 | +0.46 / +0.65 | both halves | 3e-05 |  |
| [[MICOS13]] | +0.66 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[SLC66A2]] | +0.65 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[C15orf61]] ⚠ | +0.65 | +0.33 / +0.66 | both halves | 1e-04 | ⚠ in the vector space only through flagged drug-doses |
| [[TMEM256]] | +0.64 | +0.45 / +0.61 | both halves | 3e-05 |  |
| [[FAM13B]] | +0.63 | +0.51 / +0.41 | both halves | 4e-05 |  |
| [[ANTKMT]] | +0.63 | +0.38 / +0.56 | both halves | 7e-05 |  |
| [[MRPS34]] | +0.63 | +0.42 / +0.55 | both halves | 4e-05 |  |
| [[MHENCR]] | +0.63 | +0.53 / +0.61 | both halves | 1e-05 |  |
| [[CHCHD10]] | +0.63 | +0.49 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUG1]] | -0.68 | -0.49 / -0.62 | both halves | 1e-05 |  |
| [[ZNF655]] | -0.66 | -0.40 / -0.62 | both halves | 5e-05 |  |
| [[ELK4]] | -0.64 | -0.41 / -0.62 | both halves | 4e-05 |  |
| [[EIF4G2]] | -0.63 | -0.37 / -0.56 | both halves | 9e-05 |  |
| [[PRKAR1A]] | -0.62 | -0.30 / -0.58 | both halves | 2e-04 |  |
| [[PSME3IP1]] | -0.60 | -0.43 / -0.51 | both halves | 3e-05 |  |
| [[KRR1]] | -0.58 | -0.48 / -0.43 | both halves | 3e-05 |  |
| [[LINC01829]] | -0.58 | -0.43 / -0.35 | both halves | 1e-04 |  |
| [[LIG4]] | -0.56 | -0.53 / -0.32 | both halves | 2e-04 |  |
| [[ALG13]] | -0.56 | -0.29 / -0.49 | both halves | 2e-04 |  |
| [[SDCBP2-AS1]] | -0.55 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[DDX6]] | -0.55 | -0.32 / -0.38 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CAMKK1]] | C | CAMKK1 activity raises RAC3's level | lines that do not express CAMKK1 (4) vs lines expressing it (46) | 2.07× lower at baseline in the lines without CAMKK1 | 0.073 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: CKAP4, ADGRB2, POGLUT3; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PAFAH1B3]] | B | RAC3 activity raises PAFAH1B3's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.26× lower at baseline in the lines without RAC3 | 0.049 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |
| [[POLR2I]] | B | RAC3 activity raises POLR2I's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.32× lower at baseline in the lines without RAC3 | 0.052 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |
| [[CAMKK1]] | B | RAC3 activity raises CAMKK1's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.78× lower at baseline in the lines without RAC3 | 0.086 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |
| [[TSPYL1]] | B | RAC3 activity raises TSPYL1's level | lines that do not express RAC3 (7) vs lines expressing it (43) | 1.31× lower at baseline in the lines without RAC3 | 0.090 | ⚠ within organs, on part of the lines; also absent: FKBP10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 058]] — oxidative phosphorylation; 80 genes; every member is in the + arm (projection on the module's main direction 0.690). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.35; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-1.8, -3.3); signed map (-33.0, 5.6). **Vector** length 49.8, 8.42% of its response variance represented; |z| ≥ 3 in 673 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.2 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +2.3 | -1.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.2 | -1.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | +1.9 | +1.5 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +1.8 | -0.9 |
|  | [[Budesonide (drug)]] 0.05 µM |  | +1.5 | +2.1 |
|  | [[Betamethasone dipropionate (drug)]] 0.5 µM |  | +1.4 | +1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.3 | -1.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.3 | +0.6 |
|  | [[Clobetasol propionate (drug)]] 0.5 µM |  | +1.2 | +1.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -2.8 | -9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.7 | -3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.6 | -2.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | -2.6 | -4.6 |
|  | [[Auranofin (drug)]] 5 µM |  | -2.3 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.1 | -2.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -1.1 | -1.3 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.0 | -2.8 |

## What is on record

|  |  |
|---|---|
| Name | Rac family small GTPase 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 17q25.3 — chr17:82,031,678-82,034,204 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | Rho family GTPases; Receptor ligands |
| Reactome | 7 pathways, smallest: PCP/CE pathway; RAC3 GTPase cycle; Beta-catenin independent WNT signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P60763](https://www.uniprot.org/uniprotkb/P60763) (Ras-related C3 botulinum toxin substrate 3):

> Plasma membrane-associated small GTPase which cycles between an active GTP-bound and inactive GDP-bound state. In active state binds to a variety of effector proteins to regulate cellular responses, such as cell spreading and the formation of actin-based protusions including lamellipodia and membrane ruffles. Promotes cell adhesion and spreading on fibrinogen in a CIB1 and alpha-IIb/beta3 integrin-mediated manner.

**Summary**, from NCBI Gene [5881](https://www.ncbi.nlm.nih.gov/gene/5881):

> The protein encoded by this gene is a GTPase which belongs to the RAS superfamily of small GTP-binding proteins. Members of this superfamily appear to regulate a diverse array of cellular events, including the control of cell growth, cytoskeletal reorganization, and the activation of protein kinases. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Oct 2015]

**Accessions** — [HGNC:9803](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9803) · Entrez [5881](https://www.ncbi.nlm.nih.gov/gene/5881) · UniProt [P60763](https://www.uniprot.org/uniprotkb/P60763) · Ensembl [ENSG00000169750](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000169750)

## Data

Gene col 9849: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9849); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9849, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9849]; `tensor/DDL_lfc|DDL_z.npy` [9849]; `embed/gene_vectors.npy` [9849]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9849 or target_col == 9849). Every well: [[RAC3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/RAC3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
