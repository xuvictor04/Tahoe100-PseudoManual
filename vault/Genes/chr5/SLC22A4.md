---
symbol: "SLC22A4"
type: "gene"
col: 12364
ensembl_id: "ENSG00000197208"
name: "solute carrier family 22 member 4"
location: "5q31.1"
module: 78
arm: "+"
pooled_cpm: 19.38
n_lines_expressing: 45
n_dd_up: 10
n_dd_down: 5
n_dd_up_clean: 3
n_dd_down_clean: 5
in_vector_space: true
direction_upstream: 4
direction_downstream: 1
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# SLC22A4

*solute carrier family 22 member 4* — 5q31.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.05 µM: 2.36× (z +11.8, q 4e-29, up in 23 of 28 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.46× (z +8.0, q 5e-13, up in 25 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 5 drug-doses (none with an alert); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.715× (z -5.0, q 4e-04, down in 15 of 42 measured lines).
> Its strongest partners by |cos| (86 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 14 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FMNL3]] (+0.47, fdr 8e-05), [[ARGLU1]] (+0.46, fdr 2e-04), [[ITGA1]] (+0.45, fdr 1e-04); moves opposite to [[KDM4A]] (-0.50, fdr 6e-05), [[RBBP5]] (-0.46, fdr 6e-05), [[ZYG11B]] (-0.43, fdr 3e-04).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[COL7A1]] → it (grade B ⚠); 1 goes from it, the strongest it → cells under [[Tomivosertib (drug)]] 5 µM (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 9 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12364.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.36×** | +11.8 | 4e-29 | 23/28 (HS-578T, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.46×** | +8.0 | 5e-13 | 25/41 (C32, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.65×** | +7.1 | 2e-10 | 14/35 (Panc 03.27, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.6 | 5e-09 | 20/42 (SK-MEL-2, NCI-H2347, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.57×** | +6.4 | 2e-08 | 11/26 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.54×** | +6.4 | 2e-08 | 13/31 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **1.45×** | +5.3 | 1e-05 | 14/39 (J82, PANC-1, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.75×** | +4.3 | 0.001 | 9/25 (HS-578T, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.29×** | +3.7 | 0.012 | 10/43 (SW480, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.26×** | +3.5 | 0.031 | 15/37 (SW480, HS-578T, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | 1.17× | +3.3 | 0.056 | 4/43 (Panc 03.27, NCI-H2030, …) | top dose only |  |
| [[Trifluridine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.16× | +3.1 | 0.10 | 7/42 (NCI-H460, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 1 with an alert ⚠. 5 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.715×** | -5.0 | 4e-04 | 15/42 (Hs 766T, CFPAC-1, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.754×** | -4.2 | 0.008 | 18/42 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~11% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.769×** | -3.9 | 0.017 | 18/43 (SNU-423, A549, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[NG25 (drug)]] 5 µM |  | **0.608×** | -3.8 | 0.017 | 15/37 (NCI-H1792, HS-578T, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.781×** | -3.6 | 0.030 | 16/43 (HOP62, A498, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.942× | -3.3 | 0.11 | 4/43 (HOP62, NCI-H1792, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, -0.12 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 99.5 | 0 | 4 (3 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0932× (z -18.0) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.123× (z -15.9) |
| [[A-172 (line)]] | wt | 45.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -12.8) ⚠ toxic; transcription drop |
| [[A498 (line)]] | wt | 50.2 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.172× (z -13.1) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.216× (z -11.4) |
| [[A549 (line)]] | wt | 34.8 | 0 | 2 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -11.9) |
| [[H4 (line)]] | wt | 25.2 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 6.10× (z +11.1) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[Hs 766T (line)]] | wt | 49.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.271× (z -8.5) ⚠ cell-cycle shift, explains ~26% of this change |
| [[HS-578T (line)]] | alt | 38.8 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.311× (z -8.7) ⚠ cell-cycle shift, explains ~26% of this change |
| [[J82 (line)]] | alt | 17.4 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 2.98× (z +8.8) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[LoVo (line)]] | wt | 15.7 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.74× (z +10.3) ⚠ toxic; transcription drop | — |
| [[RPMI-7951 (line)]] | alt | 50.6 | 0 | 1 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.233× (z -9.2) ⚠ cell-cycle shift, explains ~26% of this change |
| [[SHP-77 (line)]] | alt | 7.85 | 0 | 1 | — | [[Pimozide (drug)]] 0.05 µM 0.0692× (z -10.2) |
| [[A-427 (line)]] | wt | 8.74 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 6.18 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 4.47 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 5.29 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 5.91 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 27.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 4.85 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.26 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 3.46 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 12.0 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 35.0 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.26 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.96 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 4.29 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 8.11 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.53 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 29.6 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 9.10 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 9.82 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 23.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 5.85 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 15.1 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.62 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 33.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 51.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.50 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 8.93 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 13.3 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FMNL3]] | +0.47 | +0.46 / +0.37 | both halves | 8e-05 |  |
| [[ARGLU1]] | +0.46 | +0.31 / +0.44 | both halves | 2e-04 |  |
| [[ITGA1]] | +0.45 | +0.34 / +0.48 | both halves | 1e-04 |  |
| [[CEACAM16-AS1]] | +0.45 | +0.24 / +0.44 | both halves | 5e-04 |  |
| [[FAM81A]] | +0.45 | +0.26 / +0.43 | both halves | 4e-04 |  |
| [[ANKRD10]] | +0.44 | +0.31 / +0.48 | both halves | 2e-04 |  |
| [[BMP1]] | +0.44 | +0.40 / +0.45 | both halves | 5e-05 |  |
| [[CTC-338M12.4]] | +0.44 | +0.29 / +0.49 | both halves | 2e-04 |  |
| [[NIPBL-DT]] | +0.44 | +0.29 / +0.45 | both halves | 2e-04 |  |
| [[STMN3]] | +0.43 | +0.27 / +0.56 | both halves | 3e-04 |  |
| [[NBL1]] | +0.42 | +0.19 / +0.54 | ⚠ one half (not replicated) | 8e-04 |  |
| [[PICART1]] | +0.42 | +0.28 / +0.41 | both halves | 3e-04 |  |
| [[ATP13A3]] | +0.41 | +0.40 / +0.48 | both halves | 5e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[KDM4A]] | -0.50 | -0.38 / -0.48 | both halves | 6e-05 |  |
| [[RBBP5]] | -0.46 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[ZYG11B]] | -0.43 | -0.28 / -0.42 | both halves | 3e-04 |  |
| [[PARP2]] | -0.41 | -0.30 / -0.37 | both halves | 2e-04 |  |
| [[ZRANB1]] | -0.40 | -0.31 / -0.47 | both halves | 2e-04 |  |
| [[AQR]] | -0.40 | -0.43 / -0.22 | both halves | 6e-04 |  |
| [[SFSWAP]] | -0.40 | -0.27 / -0.43 | both halves | 3e-04 |  |
| [[WDR70]] | -0.39 | -0.26 / -0.38 | both halves | 3e-04 |  |
| [[RAB3GAP1]] | -0.39 | -0.28 / -0.38 | both halves | 3e-04 |  |
| [[PSMD10]] | -0.39 | -0.32 / -0.39 | both halves | 2e-04 |  |
| [[MAP2K5]] | -0.38 | -0.33 / -0.40 | both halves | 1e-04 |  |
| [[HAX1]] | -0.38 | -0.36 / -0.30 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL7A1]] | B | COL7A1 activity raises SLC22A4's level | lines that do not express COL7A1 (24) vs lines expressing it (26) | 2.75× lower at baseline in the lines without COL7A1 | 0.010 | ⚠ within organs, on part of the lines; also absent: DKK3, ABI3BP, COL5A1; maybe low, not absent |
| [[SHISAL1]] | B | SHISAL1 activity raises SLC22A4's level | lines that do not express SHISAL1 (30) vs lines expressing it (20) | 2.33× lower at baseline in the lines without SHISAL1 | 0.043 | ⚠ within organs, on part of the lines; also absent: ZMAT4, AK5, SOX11 |
| [[HTRA1]] | B | HTRA1 activity raises SLC22A4's level | lines that do not express HTRA1 (19) vs lines expressing it (31) | 1.94× lower at baseline in the lines without HTRA1 | 0.060 | ⚠ within organs, on part of the lines; also absent: NTF3, COL4A1, COL7A1 |
| [[SMOX]] | B | SMOX activity raises SLC22A4's level | lines that do not express SMOX (6) vs lines expressing it (44) | 2.25× lower at baseline in the lines without SMOX | 0.073 | ⚠ within organs, on part of the lines; also absent: NIBAN2, NDRG1, TRIM38; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| cells under [[Tomivosertib (drug)]] 5 µM | C | SLC22A4 activity raises the cells' numbers under Tomivosertib 5 µM (protects the cells) | lines that do not express SLC22A4 (5) vs lines expressing it (43) | the lines without SLC22A4: 0.79× the cells of the other lines | 0.040 | ⚠ tissue-confounded; across organs; also absent: TGFB1, ITGA7, CAVIN1; maybe low, not absent |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.220). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (31.4, -2.4); signed map (43.8, -11.4). **Vector** length 87.1, 18.1% of its response variance represented; |z| ≥ 3 in 872 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.2 | +8.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.1 | +11.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +3.1 | +6.6 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.8 | +2.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.8 | +6.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Benztropine (mesylate) (drug)]] 0.05 µM |  | +1.6 | +1.0 |
|  | [[Rapamycin (drug)]] 0.5 µM |  | +1.4 | +2.0 |
|  | [[Cabozantinib (S-malate) (drug)]] 5 µM |  | +1.4 | +1.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -3.2 | -5.0 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -3.1 | -3.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -2.9 | -2.3 |
|  | [[Panobinostat (drug)]] 5 µM |  | -2.8 | -3.9 |
|  | [[NG25 (drug)]] 5 µM |  | -2.7 | -3.8 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.4 | -2.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.7 | -2.9 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.6 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 22 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 5q31.1 — chr5:132,294,394-132,344,190 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OCTN1, MGC34546; previously DFNB60 |
| Gene groups (HGNC) | Solute carrier family 22 |
| Hallmark sets | HEME_METABOLISM |
| Reactome | 5 pathways, smallest: Choline catabolism; SLC-mediated transport of organic cations; SLC-mediated transmembrane transport |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H015](https://www.uniprot.org/uniprotkb/Q9H015) (Solute carrier family 22 member 4):

> Transporter that mediates the transport of endogenous and microbial zwitterions and organic cations. Functions as a Na(+)-dependent and pH-dependent high affinity microbial symporter of potent food-derived antioxidant ergothioeine. Transports one sodium ion with one ergothioeine molecule (By similarity). Involved in the absorption of ergothioneine from the luminal/apical side of the small intestine and renal tubular cells, and into non-parenchymal liver cells, thereby contributing to maintain …

**Summary**, from NCBI Gene [6583](https://www.ncbi.nlm.nih.gov/gene/6583):

> Polyspecific organic cation transporters in the liver, kidney, intestine, and other organs are critical for elimination of many endogenous small organic cations as well as a wide array of drugs and environmental toxins. The encoded protein is an organic cation transporter and plasma integral membrane protein containing eleven putative transmembrane domains as well as a nucleotide-binding site motif. Transport by this protein is at least partially ATP-dependent. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:10968](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:10968) · Entrez [6583](https://www.ncbi.nlm.nih.gov/gene/6583) · UniProt [Q9H015](https://www.uniprot.org/uniprotkb/Q9H015) · Ensembl [ENSG00000197208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000197208)

## Data

Gene col 12364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12364); `tables/drug_effects.parquet` (18 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12364]; `tensor/DDL_lfc|DDL_z.npy` [12364]; `embed/gene_vectors.npy` [12364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12364 or target_col == 12364). Every well: [[SLC22A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC22A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
