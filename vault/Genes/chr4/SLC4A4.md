---
symbol: "SLC4A4"
type: "gene"
col: 1281
ensembl_id: "ENSG00000080493"
name: "solute carrier family 4 member 4"
location: "4q13.3"
module: 8
arm: "+"
pooled_cpm: 22.59
n_lines_expressing: 21
n_dd_up: 22
n_dd_down: 11
n_dd_up_clean: 18
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 10
direction_downstream: 11
tags: ["gene", "module/008"]
generated_by: "tahoemap"
---

# SLC4A4

*solute carrier family 4 member 4* — 4q13.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 22 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 4.55× (z +28.0, q 0e+00, up in 12 of 18 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (none with an alert); the strongest is [[Dexamethasone (drug)]] 0.5 µM: 0.666× (z -5.3, q 6e-05, down in 9 of 19 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PREX2]] (+0.66, fdr 7e-06), [[HAVCR1]] (+0.66, fdr 1e-05), [[NCKAP5]] (+0.65, fdr 1e-05); moves opposite to [[PPP2R2C]] (-0.51, fdr 1e-04), [[CLTCL1]] (-0.47, fdr 1e-04), [[HMOX2]] (-0.46, fdr 2e-04).
> It is in [[Module 008]], a single-armed module (Dectin-2 family).
> Probable direction (from the cell lines, not proof of direct regulation): 10 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 11 go from it, the strongest it → [[ARHGAP42]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 22 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1281.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **4.55×** | +28.0 | 0e+00 | 12/18 (LoVo, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.86×** | +19.4 | 0e+00 | 10/19 (LoVo, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.89×** | +13.3 | 4e-38 | 8/16 (A549, NCI-H1792, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.01×** | +12.9 | 9e-36 | 10/19 (LoVo, NCI-H2347, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.39×** | +11.0 | 5e-26 | 10/17 (A549, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.33×** | +10.2 | 2e-22 | 5/17 (NCI-H2347, hTERT-HPNE, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **2.01×** | +9.1 | 8e-18 | 10/19 (HOP62, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +8.5 | 2e-15 | 3/19 (HOP62, LoVo, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.85×** | +8.0 | 8e-14 | 9/18 (LoVo, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~1% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.51×** | +7.6 | 1e-12 | 5/19 (HOP62, HS-578T, …) | top dose only | position effect removed |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +6.1 | 5e-08 | 1/18 (HOP62) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +5.9 | 2e-07 | 5/19 (J82, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.48×** | +5.1 | 1e-05 | 0/18 | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.42×** | +4.4 | 5e-04 | 9/19 (CFPAC-1, KATO III, …) | two highest doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.001 | 2/18 (LOX-IMVI, NCI-H2347) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Filgotinib (drug)]] 5 µM |  | **1.38×** | +4.2 | 0.001 | 5/19 (A498, KATO III, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.36×** | +4.0 | 0.002 | 3/19 (H4, SW48, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.38×** | +4.0 | 0.002 | 8/19 (KATO III, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1281.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.666×** | -5.3 | 6e-05 | 9/19 (A498, CFPAC-1, …) | all doses, flat |  |
| [[Artesunate (drug)]] 5 µM |  | **0.780×** | -4.6 | 0.001 | 10/19 (SW 900, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.744×** | -3.9 | 0.016 | 4/17 (A549, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~3% here) |
| [[Dexamethasone (drug)]] 0.05 µM |  | **0.732×** | -3.9 | 0.016 | 7/19 (A498, LOX-IMVI, …) | all doses, flat |  |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.756×** | -3.7 | 0.027 | 5/19 (SW48, A498, …) | top dose only |  |
| [[Mebendazole (drug)]] 5 µM |  | **0.753×** | -3.6 | 0.032 | 3/19 (HT-29, A498, …) | top dose only |  |
| [[Artesunate (drug)]] 0.5 µM |  | **0.767×** | -3.5 | 0.039 | 2/19 (J82, SHP-77) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.053 | 6/19 (HT-29, HS-578T, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.775×** | -3.3 | 0.053 | 8/19 (A498, KATO III, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.780×** | -3.3 | 0.061 | 9/19 (KATO III, CFPAC-1, …) | top dose only |  |
| [[Triamcinolone (drug)]] 5 µM |  | 0.840× | -3.2 | 0.061 | 9/19 (A498, hTERT-HPNE, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 5 µM |  | **0.777×** | -3.2 | 0.068 | 10/19 (A498, CHP-212, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, +0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1281. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[A498 (line)]] | wt | 272 | 0 | 14 (4 ⚠) | — | [[Bortezomib (drug)]] 0.05 µM 0.139× (z -13.0) |
| [[SHP-77 (line)]] | alt | 50.9 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.157× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[CFPAC-1 (line)]] | alt | 119 | 0 | 2 | — | [[Vinblastine (sulfate) (drug)]] 0.5 µM 0.0970× (z -9.4) |
| [[LoVo (line)]] | wt | 6.80 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.13× (z +12.5) | — |
| [[HT-29 (line)]] | alt | 15.9 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.144× (z -8.5) ⚠ unreliable plate only |
| [[KATO III (line)]] | alt | 39.4 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.195× (z -9.5) |
| [[LOX-IMVI (line)]] | wt | 12.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.22× (z +9.8) | — |
| [[NCI-H2030 (line)]] | alt | 12.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -8.6) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 17.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.84× (z +9.2) | — |
| [[A-172 (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 2.79 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 4.99 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.08 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 2.21 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 4.68 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 8.53 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 2.93 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 30.2 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.86 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.02 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.55 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 2.36 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 6.94 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 40.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.18 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 3.03 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 5.01 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 5.41 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 2.41 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.94 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.37 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 2.94 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.04 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 2.62 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 4.27 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.85 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 4.35 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.97 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 6.04 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 2.70 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1281), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*95 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PREX2]] | +0.66 | +0.59 / +0.65 | both halves | 7e-06 |  |
| [[HAVCR1]] | +0.66 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NCKAP5]] | +0.65 | +0.53 / +0.57 | both halves | 1e-05 |  |
| [[TSHZ2]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[TIMD4]] | +0.62 | +0.51 / +0.54 | both halves | 1e-05 |  |
| [[PBX1]] | +0.57 | +0.53 / +0.58 | both halves | 1e-05 |  |
| [[ADAMTS3]] | +0.56 | +0.46 / +0.51 | both halves | 2e-05 |  |
| [[TEX41]] | +0.55 | +0.61 / +0.42 | both halves | 4e-05 |  |
| [[CFH]] | +0.55 | +0.51 / +0.40 | both halves | 5e-05 |  |
| [[SERTAD4]] | +0.55 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[DIO2]] | +0.54 | +0.49 / +0.43 | both halves | 3e-05 |  |
| [[GUCY1A1]] | +0.54 | +0.53 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*5 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PPP2R2C]] | -0.51 | -0.46 / -0.36 | both halves | 1e-04 |  |
| [[CLTCL1]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[HMOX2]] | -0.46 | -0.36 / -0.31 | both halves | 2e-04 |  |
| [[FAM222B]] | -0.46 | -0.40 / -0.39 | both halves | 6e-05 |  |
| [[ZDHHC9]] | -0.44 | -0.43 / -0.31 | both halves | 2e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*10 arrows, 10 of them with an alert ⚠; grade A 0, B 5, C 5.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers SLC4A4's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 4.2% of all compounds | 0.024 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[BDKRB2]] | B | BDKRB2 activity raises SLC4A4's level | lines that do not express BDKRB2 (18) vs lines expressing it (32) | 2.18× lower at baseline in the lines without BDKRB2 | 0.042 | ⚠ within organs, on part of the lines; also absent: NRP1, MAN1A1, ENSG00000287003 |
| [[LINC02889]] | B | LINC02889 activity raises SLC4A4's level | lines that do not express LINC02889 (12) vs lines expressing it (38) | 2.59× lower at baseline in the lines without LINC02889 | 0.053 | ⚠ within organs, on part of the lines; also absent: TMEM92-AS1, SAMD5, ENSG00000226640; maybe low, not absent |
| [[TTC6]] | B | TTC6 activity raises SLC4A4's level | lines that do not express TTC6 (15) vs lines expressing it (35) | 1.64× lower at baseline in the lines without TTC6 | 0.063 | ⚠ within organs, on part of the lines; also absent: SLC27A2, FOXA1, LIMCH1; maybe low, not absent |
| [[PLCB4]] | B | PLCB4 activity raises SLC4A4's level | lines that do not express PLCB4 (13) vs lines expressing it (37) | 2.45× lower at baseline in the lines without PLCB4 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC39A8, ENSG00000248347, PKIA |
| [[PEX5L]] | C | PEX5L activity raises SLC4A4's level | lines that do not express PEX5L (32) vs lines expressing it (18) | 2.11× lower at baseline in the lines without PEX5L | 0.004 | ⚠ within organs, on part of the lines; also absent: ENSG00000253363, APCDD1L, UBBP4-1; maybe low, not absent; co-absent with the target |
| [[SNTG1]] | C | SNTG1 activity raises SLC4A4's level | lines that do not express SNTG1 (38) vs lines expressing it (12) | 2.65× lower at baseline in the lines without SNTG1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ENSG00000232252, ASCL1, SYT4; maybe low, not absent; co-absent with the target |
| [[ARSL]] | C | ARSL activity raises SLC4A4's level | lines that do not express ARSL (26) vs lines expressing it (24) | 2.13× lower at baseline in the lines without ARSL | 0.033 | ⚠ within organs, on part of the lines; also absent: LINC03040, APOL1, SLC44A4; co-absent with the target |
| [[ADAMTS3]] | C | ADAMTS3 activity raises SLC4A4's level | lines that do not express ADAMTS3 (23) vs lines expressing it (27) | 2.45× lower at baseline in the lines without ADAMTS3 | 0.053 | ⚠ within organs, on part of the lines; also absent: ARMCX1, EYA1, ENSG00000232949; co-absent with the target |
| [[TRHDE]] | C | TRHDE activity raises SLC4A4's level | lines that do not express TRHDE (26) vs lines expressing it (24) | 1.84× lower at baseline in the lines without TRHDE | 0.069 | ⚠ within organs, on part of the lines; also absent: ZSCAN23, SAMD3, ITGA11; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 3, C 8.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ARHGAP42]] | B | SLC4A4 activity raises ARHGAP42's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.05× lower at baseline in the lines without SLC4A4 | 0.053 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1 |
| [[RBPMS]] | B | SLC4A4 activity raises RBPMS's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.23× lower at baseline in the lines without SLC4A4 | 0.056 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1 |
| [[AMIGO2]] | B | SLC4A4 activity raises AMIGO2's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.19× lower at baseline in the lines without SLC4A4 | 0.070 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1 |
| [[NRP2]] | C | SLC4A4 activity raises NRP2's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 1.92× lower at baseline in the lines without SLC4A4 | 0.037 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[POU5F1]] | C | SLC4A4 activity raises POU5F1's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.02× lower at baseline in the lines without SLC4A4 | 0.042 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[EDIL3]] | C | SLC4A4 activity raises EDIL3's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.82× lower at baseline in the lines without SLC4A4 | 0.053 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[TRHDE]] | C | SLC4A4 activity raises TRHDE's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 1.64× lower at baseline in the lines without SLC4A4 | 0.055 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[DOCK10]] | C | SLC4A4 activity raises DOCK10's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 3.17× lower at baseline in the lines without SLC4A4 | 0.056 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[IL6]] | C | SLC4A4 activity raises IL6's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 3.49× lower at baseline in the lines without SLC4A4 | 0.090 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[ADAMTS3]] | C | SLC4A4 activity raises ADAMTS3's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 1.99× lower at baseline in the lines without SLC4A4 | 0.094 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |
| [[TARID]] | C | SLC4A4 activity raises TARID's level | lines that do not express SLC4A4 (29) vs lines expressing it (21) | 2.31× lower at baseline in the lines without SLC4A4 | 0.098 | ⚠ within organs, on part of the lines; also absent: PTGS2, LINC00632, AGTR1; co-absent with the target |

## Where it sits

- **Module**: [[Module 008]] — Dectin-2 family; 228 genes; every member is in the + arm (projection on the module's main direction 0.412). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.23; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (37.3, 43.6); signed map (51.1, 27.5). **Vector** length 63.8, 19.0% of its response variance represented; |z| ≥ 3 in 539 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +7.6 | +13.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.3 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.1 | +10.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.4 | +28.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +5.0 | +19.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.5 | +12.9 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.6 | +7.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.4 | +2.7 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.6 | +4.2 |
|  | [[Binimetinib (drug)]] 5 µM |  | +1.6 | +2.6 |
| fall | [[Dexamethasone (drug)]] 0.5 µM |  | -2.9 | -5.3 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~62% of this change | -2.4 | -0.7 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | +0.2 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -2.1 | -2.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -2.1 | -2.6 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -2.1 | -3.9 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.0 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 4 member 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q13.3 — chr4:71,062,667-71,572,087 (+) |
| Ensembl biotype | protein_coding |
| Also known as | NBC1, HNBC1, NBC2, pNBC, hhNMC, kNBC1, KNBC, NBCe1; previously SLC4A5 |
| Gene groups (HGNC) | Solute carrier family 4 |
| Hallmark sets | INFLAMMATORY_RESPONSE |
| Reactome | 6 pathways, smallest: Bicarbonate transporters; SLC-mediated transport of inorganic anions; SLC transporter disorders |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6R1](https://www.uniprot.org/uniprotkb/Q9Y6R1) (Electrogenic sodium bicarbonate cotransporter 1):

> Electrogenic sodium/bicarbonate cotransporter with a Na(+):HCO3(-) stoichiometry varying from 1:2 to 1:3. May regulate bicarbonate influx/efflux at the basolateral membrane of cells and regulate intracellular pH.

**Summary**, from NCBI Gene [8671](https://www.ncbi.nlm.nih.gov/gene/8671):

> This gene encodes a sodium bicarbonate cotransporter (NBC) involved in the regulation of bicarbonate secretion and absorption and intracellular pH. Mutations in this gene are associated with proximal renal tubular acidosis. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Oct 2008]

**Accessions** — [HGNC:11030](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11030) · Entrez [8671](https://www.ncbi.nlm.nih.gov/gene/8671) · UniProt [Q9Y6R1](https://www.uniprot.org/uniprotkb/Q9Y6R1) · Ensembl [ENSG00000080493](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000080493)

## Data

Gene col 1281: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1281); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1281, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1281]; `tensor/DDL_lfc|DDL_z.npy` [1281]; `embed/gene_vectors.npy` [1281]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1281 or target_col == 1281). Every well: [[SLC4A4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC4A4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
