---
symbol: "PCDH18"
type: "gene"
col: 12101
ensembl_id: "ENSG00000189184"
name: "protocadherin 18"
location: "4q28.3"
module: 9
arm: "+"
pooled_cpm: 2.19
n_lines_expressing: 16
n_dd_up: 24
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 7
direction_downstream: 30
tags: ["gene", "module/009"]
generated_by: "tahoemap"
---

# PCDH18

*protocadherin 18* — 4q28.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (9 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 11.1× (z +11.0, q 3e-25, up in 0 of 3 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Homoharringtonine (drug)]] 5 µM: 2.35× (z +5.7, q 1e-06, up in 3 of 10 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Artesunate (drug)]] 0.5 µM: 0.456× (z -3.8, q 0.097, down in 4 of 13 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0989×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.227×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MAPK10]] (+0.66, fdr 1e-05), [[UNC5C]] (+0.64, fdr 7e-06), [[CDH6]] (+0.64, fdr 9e-06).
> It is in [[Module 009]], a single-armed module (Neuronal System).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[COL3A1]] → it (grade C ⚠); 30 go from it, the strongest it → [[MEF2C]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 9 with an alert ⚠. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12101.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **11.1×** | +11.0 | 3e-25 | 0/3 | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **6.31×** | +8.7 | 7e-16 | 0/6 | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **6.40×** | +8.1 | 7e-14 | 1/3 (A-427) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift; position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **3.39×** | +5.8 | 1e-06 | 0/3 | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.35×** | +5.7 | 1e-06 | 3/10 (HS-578T, C32, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Selinexor (drug)]] 5 µM |  | **2.25×** | +5.4 | 6e-06 | 3/13 (A-427, C32, …) | top dose only | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **2.21×** | +5.3 | 1e-05 | 4/13 (C32, A-427, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.87×** | +5.0 | 4e-05 | 8/13 (SHP-77, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~4% here); position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.97×** | +5.0 | 4e-05 | 1/6 (hTERT-HPNE) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[AZD2858 (drug)]] 0.5 µM | ⚠ toxic | **4.31×** | +4.9 | 4e-05 | 0/2 | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.73×** | +4.7 | 1e-04 | 0/7 | top dose only | cell-cycle shift (explains ~14% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.99×** | +4.6 | 2e-04 | 1/9 (A-172) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Panobinostat (drug)]] 5 µM |  | **2.12×** | +3.6 | 0.017 | 6/12 (PANC-1, C32, …) | all doses, flat | cell-cycle shift (explains ~5% here); position effect removed |
| [[Imiquimod (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.08×** | +3.4 | 0.023 | 0/7 | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.13×** | +3.4 | 0.023 | 1/6 (hTERT-HPNE) | top dose only | cell-cycle shift (explains ~13% here); position effect removed |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.66×** | +3.4 | 0.024 | 0/13 | top dose only | position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **2.05×** | +3.4 | 0.024 | 5/11 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Lidocaine (hydrochloride) (drug)]] 0.05 µM |  | **2.04×** | +3.4 | 0.024 | 0/3 | inconsistent across doses | low cells (technical?); position effect removed |
| [[Ponatinib (drug)]] 0.5 µM |  | **2.00×** | +3.3 | 0.031 | 3/9 (PANC-1, HS-578T, …) | rises with dose |  |
| [[Saquinavir (drug)]] 5 µM |  | **1.60×** | +3.1 | 0.049 | 0/8 | inconsistent across doses |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.93×** | +3.1 | 0.052 | 1/7 (HS-578T) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.91×** | +3.0 | 0.059 | 9/14 (PANC-1, NCI-H1792, …) | rises with dose |  |
| [[XRK3F2 (drug)]] 0.5 µM |  | **2.45×** | +3.0 | 0.062 | 0/3 | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM |  | **1.88×** | +3.0 | 0.071 | 0/7 | inconsistent across doses | low cells (technical?) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12101.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H661 0.0989×; ⚠ toxic; transcription drop); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H661 0.227×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 0.5 µM |  | **0.456×** | -3.8 | 0.097 | 4/13 (RPMI-7951, A-172, …) | inconsistent across doses |  |
| [[Sapanisertib (drug)]] 5 µM |  | 0.300× | -3.0 | 0.47 | 2/12 (Hs 766T, C32) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12101. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H661 (line)]] | alt | 188 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0989× (z -9.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.227× (z -8.5) |
| [[A-172 (line)]] | wt | 0.871 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 0.193 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 0.107 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 0.231 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 0.134 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 0.110 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 0.181 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 0.740 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 27.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 0.124 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.66 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 0.122 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 0.132 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 0.326 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.83 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 2.72 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 0.150 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.63 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 0.383 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.120 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 0.107 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 0.287 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.124 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 0.122 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 0.137 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 0.637 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 0.111 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 1.50 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 0.138 n.m. | — | — | — | — |
| [[NCI-H2347 (line)]] | alt | 0.154 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 0.187 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 1.49 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.104 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 0.744 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.545 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 1.38 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 0.576 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 0.195 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 0.150 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 0.208 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 0.147 n.m. | — | — | — | — |
| [[SW 900 (line)]] | alt | 0.205 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 0.121 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 0.149 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 0.138 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12101), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MAPK10]] | +0.66 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[UNC5C]] | +0.64 | +0.63 / +0.64 | both halves | 7e-06 |  |
| [[CDH6]] | +0.64 | +0.57 / +0.66 | both halves | 9e-06 | **novel candidate** |
| [[EPHA5]] | +0.63 | +0.62 / +0.67 | both halves | 7e-06 |  |
| [[ANGPT1]] | +0.63 | +0.59 / +0.66 | both halves | 7e-06 |  |
| [[CDH8]] | +0.61 | +0.39 / +0.71 | both halves | 5e-05 |  |
| [[EPHA5-AS1]] | +0.60 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[ZFHX4]] | +0.59 | +0.53 / +0.62 | both halves | 1e-05 |  |
| [[CRISPLD1]] | +0.58 | +0.45 / +0.64 | both halves | 3e-05 |  |
| [[TP63]] | +0.57 | +0.50 / +0.55 | both halves | 1e-05 |  |
| [[SIM1]] | +0.57 | +0.59 / +0.51 | both halves | 1e-05 |  |
| [[SULF1]] | +0.57 | +0.42 / +0.57 | both halves | 4e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 0, C 7.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[COL3A1]] | C | COL3A1 activity raises PCDH18's level | lines that do not express COL3A1 (35) vs lines expressing it (15) | 3.88× lower at baseline in the lines without COL3A1 | 0.008 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: THY1, PDGFRB, ZNF677; co-absent with the target |
| [[ZNF677]] | C | ZNF677 activity raises PCDH18's level | lines that do not express ZNF677 (39) vs lines expressing it (11) | 5.44× lower at baseline in the lines without ZNF677 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53, KRAS; also absent: COL11A1, COL3A1, GCG; co-absent with the target |
| [[MEOX2]] | C | MEOX2 activity raises PCDH18's level | lines that do not express MEOX2 (36) vs lines expressing it (14) | 3.63× lower at baseline in the lines without MEOX2 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: LINC02566, MMRN1, ENSG00000232252; co-absent with the target |
| [[BCHE]] | C | BCHE activity raises PCDH18's level | lines that do not express BCHE (35) vs lines expressing it (15) | 3.01× lower at baseline in the lines without BCHE | 0.070 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: NETO1, ENSG00000226043, MAGEB2; co-absent with the target |
| [[COL5A2]] | C | COL5A2 activity raises PCDH18's level | lines that do not express COL5A2 (29) vs lines expressing it (21) | 2.35× lower at baseline in the lines without COL5A2 | 0.073 | ⚠ within organs, on part of the lines; also absent: COL1A2, COL3A1, TRIML2; co-absent with the target |
| [[ANGPT1]] | C | ANGPT1 activity raises PCDH18's level | lines that do not express ANGPT1 (24) vs lines expressing it (26) | 2.45× lower at baseline in the lines without ANGPT1 | 0.074 | ⚠ within organs, on part of the lines; also absent: HTR1F, KC6, AK5; co-absent with the target |
| [[COL11A1]] | C | COL11A1 activity raises PCDH18's level | lines that do not express COL11A1 (39) vs lines expressing it (11) | 3.44× lower at baseline in the lines without COL11A1 | 0.095 | ⚠ within organs, on part of the lines; co-occurs with KRAS, TP53; also absent: ZNF677, THY1, LINC02566; co-absent with the target |

