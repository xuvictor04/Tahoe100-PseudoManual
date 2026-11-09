---
symbol: "USH1C"
type: "gene"
col: 119
ensembl_id: "ENSG00000006611"
name: "USH1 protein network component harmonin"
location: "11p15.1"
module: 55
arm: "+"
pooled_cpm: 18.54
n_lines_expressing: 16
n_dd_up: 18
n_dd_down: 10
n_dd_up_clean: 12
n_dd_down_clean: 9
in_vector_space: true
direction_upstream: 98
direction_downstream: 53
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# USH1C

*USH1 protein network component harmonin* — 11p15.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (6 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.70× (z +11.7, q 4e-29, up in 3 of 12 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Tucidinostat (drug)]] 5 µM: 1.49× (z +6.7, q 3e-09, up in 7 of 14 measured lines).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 0.5 µM: 0.571× (z -6.6, q 3e-08, down in 11 of 13 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HNF4A]] (+0.75, fdr 7e-06), [[MYO7B]] (+0.75, fdr 7e-06), [[ABO]] (+0.74, fdr 7e-06).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 98 arrows point to it, the strongest [[SMAD9]] → it (grade B ⚠); 53 go from it, the strongest it → [[SMAD9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 6 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 119.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.70×** | +11.7 | 4e-29 | 3/12 (A549, NCI-H460, …) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.84×** | +11.4 | 8e-28 | 1/10 (HEC-1-A) | all doses, flat | cell-cycle shift (explains ~3% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.46×** | +9.1 | 2e-17 | 0/9 | all doses, flat | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.49×** | +6.7 | 3e-09 | 7/14 (A498, SW480, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | **1.83×** | +5.1 | 4e-05 | 1/14 (SW48) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[XRK3F2 (drug)]] 0.5 µM |  | **1.71×** | +4.5 | 5e-04 | 0/14 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.30×** | +4.4 | 1e-03 | 0/13 | inconsistent across doses | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **1.36×** | +3.7 | 0.014 | 7/14 (LoVo, HEC-1-A, …) | inconsistent across doses | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~15% of this change | **1.24×** | +3.7 | 0.014 | 5/14 (LoVo, A498, …) | rises with dose | low cells (technical?) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.43×** | +3.7 | 0.014 | 1/14 (A549) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.073 | 0/14 | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.25×** | +3.1 | 0.083 | 7/14 (NCI-H460, A498, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Erythromycin (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.083 | 0/14 | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~17% of this change | **1.29×** | +3.1 | 0.083 | 7/14 (A549, HEC-1-A, …) | inconsistent across doses |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.29×** | +3.1 | 0.083 | 6/14 (SW480, KATO III, …) | rises with dose |  |
| [[Oxaprozin (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.083 | 1/14 (NCI-H460) | inconsistent across doses |  |
| [[(R)-Verapamil (hydrochloride) (drug)]] 0.5 µM |  | **1.29×** | +3.0 | 0.083 | 0/14 | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 1 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 119.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.571×** | -6.6 | 3e-08 | 11/13 (LoVo, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.635×** | -5.3 | 3e-05 | 11/14 (SW480, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~1% here) |
| [[Anethole trithione (drug)]] 0.5 µM |  | **0.655×** | -5.0 | 1e-04 | 0/14 | inconsistent across doses |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.667×** | -4.7 | 3e-04 | 9/14 (SW480, A-427, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.649×** | -4.3 | 0.002 | 10/14 (AsPC-1, COLO 205, …) | rises with dose | cell-cycle shift (explains ~10% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.797×** | -3.7 | 0.019 | 12/14 (AsPC-1, LoVo, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.734×** | -3.6 | 0.023 | 5/14 (LoVo, LS 180, …) | all doses, flat |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.735×** | -3.6 | 0.023 | 4/14 (SW480, SW48, …) | inconsistent across doses | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.741×** | -3.5 | 0.030 | 12/14 (SW480, COLO 205, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift |
| [[Sapanisertib (drug)]] 5 µM |  | **0.582×** | -3.3 | 0.054 | 1/14 (LS 180) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fenofibrate (drug)]] 0.05 µM |  | 0.757× | -3.0 | 0.14 | 0/14 | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.13 per unit of S-phase module lfc, -0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 119. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 51.4 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.403× (z -11.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.319× (z -10.5) |
| [[COLO 205 (line)]] | alt | 96.9 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.284× (z -10.4) |
| [[AsPC-1 (line)]] | alt | 99.2 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -32.7) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.234× (z -12.3) |
| [[HT-29 (line)]] | alt | 108 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.331× (z -15.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.294× (z -11.7) |
| [[LoVo (line)]] | wt | 39.6 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -20.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.119× (z -19.6) |
| [[A498 (line)]] | wt | 12.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -14.0) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.264× (z -8.6) |
| [[KATO III (line)]] | alt | 19.9 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.210× (z -9.8) |
| [[LS 180 (line)]] | wt | 82.6 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.466× (z -11.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.432× (z -8.7) |
| [[SW48 (line)]] | wt | 11.4 | 0 | 1 | — | [[5-Azacytidine (drug)]] 0.5 µM 0.0845× (z -8.5) |
| [[A-172 (line)]] | wt | 1.63 n.m. | — | — | — | — |
| [[A-427 (line)]] | wt | 12.1 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.08 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 3.60 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 1.51 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 1.87 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 1.57 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 4.44 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 2.14 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 1.79 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 21.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 2.19 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 1.75 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.84 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 2.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 1.33 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 2.12 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 2.27 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.37 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 2.91 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 3.70 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 1.43 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 5.79 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 2.39 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 1.53 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 1.92 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.52 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.69 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 1.73 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 1.90 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 1.90 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.49 n.m. | — | — | — | — |
| [[SW 1271 (line)]] | alt | 1.85 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 2.03 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 143 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 119), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HNF4A]] | +0.75 | +0.68 / +0.74 | both halves | 7e-06 |  |
| [[MYO7B]] | +0.75 | +0.65 / +0.75 | both halves | 7e-06 | STRING 985 |
| [[ABO]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[CYP4F12]] | +0.74 | +0.67 / +0.74 | both halves | 7e-06 | **novel candidate** |
| [[LINC03040]] | +0.74 | +0.66 / +0.61 | both halves | 7e-06 | **novel candidate** |
| [[MUC3A]] | +0.72 | +0.62 / +0.57 | both halves | 1e-05 | **novel candidate** |
| [[PRR15L]] | +0.71 | +0.66 / +0.71 | both halves | 7e-06 |  |
| [[EPS8L3]] | +0.71 | +0.56 / +0.74 | both halves | 1e-05 | STRING 616 |
| [[LINC01814]] | +0.71 | +0.65 / +0.72 | both halves | 7e-06 |  |
| [[TJP3]] | +0.70 | +0.63 / +0.68 | both halves | 7e-06 | same gene group |
| [[CLRN3]] | +0.70 | +0.66 / +0.70 | both halves | 7e-06 | STRING 528 |
| [[SLC44A4]] | +0.70 | +0.63 / +0.66 | both halves | 7e-06 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*98 arrows, 98 of them with an alert ⚠; grade A 0, B 7, C 91. Shown: the 12 strongest; 86 more arrows (86 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | SMAD9 activity lowers USH1C's level | lines that do not express SMAD9 (11) vs lines expressing it (39) | 5.71× higher at baseline in the lines without SMAD9 | 0.023 | ⚠ within organs, on part of the lines; also absent: FAM184A, SAMD11, HHIPL2 |
| [[SEC16B]] | B | SEC16B activity raises USH1C's level | lines that do not express SEC16B (13) vs lines expressing it (37) | 2.93× lower at baseline in the lines without SEC16B | 0.031 | ⚠ within organs, on part of the lines; also absent: CRYZL2P, CYP2S1, GRHL3 |
| [[PLEKHG1]] | B | PLEKHG1 activity raises USH1C's level | lines that do not express PLEKHG1 (17) vs lines expressing it (33) | 3.02× lower at baseline in the lines without PLEKHG1 | 0.040 | ⚠ within organs, on part of the lines; also absent: HLA-V-1, LSR, ARHGAP8 |
| [[VILL]] | B | VILL activity raises USH1C's level | lines that do not express VILL (16) vs lines expressing it (34) | 3.00× lower at baseline in the lines without VILL | 0.056 | ⚠ within organs, on part of the lines; also absent: IL1R2, DNAJC15, EPHA1; maybe low, not absent |
| [[NCALD]] | B | NCALD activity raises USH1C's level | lines that do not express NCALD (18) vs lines expressing it (32) | 2.72× lower at baseline in the lines without NCALD | 0.061 | ⚠ within organs, on part of the lines; also absent: MOGAT3, EPHA1, HNF1A; maybe low, not absent |
| [[SORL1]] | B | SORL1 activity raises USH1C's level | lines that do not express SORL1 (21) vs lines expressing it (29) | 3.22× lower at baseline in the lines without SORL1 | 0.073 | ⚠ within organs, on part of the lines; also absent: PRR15-DT, PLEKHG6, SLC52A3 |
| [[SLC44A3]] | B | SLC44A3 activity raises USH1C's level | lines that do not express SLC44A3 (13) vs lines expressing it (37) | 2.88× lower at baseline in the lines without SLC44A3 | 0.088 | ⚠ within organs, on part of the lines; also absent: SLC44A3-AS1, ENSG00000287306, SH2D3A; maybe low, not absent |
| [[CLRN3]] | C | CLRN3 activity raises USH1C's level | lines that do not express CLRN3 (40) vs lines expressing it (10) | 14.54× lower at baseline in the lines without CLRN3 | 6e-05 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NPSR1, CDH17, MUC13; co-absent with the target |
| [[LINC01559]] | C | LINC01559 activity raises USH1C's level | lines that do not express LINC01559 (38) vs lines expressing it (12) | 9.55× lower at baseline in the lines without LINC01559 | 2e-04 | ⚠ within organs, on part of the lines; also absent: CLRN3, NPSR1, CDH17; co-absent with the target |
| [[HNF1A-AS1]] | C | HNF1A-AS1 activity raises USH1C's level | lines that do not express HNF1A-AS1 (31) vs lines expressing it (19) | 5.44× lower at baseline in the lines without HNF1A-AS1 | 2e-04 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: HNF1A, EPS8L3, GCNT3; maybe low, not absent; co-absent with the target |
| [[NPSR1-AS1]] | C | NPSR1-AS1 activity raises USH1C's level | lines that do not express NPSR1-AS1 (34) vs lines expressing it (16) | 7.04× lower at baseline in the lines without NPSR1-AS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: VIL1, A1CF, EPS8L3; maybe low, not absent; co-absent with the target |
| [[GCNT3]] | C | GCNT3 activity raises USH1C's level | lines that do not express GCNT3 (38) vs lines expressing it (12) | 7.54× lower at baseline in the lines without GCNT3 | 4e-04 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: TRIM31, LYZ, MUC13; co-absent with the target |

### Downstream of this gene

*53 arrows, 53 of them with an alert ⚠; grade A 0, B 6, C 47. Shown: the 12 strongest; 41 more arrows (41 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SMAD9]] | B | USH1C activity lowers SMAD9's level | lines that do not express USH1C (34) vs lines expressing it (16) | 3.34× higher at baseline in the lines without USH1C | 0.023 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[MYH14]] | B | USH1C activity raises MYH14's level | lines that do not express USH1C (34) vs lines expressing it (16) | 4.59× lower at baseline in the lines without USH1C | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[SORL1]] | B | USH1C activity raises SORL1's level | lines that do not express USH1C (34) vs lines expressing it (16) | 4.05× lower at baseline in the lines without USH1C | 0.062 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[TLDC2]] | B | USH1C activity raises TLDC2's level | lines that do not express USH1C (34) vs lines expressing it (16) | 2.06× lower at baseline in the lines without USH1C | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[ARHGEF16]] | B | USH1C activity raises ARHGEF16's level | lines that do not express USH1C (34) vs lines expressing it (16) | 2.79× lower at baseline in the lines without USH1C | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[NGEF]] | B | USH1C activity raises NGEF's level | lines that do not express USH1C (34) vs lines expressing it (16) | 2.14× lower at baseline in the lines without USH1C | 0.099 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2 |
| [[HNF4A]] | C | USH1C activity raises HNF4A's level | lines that do not express USH1C (34) vs lines expressing it (16) | 9.13× lower at baseline in the lines without USH1C | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[EPS8L3]] | C | USH1C activity raises EPS8L3's level | lines that do not express USH1C (34) vs lines expressing it (16) | 5.30× lower at baseline in the lines without USH1C | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[CDHR2]] | C | USH1C activity raises CDHR2's level | lines that do not express USH1C (34) vs lines expressing it (16) | 3.35× lower at baseline in the lines without USH1C | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[MUC13]] | C | USH1C activity raises MUC13's level | lines that do not express USH1C (34) vs lines expressing it (16) | 7.16× lower at baseline in the lines without USH1C | 0.013 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[POF1B]] | C | USH1C activity raises POF1B's level | lines that do not express USH1C (34) vs lines expressing it (16) | 6.54× lower at baseline in the lines without USH1C | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |
| [[INPP5D]] | C | USH1C activity raises INPP5D's level | lines that do not express USH1C (34) vs lines expressing it (16) | 4.06× lower at baseline in the lines without USH1C | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MUC13, CLRN3, HHLA2; co-absent with the target |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.769). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (21.0, 52.5); signed map (61.8, 8.6). **Vector** length 55.1, 20.7% of its response variance represented; |z| ≥ 3 in 298 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +5.4 | +9.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +4.8 | +11.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +3.9 | +11.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.7 | +6.7 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | +2.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.2 | +5.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.6 | +4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.5 | +1.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +1.4 | +3.2 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -2.1 | -5.3 |
|  | [[Digitoxin (drug)]] 0.05 µM |  | -1.5 | -3.6 |
|  | [[Harringtonine (drug)]] 5 µM |  | -1.4 | -4.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.4 | -2.9 |
|  | [[Sapanisertib (drug)]] 5 µM |  | -1.3 | -3.3 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -1.3 | -2.2 |
|  | [[Rutin (trihydrate) (drug)]] 0.05 µM |  | -1.3 | -1.4 |
|  | [[Dabrafenib (drug)]] 5 µM |  | -1.2 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | USH1 protein network component harmonin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.1 — chr11:17,493,895-17,544,416 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PDZ73, harmonin, NY-CO-37, NY-CO-38, PDZ-73, AIE-75, PDZD7C; previously DFNB18 |
| Gene groups (HGNC) | PDZ domain containing |
| Hallmark sets | KRAS_SIGNALING_UP |
| Reactome | 4 pathways, smallest: Sensory processing of sound by outer hair cells of the cochlea; Sensory processing of sound by inner hair cells of the cochlea; Sensory processing of sound |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9Y6N9](https://www.uniprot.org/uniprotkb/Q9Y6N9) (Harmonin):

> Anchoring/scaffolding protein that is a part of the functional network formed by USH1C, USH1G, CDH23 and MYO7A that mediates mechanotransduction in cochlear hair cells. Required for normal development and maintenance of cochlear hair cell bundles (By similarity). As part of the intermicrovillar adhesion complex/IMAC plays a role in brush border differentiation, controlling microvilli organization and length. Probably plays a central regulatory role in the assembly of the complex, recruiting …

**Summary**, from NCBI Gene [10083](https://www.ncbi.nlm.nih.gov/gene/10083):

> This gene encodes a scaffold protein that functions in the assembly of Usher protein complexes. The protein contains PDZ domains, a coiled-coil region with a bipartite nuclear localization signal and a PEST degradation sequence. Defects in this gene are the cause of Usher syndrome type 1C and non-syndromic sensorineural deafness autosomal recessive type 18. Multiple transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Mar 2009]

**Accessions** — [HGNC:12597](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:12597) · Entrez [10083](https://www.ncbi.nlm.nih.gov/gene/10083) · UniProt [Q9Y6N9](https://www.uniprot.org/uniprotkb/Q9Y6N9) · Ensembl [ENSG00000006611](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000006611)

## Data

Gene col 119: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 119); `tables/drug_effects.parquet` (29 rows, flagged included); `relations/gene_relations.parquet` (col_a == 119, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 119]; `tensor/DDL_lfc|DDL_z.npy` [119]; `embed/gene_vectors.npy` [119]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 119 or target_col == 119). Every well: [[USH1C — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/USH1C.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
