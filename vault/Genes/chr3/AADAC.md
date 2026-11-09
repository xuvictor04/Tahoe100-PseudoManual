---
symbol: "AADAC"
type: "gene"
col: 3586
ensembl_id: "ENSG00000114771"
name: "arylacetamide deacetylase"
location: "3q25.1"
module: 81
arm: "+"
pooled_cpm: 12.12
n_lines_expressing: 16
n_dd_up: 4
n_dd_down: 13
n_dd_up_clean: 1
n_dd_down_clean: 13
in_vector_space: true
direction_upstream: 10
direction_downstream: 16
tags: ["gene", "module/081"]
generated_by: "tahoemap"
---

# AADAC

*arylacetamide deacetylase* — 3q25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 5.86× (z +11.1, q 5e-26, up in 3 of 10 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 1.63× (z +4.5, q 0.001, up in 10 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (none with an alert); the strongest is [[Belinostat (drug)]] 5 µM: 0.533× (z -4.2, q 0.019, down in 9 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[AADACP1]] (+0.88, fdr 7e-06, ⚠ same locus), [[MOCS2-DT]] (+0.67, fdr 7e-06), [[GJA1]] (+0.67, fdr 7e-06), [[SERPIND1]] (+0.66, fdr 1e-05); moves opposite to [[FLVCR2]] (-0.56, fdr 1e-05), [[EDN2]] (-0.54, fdr 2e-05), [[STOM]] (-0.54, fdr 2e-05).
> It is in [[Module 081]], a single-armed module (KRAS signaling up).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[FAM107B]] → it (grade B ⚠); 16 go from it, the strongest it → [[AADACL2-AS1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 4 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3586.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **5.86×** | +11.1 | 5e-26 | 3/10 (H4, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **4.09×** | +9.2 | 8e-18 | 2/12 (CFPAC-1, H4) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **3.21×** | +6.1 | 2e-07 | 0/10 | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.63×** | +4.5 | 0.001 | 10/14 (Panc 03.27, CFPAC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | 1.66× | +3.2 | 0.14 | 1/12 (CFPAC-1) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Lactate (calcium) (drug)]] 5 µM |  | 1.63× | +3.2 | 0.14 | 2/13 (NCI-H1792, SK-MEL-2) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | 1.62× | +3.0 | 0.19 | 1/12 (A-172) | top dose only | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, none with an alert. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 3586.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.533×** | -4.2 | 0.019 | 9/13 (KATO III, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Anethole trithione (drug)]] 5 µM |  | **0.659×** | -3.9 | 0.027 | 3/14 (NCI-H460, CFPAC-1, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Fenofibrate (drug)]] 0.05 µM |  | **0.497×** | -3.7 | 0.041 | 0/13 | inconsistent across doses | noisy plate (z scaled) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.581×** | -3.6 | 0.041 | 11/13 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.586×** | -3.5 | 0.041 | 8/13 (NCI-H1792, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Trametinib (drug)]] 5 µM |  | **0.592×** | -3.5 | 0.041 | 9/14 (AsPC-1, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.592×** | -3.5 | 0.044 | 9/13 (A498, SW 900, …) | all doses, flat | position effect removed |
| [[Radotinib (drug)]] 5 µM |  | **0.701×** | -3.3 | 0.059 | 10/14 (AsPC-1, NCI-H2030, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.606×** | -3.3 | 0.059 | 6/13 (NCI-H1792, A498, …) | rises with dose |  |
| [[Medroxyprogesterone acetate (drug)]] 0.05 µM |  | **0.613×** | -3.2 | 0.070 | 3/13 (A498, NCI-H460, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 5 µM |  | **0.617×** | -3.2 | 0.074 | 9/13 (AsPC-1, NCI-H2030, …) | rises with dose |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **0.626×** | -3.1 | 0.094 | 8/13 (H4, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **0.671×** | -3.1 | 0.098 | 8/14 (NCI-H2030, AsPC-1, …) | two highest doses | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.06 per unit of S-phase module lfc, +0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3586. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW 900 (line)]] | alt | 21.6 | 0 | 2 | — | [[Budesonide (drug)]] 0.05 µM 0.0547× (z -9.4) |
| [[A-172 (line)]] | wt | 19.0 | 0 | 1 | — | [[Ponatinib (drug)]] 0.05 µM 0.0338× (z -9.1) |
| [[A549 (line)]] | wt | 66.2 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.142× (z -9.8) |
| [[AsPC-1 (line)]] | alt | 30.9 | 0 | 1 | — | [[Cobimetinib (drug)]] 0.5 µM 0.120× (z -9.0) |
| [[H4 (line)]] | wt | 23.8 | 0 | 1 | — | [[Dexamethasone (drug)]] 5 µM 0.0212× (z -9.8) |
| [[NCI-H2030 (line)]] | alt | 46.0 | 0 | 1 (1 ⚠) | — | [[Adagrasib (drug)]] 0.05 µM 0.423× (z -11.0) ⚠ position not correctable |
| [[A-427 (line)]] | wt | 0.840 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 7.58 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.992 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.18 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.14 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 26.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 1.10 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.12 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.13 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.33 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.90 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 11.1 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.611 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.45 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 155 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 1.60 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.870 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 39.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 1.05 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 9.52 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 0.811 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.15 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 0.760 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.54 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 0.952 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 7.35 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.49 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 1.01 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.35 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.974 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3586), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AADACP1]] | +0.88 | +0.89 / +0.87 | both halves | 7e-06 | ⚠ same locus (29.7 kb, same strand: neighbours can correlate without regulation) |
| [[MOCS2-DT]] | +0.67 | +0.62 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[GJA1]] | +0.67 | +0.60 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[SERPIND1]] | +0.66 | +0.57 / +0.68 | both halves | 1e-05 | **novel candidate** |
| [[MMP1]] | +0.66 | +0.59 / +0.71 | both halves | 7e-06 |  |
| [[NEK10]] | +0.64 | +0.50 / +0.65 | both halves | 1e-05 |  |
| [[ITGA2]] | +0.63 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[TBILA]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[ANXA10]] | +0.62 | +0.60 / +0.66 | both halves | 7e-06 |  |
| [[PTHLH]] | +0.62 | +0.62 / +0.58 | both halves | 8e-06 |  |
| [[FAM107B]] | +0.61 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[IL1B]] | +0.61 | +0.57 / +0.61 | both halves | 1e-05 |  |
| [[DCBLD2]] | +0.60 | +0.56 / +0.61 | both halves | 1e-05 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FLVCR2]] | -0.56 | -0.52 / -0.56 | both halves | 1e-05 |  |
| [[EDN2]] | -0.54 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[STOM]] | -0.54 | -0.56 / -0.46 | both halves | 2e-05 |  |
| [[RCOR3]] | -0.49 | -0.49 / -0.42 | both halves | 4e-05 |  |
| [[MIRLET7BHG]] | -0.48 | -0.49 / -0.34 | both halves | 1e-04 |  |
| [[CHPT1]] | -0.48 | -0.44 / -0.44 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 3, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM107B]] | B | FAM107B activity raises AADAC's level | lines that do not express FAM107B (11) vs lines expressing it (39) | 2.45× lower at baseline in the lines without FAM107B | 0.075 | ⚠ within organs, on part of the lines; also absent: KIAA1217, ETS2, NRP1 |
| [[S100A16]] | B | S100A16 activity raises AADAC's level | lines that do not express S100A16 (9) vs lines expressing it (41) | 2.15× lower at baseline in the lines without S100A16 | 0.088 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, MET, TGFBR2 |
| [[GRB10]] | B | GRB10 activity raises AADAC's level | lines that do not express GRB10 (11) vs lines expressing it (39) | 2.69× lower at baseline in the lines without GRB10 | 0.090 | ⚠ within organs, on part of the lines; also absent: FAM107B, DGKG, GEM |
| [[AADACP1]] | C | AADACP1 activity raises AADAC's level | lines that do not express AADACP1 (32) vs lines expressing it (18) | 7.63× lower at baseline in the lines without AADACP1 | 3e-05 | ⚠ within organs, on part of the lines; co-absent genes; also absent: AADAC, SLC19A3, IGFN1; co-absent with the target |
| [[SERPINE2]] | C | SERPINE2 activity raises AADAC's level | lines that do not express SERPINE2 (21) vs lines expressing it (29) | 3.09× lower at baseline in the lines without SERPINE2 | 0.009 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, ZNF365, ADAM12; co-absent with the target |
| [[GCKR]] | C | GCKR activity raises AADAC's level | lines that do not express GCKR (24) vs lines expressing it (26) | 3.20× lower at baseline in the lines without GCKR | 0.020 | ⚠ within organs, on part of the lines; also absent: G0S2, IGFBP1, AADAC; maybe low, not absent; co-absent with the target |
| [[IL1RL1]] | C | IL1RL1 activity raises AADAC's level | lines that do not express IL1RL1 (32) vs lines expressing it (18) | 3.12× lower at baseline in the lines without IL1RL1 | 0.031 | ⚠ within organs, on part of the lines; also absent: FAM83A, GSDMC, IGFBP1; co-absent with the target |
| [[BMP2]] | C | BMP2 activity raises AADAC's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.74× lower at baseline in the lines without BMP2 | 0.069 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44; co-absent with the target |
| [[LINC01589]] | C | LINC01589 activity raises AADAC's level | lines that do not express LINC01589 (23) vs lines expressing it (27) | 2.25× lower at baseline in the lines without LINC01589 | 0.070 | ⚠ within organs, on part of the lines; also absent: HNF1B, ENSG00000279806, GOLT1A; co-absent with the target |
| [[ANXA10]] | C | ANXA10 activity raises AADAC's level | lines that do not express ANXA10 (36) vs lines expressing it (14) | 3.12× lower at baseline in the lines without ANXA10 | 0.089 | ⚠ within organs, on part of the lines; also absent: CXCL5, AKR1B10, CP; co-absent with the target |

### Downstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 10, C 6. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AADACL2-AS1]] | B | AADAC activity raises AADACL2-AS1's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.89× lower at baseline in the lines without AADAC | 7e-04 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[FAM107B]] | B | AADAC activity raises FAM107B's level | lines that do not express AADAC (34) vs lines expressing it (16) | 2.96× lower at baseline in the lines without AADAC | 0.023 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[S100A16]] | B | AADAC activity raises S100A16's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.63× lower at baseline in the lines without AADAC | 0.060 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[SERPIND1]] | B | AADAC activity raises SERPIND1's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.32× lower at baseline in the lines without AADAC | 0.062 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[CD55]] | B | AADAC activity raises CD55's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.91× lower at baseline in the lines without AADAC | 0.067 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[LINC03004]] | B | AADAC activity raises LINC03004's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.63× lower at baseline in the lines without AADAC | 0.070 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[STK17A]] | B | AADAC activity raises STK17A's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.69× lower at baseline in the lines without AADAC | 0.078 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[RDH10]] | B | AADAC activity raises RDH10's level | lines that do not express AADAC (34) vs lines expressing it (16) | 1.80× lower at baseline in the lines without AADAC | 0.079 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[GRB10]] | B | AADAC activity raises GRB10's level | lines that do not express AADAC (34) vs lines expressing it (16) | 2.77× lower at baseline in the lines without AADAC | 0.080 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[TFPI]] | B | AADAC activity raises TFPI's level | lines that do not express AADAC (34) vs lines expressing it (16) | 3.08× lower at baseline in the lines without AADAC | 0.099 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610 |
| [[AADACP1]] | C | AADAC activity raises AADACP1's level | lines that do not express AADAC (34) vs lines expressing it (16) | 15.66× lower at baseline in the lines without AADAC | 2e-05 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |
| [[LINC01589]] | C | AADAC activity raises LINC01589's level | lines that do not express AADAC (34) vs lines expressing it (16) | 2.21× lower at baseline in the lines without AADAC | 0.009 | ⚠ within organs, on part of the lines; also absent: AADACP1, SUCNR1, LINC01610; co-absent with the target |