### Downstream of this gene

*30 arrows, 30 of them with an alert ⚠; grade A 0, B 10, C 20. Shown: the 12 strongest; 18 more arrows (18 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MEF2C]] | B | PCDH18 activity raises MEF2C's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.17× lower at baseline in the lines without PCDH18 | 0.003 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[RAB30]] | B | PCDH18 activity raises RAB30's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.92× lower at baseline in the lines without PCDH18 | 0.005 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[MAP1A]] | B | PCDH18 activity raises MAP1A's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 4.11× lower at baseline in the lines without PCDH18 | 0.037 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[MEF2C]] | B | PCDH18 activity strengthens MEF2C's drug response | lines that do not express PCDH18 (21) vs lines expressing it (13) | the lines without PCDH18 respond 0.91× as strongly (z diff +1.15); strongest at Auranofin 5 µM: 0.56x vs 0.41x (z diff +3.8) | 0.041 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; target measured in part of the lines; artifact flags |
| [[TFAP2A]] | B | PCDH18 activity lowers TFAP2A's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.30× higher at baseline in the lines without PCDH18 | 0.053 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[LRIG3]] | B | PCDH18 activity raises LRIG3's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.57× lower at baseline in the lines without PCDH18 | 0.075 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[BEND6]] | B | PCDH18 activity raises BEND6's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.57× lower at baseline in the lines without PCDH18 | 0.081 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[CALCRL]] | B | PCDH18 activity raises CALCRL's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 2.50× lower at baseline in the lines without PCDH18 | 0.083 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[TRERF1]] | B | PCDH18 activity raises TRERF1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 1.32× lower at baseline in the lines without PCDH18 | 0.088 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[NREP]] | B | PCDH18 activity raises NREP's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 3.13× lower at baseline in the lines without PCDH18 | 0.097 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677 |
| [[ANGPT1]] | C | PCDH18 activity raises ANGPT1's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 5.07× lower at baseline in the lines without PCDH18 | 0.004 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |
| [[ZNF677]] | C | PCDH18 activity raises ZNF677's level | lines that do not express PCDH18 (34) vs lines expressing it (16) | 3.37× lower at baseline in the lines without PCDH18 | 0.009 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZIC1, DCN, ZNF677; co-absent with the target |

