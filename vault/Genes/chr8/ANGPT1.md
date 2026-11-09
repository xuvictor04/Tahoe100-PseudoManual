---
symbol: "ANGPT1"
type: "gene"
col: 7783
ensembl_id: "ENSG00000154188"
name: "angiopoietin 1"
location: "8q23.1"
module: 9
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 26
n_dd_up: 14
n_dd_down: 12
n_dd_up_clean: 10
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 20
direction_downstream: 26
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# ANGPT1

*angiopoietin 1* — 8q23.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.36× (z +10.6, q 1e-23, up in 11 of 21 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.57× (z +7.9, q 7e-13, up in 9 of 24 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[5-Azacytidine (drug)]] 5 µM: 0.635× (z -5.7, q 8e-06, down in 11 of 23 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[UNC5C]] (+0.71, fdr 7e-06), [[FIGN]] (+0.65, fdr 1e-05), [[HMCN1]] (+0.64, fdr 7e-06); moves opposite to [[TMEM44]] (-0.47, fdr 3e-05), [[ZFPM1]] (-0.47, fdr 4e-05).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 20 arrows point to it, the strongest [[MEF2C]] → it (grade B ⚠); 26 go from it, the strongest it → [[MEF2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7783.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.36×** | +10.6 | 1e-23 | 11/21 (hTERT-HPNE, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~12% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.00×** | +8.3 | 3e-14 | 6/17 (hTERT-HPNE, J82, …) | all doses, flat | cell-cycle shift (explains ~13% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.57×** | +7.9 | 7e-13 | 9/24 (RPMI-7951, SNU-423, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.90×** | +7.4 | 3e-11 | 8/18 (HS-578T, hTERT-HPNE, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 4e-04 | 8/23 (RPMI-7951, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.6 | 4e-04 | 1/24 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.30×** | +4.5 | 5e-04 | 10/23 (HT-29, SNU-423, …) | top dose only | cell-cycle shift (explains ~6% here); composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.94×** | +4.3 | 0.001 | 2/13 (HOP62, SNU-423) | top dose only | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.5 µM |  | **1.26×** | +3.5 | 0.028 | 9/24 (HOP62, HS-578T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.32×** | +3.4 | 0.032 | 7/24 (HOP62, C32, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.063 | 9/23 (HOP62, HS-578T, …) | all doses, flat |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.31×** | +3.2 | 0.063 | 5/23 (HS-578T, hTERT-HPNE, …) | top dose only |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.29×** | +3.1 | 0.077 | 3/23 (HOP62, H4, …) | all doses, flat |  |
| [[Ixazomib (drug)]] 5 µM |  | **1.61×** | +3.1 | 0.083 | 5/22 (HOP62, H4, …) | inconsistent across doses | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7783.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[5-Azacytidine (drug)]] 5 µM |  | **0.635×** | -5.7 | 8e-06 | 11/23 (C32, H4, …) | top dose only |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.754×** | -5.0 | 1e-04 | 10/24 (CHP-212, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.673×** | -5.0 | 1e-04 | 10/23 (CHP-212, C32, …) | rises with dose |  |
| [[ULK-101 (drug)]] 0.05 µM |  | **0.704×** | -4.1 | 0.005 | 9/23 (NCI-H23, SW 900, …) | inconsistent across doses |  |
| [[Asciminib (drug)]] 0.05 µM |  | **0.734×** | -3.9 | 0.013 | 1/23 (Hs 766T) | inconsistent across doses |  |
| [[Neratinib (drug)]] 5 µM |  | **0.759×** | -3.4 | 0.053 | 6/23 (H4, CHP-212, …) | top dose only |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.763×** | -3.4 | 0.058 | 10/23 (CHP-212, LoVo, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~12% of this change | **0.832×** | -3.3 | 0.075 | 7/24 (SW 900, H4, …) | top dose only | position effect removed |
| [[Mebendazole (drug)]] 5 µM |  | **0.765×** | -3.2 | 0.075 | 3/24 (NCI-H23, CHP-212, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **0.774×** | -3.2 | 0.075 | 3/23 (H4, LoVo, …) | top dose only | position effect removed |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.777×** | -3.2 | 0.080 | 5/24 (C32, H4, …) | inconsistent across doses |  |
| [[vincristine (drug)]] 0.05 µM |  | **0.769×** | -3.1 | 0.089 | 3/24 (SK-MEL-2, Hs 766T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7783. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[CHP-212 (line)]] | wt | 318 | 0 | 12 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0770× (z -18.3) |
| [[LoVo (line)]] | wt | 16.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -10.6) |
| [[LOX-IMVI (line)]] | wt | 68.1 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.288× (z -15.3) |
| [[SHP-77 (line)]] | alt | 42.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.186× (z -11.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.346× (z -10.8) |
| [[A-427 (line)]] | wt | 47.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.205× (z -12.6) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 19.5 | 0 | 1 | — | [[5-Azacytidine (drug)]] 5 µM 0.0816× (z -8.5) |
| [[HOP62 (line)]] | alt | 13.2 | 1 (1 ⚠) | 0 | [[Adagrasib (drug)]] 0.05 µM 2.07× (z +9.7) ⚠ position not correctable | — |
| [[hTERT-HPNE (line)]] | wt | 13.2 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.0718× (z -8.5) |
| [[SK-MEL-2 (line)]] | alt | 6.02 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0647× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[A-172 (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 4.05 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 1.79 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.09 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.974 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.15 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 1.49 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 1.04 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 20.6 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.15 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 1.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.31 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.38 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 1.71 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 4.81 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.911 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 1.69 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 40.4 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.971 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 9.55 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 4.58 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 0.931 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 1.39 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 1.47 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.979 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.21 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 6.19 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 1.30 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 9.04 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.20 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 1.22 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.17 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7783), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[UNC5C]] | +0.71 | +0.58 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[FIGN]] | +0.65 | +0.56 / +0.61 | both halves | 1e-05 |  |
| [[HMCN1]] | +0.64 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[PCDH18]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[SLC6A15]] | +0.63 | +0.56 / +0.60 | both halves | 1e-05 |  |
| [[SULF1]] | +0.61 | +0.43 / +0.64 | both halves | 3e-05 |  |
| [[NREP]] | +0.61 | +0.47 / +0.65 | both halves | 2e-05 |  |
| [[SUSD5]] | +0.61 | +0.51 / +0.56 | both halves | 1e-05 |  |
| [[MMP16]] | +0.60 | +0.58 / +0.59 | both halves | 7e-06 |  |
| [[MAPK10]] | +0.60 | +0.53 / +0.55 | both halves | 1e-05 |  |
| [[EFEMP1]] | +0.59 | +0.50 / +0.60 | both halves | 1e-05 |  |
| [[ARHGAP28]] | +0.59 | +0.49 / +0.60 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM44]] | -0.47 | -0.44 / -0.49 | both halves | 3e-05 |  |
| [[ZFPM1]] | -0.47 | -0.43 / -0.40 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*20 arrows, 20 of them with an alert ⚠; grade A 0, B 4, C 16. Shown: the 12 strongest; 8 more arrows (8 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | MEF2C activity raises ANGPT1's level | lines that do not express MEF2C (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without MEF2C | 0.052 | ⚠ within organs, on part of the lines; also absent: MEF2C-AS1, RGS2, MYOSLID |
| [[PTPN13]] | B | PTPN13 activity raises ANGPT1's level | lines that do not express PTPN13 (10) vs lines expressing it (40) | 4.00× lower at baseline in the lines without PTPN13 | 0.060 | ⚠ within organs, on part of the lines; also absent: MAPK10, AGPAT4, ENSG00000236230 |
| [[MAPK10]] | B | MAPK10 activity raises ANGPT1's level | lines that do not express MAPK10 (11) vs lines expressing it (39) | 3.71× lower at baseline in the lines without MAPK10 | 0.082 | ⚠ within organs, on part of the lines; also absent: PTPN13, HDGFL3, EML1; maybe low, not absent |
| [[RHOBTB3]] | B | RHOBTB3 activity raises ANGPT1's level | lines that do not express RHOBTB3 (10) vs lines expressing it (40) | 3.36× lower at baseline in the lines without RHOBTB3 | 0.091 | ⚠ within organs, on part of the lines; also absent: FYN, POGLUT3; maybe low, not absent |
| [[PCDH18]] | C | PCDH18 activity raises ANGPT1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 5.07× lower at baseline in the lines without PCDH18 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[CDH12]] | C | CDH12 activity raises ANGPT1's level | lines that do not express CDH12 (33) vs lines expressing it (17) | 5.56× lower at baseline in the lines without CDH12 | 0.007 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CDH18, ZIC1, ENSG00000289309; maybe low, not absent; co-absent with the target |
| [[MOXD1]] | C | MOXD1 activity raises ANGPT1's level | lines that do not express MOXD1 (25) vs lines expressing it (25) | 4.40× lower at baseline in the lines without MOXD1 | 0.008 | ⚠ within organs, on part of the lines; also absent: FLNC, EDNRA, ARMCX1; co-absent with the target |
| [[SOX5]] | C | SOX5 activity raises ANGPT1's level | lines that do not express SOX5 (24) vs lines expressing it (26) | 3.89× lower at baseline in the lines without SOX5 | 0.010 | ⚠ within organs, on part of the lines; also absent: CTHRC1, MOXD1, AK5; co-absent with the target |
| [[EPHA5]] | C | EPHA5 activity raises ANGPT1's level | lines that do not express EPHA5 (30) vs lines expressing it (20) | 4.50× lower at baseline in the lines without EPHA5 | 0.011 | ⚠ within organs, on part of the lines; also absent: EPHA5-AS1, CDH10, TRPC4; co-absent with the target |
| [[LUM]] | C | LUM activity raises ANGPT1's level | lines that do not express LUM (34) vs lines expressing it (16) | 3.89× lower at baseline in the lines without LUM | 0.012 | ⚠ within organs, on part of the lines; also absent: ITGA11, DCN, IRAG2; co-absent with the target |
| [[CDH18]] | C | CDH18 activity raises ANGPT1's level | lines that do not express CDH18 (31) vs lines expressing it (19) | 5.01× lower at baseline in the lines without CDH18 | 0.028 | ⚠ within organs, on part of the lines; also absent: CDH12, FAM133A, KCNH5; maybe low, not absent; co-absent with the target |
| [[HMCN1]] | C | HMCN1 activity raises ANGPT1's level | lines that do not express HMCN1 (26) vs lines expressing it (24) | 4.35× lower at baseline in the lines without HMCN1 | 0.055 | ⚠ within organs, on part of the lines; also absent: EPHA5, EPHA5-AS1, ITGA4; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 10, C 16. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | ANGPT1 activity raises MEF2C's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 4.43× lower at baseline in the lines without ANGPT1 | 6e-04 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[PTPN13]] | B | ANGPT1 activity raises PTPN13's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.92× lower at baseline in the lines without ANGPT1 | 0.010 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[DSEL]] | B | ANGPT1 activity raises DSEL's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.69× lower at baseline in the lines without ANGPT1 | 0.019 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[ARHGAP24]] | B | ANGPT1 activity raises ARHGAP24's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 4.22× lower at baseline in the lines without ANGPT1 | 0.026 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[SPOCK3]] | B | ANGPT1 activity raises SPOCK3's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 1.84× lower at baseline in the lines without ANGPT1 | 0.033 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[PLCE1]] | B | ANGPT1 activity raises PLCE1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 1.19× lower at baseline in the lines without ANGPT1 | 0.036 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[MAPK10]] | B | ANGPT1 activity raises MAPK10's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.60× lower at baseline in the lines without ANGPT1 | 0.045 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[DAAM2]] | B | ANGPT1 activity raises DAAM2's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.01× lower at baseline in the lines without ANGPT1 | 0.051 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[LDB2]] | B | ANGPT1 activity raises LDB2's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.36× lower at baseline in the lines without ANGPT1 | 0.070 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[LAMA2]] | B | ANGPT1 activity raises LAMA2's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.03× lower at baseline in the lines without ANGPT1 | 0.079 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5 |
| [[COL12A1]] | C | ANGPT1 activity raises COL12A1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 5.31× lower at baseline in the lines without ANGPT1 | 0.006 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[TLL1]] | C | ANGPT1 activity raises TLL1's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.09× lower at baseline in the lines without ANGPT1 | 0.009 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.590). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (38.6, 30.9); signed map (37.8, 33.1). **Vector** length 62.9, 15.6% of its response variance represented; |z| ≥ 3 in 555 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.7 | +10.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.9 | +8.3 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +6.9 | +7.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.0 | +7.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +4.2 | +4.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.0 | +3.2 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.9 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +3.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.7 | +0.4 |
| fall | [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift | -2.1 | -2.2 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.7 | -1.9 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.7 | -2.3 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.6 | -2.4 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -1.6 | -1.9 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -1.6 | -0.2 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.5 | -3.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | -1.5 | -1.2 |

## What is on record

|  |  |
|---|---|
| Name | angiopoietin 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q23.1 — chr8:107,249,482-107,498,055 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0003, Ang1, AGPT-1 |
| Gene groups (HGNC) | Receptor ligands; Fibrinogen C domain containing; Angiopoietins |
| Hallmark sets | ADIPOGENESIS |
| Reactome | 6 pathways, smallest: Tie2 Signaling; Cell surface interactions at the vascular wall; RAF/MAP kinase cascade |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15389](https://www.uniprot.org/uniprotkb/Q15389) (Angiopoietin-1):

> Binds and activates TEK/TIE2 receptor by inducing its dimerization and tyrosine phosphorylation. Plays an important role in the regulation of angiogenesis, endothelial cell survival, proliferation, migration, adhesion and cell spreading, reorganization of the actin cytoskeleton, but also maintenance of vascular quiescence. Required for normal angiogenesis and heart development during embryogenesis. After birth, activates or inhibits angiogenesis, depending on the context. Inhibits angiogenesis …

**Summary**, from NCBI Gene [284](https://www.ncbi.nlm.nih.gov/gene/284):

> This gene encodes a secreted glycoprotein that belongs to the angiopoietin family. Members of this family play important roles in vascular development and angiogenesis. All angiopoietins bind with similar affinity to an endothelial cell-specific tyrosine-protein kinase receptor. The protein encoded by this gene is a secreted glycoprotein that activates the receptor by inducing its tyrosine phosphorylation. It plays a critical role in mediating reciprocal interactions between the endothelium and …

**Accessions** — [HGNC:484](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:484) · Entrez [284](https://www.ncbi.nlm.nih.gov/gene/284) · UniProt [Q15389](https://www.uniprot.org/uniprotkb/Q15389) · Ensembl [ENSG00000154188](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000154188)

## Data

Gene col 7783: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7783); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7783, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7783]; `tensor/DDL_lfc|DDL_z.npy` [7783]; `embed/gene_vectors.npy` [7783]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7783 or target_col == 7783). Every well: [[ANGPT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/ANGPT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