## Where it sits

- **Module**: [[Module 081]] — KRAS signaling up; 55 genes; every member is in the + arm (projection on the module's main direction 0.732). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.29; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (45.1, 15.6); signed map (18.4, 52.6). **Vector** length 59.1, 22.5% of its response variance represented; |z| ≥ 3 in 404 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *KRAS signaling up* (hallmark, mean cos +0.56 to 7).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +3.7 | +11.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +3.4 | +9.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.7 | +2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.2 | +0.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.0 | +2.0 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.8 | +2.1 |
|  | [[Peretinoin (drug)]] 5 µM |  | +1.4 | +1.2 |
| fall | [[Radotinib (drug)]] 5 µM |  | -2.8 | -3.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | -2.4 | -3.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.2 | -3.5 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.1 | -2.5 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | arylacetamide deacetylase |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q25.1 — chr3:151,814,073-151,828,488 (+) |
| Ensembl biotype | protein_coding |
| Also known as | DAC, CES5A1 |
| Gene groups (HGNC) | Lipases; Arylacetamide deacetylase family |
| Reactome | 2 pathways, smallest: Phase I - Functionalization of compounds; Biological oxidations |
| Matched by | ensembl_id |

**Function**, from UniProt [P22760](https://www.uniprot.org/uniprotkb/P22760) (Deacylase AADAC):

> Catalyzes the hydrolysis of ester and amide bonds and is largely involved in prodrugs activation, xenobiotic detoxification or toxicity, and, in some contexts, lipid and indole metabolism. Prefers compounds with relatively small acyl groups, especially compounds with acetyl group. Participates in the hydrolysis of clinical drugs including acetyl esters compounds such as eslicarbazepine, abiraterone and rifamycins (rifampicin, rifabutin, and rifapentine) and N-acetylarylamine compounds such as …

**Summary**, from NCBI Gene [13](https://www.ncbi.nlm.nih.gov/gene/13):

> Microsomal arylacetamide deacetylase competes against the activity of cytosolic arylamine N-acetyltransferase, which catalyzes one of the initial biotransformation pathways for arylamine and heterocyclic amine carcinogens [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:17](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:17) · Entrez [13](https://www.ncbi.nlm.nih.gov/gene/13) · UniProt [P22760](https://www.uniprot.org/uniprotkb/P22760) · Ensembl [ENSG00000114771](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000114771)

## Data

Gene col 3586: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3586); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3586, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3586]; `tensor/DDL_lfc|DDL_z.npy` [3586]; `embed/gene_vectors.npy` [3586]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3586 or target_col == 3586). Every well: [[AADAC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AADAC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