## Where it sits

- **Module**: [[Module 009]] — Neuronal System; 222 genes; every member is in the + arm (projection on the module's main direction 0.628). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (37.9, 31.2); signed map (37.9, 32.5). **Vector** length 26.5, 6.28% of its response variance represented; |z| ≥ 3 in 294 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +2.2 | +8.1 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +2.2 | +11.0 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +2.1 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +1.6 | +5.3 |
|  | [[Selinexor (drug)]] 5 µM |  | +1.5 | +5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +1.2 | +3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +1.0 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +1.0 | +2.3 |
|  | [[Ponatinib (drug)]] 0.5 µM |  | +0.9 | +3.3 |
| fall | [[Sapanisertib (drug)]] 5 µM |  | -0.8 | -3.0 |
|  | [[BAY1125976 (drug)]] 5 µM |  | -0.8 | -2.2 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -0.7 | -2.6 |
|  | [[Artesunate (drug)]] 5 µM | ⚠ cell-cycle shift | -0.6 | -1.8 |
|  | [[4EGI-1 (drug)]] 0.5 µM | ⚠ cell-cycle shift | -0.6 | -0.9 |
|  | [[Budesonide (drug)]] 5 µM |  | -0.6 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.05 µM |  | -0.6 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | protocadherin 18 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.3 — chr4:137,518,918-137,532,494 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA1562, PCDH68L |
| Gene groups (HGNC) | Non-clustered protocadherins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9HCL0](https://www.uniprot.org/uniprotkb/Q9HCL0) (Protocadherin-18):

> Potential calcium-dependent cell-adhesion protein.

**Summary**, from NCBI Gene [54510](https://www.ncbi.nlm.nih.gov/gene/54510):

> This gene belongs to the protocadherin gene family, a subfamily of the cadherin superfamily. This gene encodes a protein which contains 6 extracellular cadherin domains, a transmembrane domain and a cytoplasmic tail differing from those of the classical cadherins. Although its specific function is undetermined, the cadherin-related neuronal receptor is thought to play a role in the establishment and function of specific cell-cell connections in the brain. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:14268](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14268) · Entrez [54510](https://www.ncbi.nlm.nih.gov/gene/54510) · UniProt [Q9HCL0](https://www.uniprot.org/uniprotkb/Q9HCL0) · Ensembl [ENSG00000189184](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000189184)

## Data

Gene col 12101: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12101); `tables/drug_effects.parquet` (26 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12101, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12101]; `tensor/DDL_lfc|DDL_z.npy` [12101]; `embed/gene_vectors.npy` [12101]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12101 or target_col == 12101). Every well: [[PCDH18 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PCDH18.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
