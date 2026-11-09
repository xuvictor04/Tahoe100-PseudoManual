---
symbol: "IFITM3"
type: "gene"
col: 6595
ensembl_id: "ENSG00000142089"
name: "interferon induced transmembrane protein 3"
location: "11p15.5"
module: 32
arm: "+"
pooled_cpm: 150.29
n_lines_expressing: 44
n_dd_up: 1
n_dd_down: 19
n_dd_up_clean: 0
n_dd_down_clean: 15
in_vector_space: true
direction_upstream: 16
direction_downstream: 0
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IFITM3

*interferon induced transmembrane protein 3* — 11p15.5

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 1 drug-dose (1 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.28× (z +4.7, q 0.002, up in 30 of 43 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 5.59×, LS 180 6.60×, HEC-1-A 5.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).
> Pooled over the cell lines (median), lowered significantly by 19 drug-doses (4 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.380× (z -7.7, q 8e-12, down in 37 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFI6]] (+0.91, fdr 7e-06), [[IFITM2]] (+0.91, fdr 7e-06, ⚠ same locus), [[IFITM1]] (+0.89, fdr 7e-06, ⚠ same locus), [[IFI27]] (+0.88, fdr 7e-06), [[ISG15]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 16 arrows point to it, the strongest [[IFITM1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 3 with an alert ⚠. 1 of them raises it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6595.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (J82 5.59×, LS 180 6.60×, HEC-1-A 5.05×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.28×** | +4.7 | 0.002 | 30/43 (J82, LS 180, …) | two highest doses | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~53% of this change | 1.83× | +3.4 | 0.11 | 36/42 (SW1417, PANC-1, …) | inconsistent across doses | low cells (technical?) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | 1.87× | +3.4 | 0.11 | 23/38 (J82, HEC-1-A, …) | two highest doses | composition shift |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 19 in all, 4 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 19 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6595.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.380×** | -7.7 | 8e-12 | 37/43 (COLO 205, AsPC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.287×** | -7.0 | 4e-10 | 37/42 (BT-474, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.290×** | -7.0 | 4e-10 | 37/42 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.416×** | -7.0 | 4e-10 | 36/42 (BT-474, RKO, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.346×** | -6.0 | 3e-07 | 37/42 (LoVo, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.363×** | -5.4 | 7e-06 | 39/42 (COLO 205, LoVo, …) | inconsistent across doses |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.417×** | -4.9 | 7e-05 | 32/43 (BT-474, LoVo, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.542×** | -4.9 | 9e-05 | 30/43 (COLO 205, LoVo, …) | rises with dose | position effect removed |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.454×** | -4.4 | 6e-04 | 30/42 (BT-474, COLO 205, …) | rises with dose | position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.461×** | -4.4 | 8e-04 | 36/42 (LoVo, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.256×** | -4.0 | 0.003 | 35/43 (COLO 205, BT-474, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.516×** | -3.7 | 0.010 | 34/43 (LoVo, BT-474, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~67% of this change | **0.630×** | -3.7 | 0.011 | 33/42 (COLO 205, LoVo, …) | top dose only | low cells (technical?) |
| [[Auranofin (drug)]] 5 µM |  | **0.522×** | -3.7 | 0.011 | 33/42 (LoVo, SHP-77, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.530×** | -3.6 | 0.014 | 28/42 (HepG2/C3A, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.564×** | -3.2 | 0.046 | 27/42 (HepG2/C3A, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[GSK1059615 (drug)]] 5 µM |  | **0.358×** | -3.0 | 0.078 | 34/43 (BT-474, LS 180, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.366×** | -3.0 | 0.092 | 28/43 (LoVo, BT-474, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.15 per unit of S-phase module lfc, +0.73 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6595. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 93.1 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -15.9) |
| [[LoVo (line)]] | wt | 175 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.2) |
| [[COLO 205 (line)]] | alt | 152 | 0 | 5 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.115× (z -13.6) |
| [[AsPC-1 (line)]] | alt | 104 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.166× (z -11.9) |
| [[HepG2_C3A (line)]] | wt | 128 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.177× (z -11.9) |
| [[SHP-77 (line)]] | alt | 51.6 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.137× (z -13.2) |
| [[KATO III (line)]] | alt | 198 | 0 | 3 | — | [[Tofacitinib (drug)]] 5 µM 0.250× (z -10.4) |
| [[RKO (line)]] | wt | 110 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -14.5) |
| [[SNU-423 (line)]] | alt | 301 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.289× (z -9.5) |
| [[A498 (line)]] | wt | 187 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.223× (z -10.7) |
| [[C32 (line)]] | wt | 236 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.315× (z -8.7) |
| [[HS-578T (line)]] | alt | 226 | 0 | 2 | — | [[Tofacitinib (drug)]] 5 µM 0.269× (z -10.8) |
| [[A-172 (line)]] | wt | 396 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.269× (z -10.3) |
| [[CFPAC-1 (line)]] | alt | 232 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.240× (z -10.9) |
| [[HCT15 (line)]] | alt | 142 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.227× (z -10.4) |
| [[HEC-1-A (line)]] | alt | 41.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.05× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[J82 (line)]] | alt | 282 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.59× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[LS 180 (line)]] | wt | 60.8 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.60× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 138 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.278× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 54.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -11.0) |
| [[NCI-H1792 (line)]] | alt | 146 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.253× (z -9.3) |
| [[NCI-H2347 (line)]] | alt | 355 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.268× (z -10.4) |
| [[RPMI-7951 (line)]] | alt | 267 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.291× (z -9.3) |
| [[SK-MEL-2 (line)]] | alt | 137 | 0 | 1 | — | [[Tofacitinib (drug)]] 5 µM 0.240× (z -10.3) |
| [[SW480 (line)]] | alt | 42.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.239× (z -10.4) |
| [[A-427 (line)]] | wt | 53.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 20.6 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 64.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 16.8 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 13.4 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 76.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 33.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 391 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 35.5 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 119 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 87.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 163 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 94.7 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 91.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.7 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 246 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 223 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 120 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 156 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 106 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 172 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 64.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6595), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFI6]] | +0.91 | +0.85 / +0.93 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 862 |
| [[IFITM2]] | +0.91 | +0.71 / +0.96 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 805; ⚠ same locus (10.3 kb: neighbours can correlate without regulation) |
| [[IFITM1]] | +0.89 | +0.77 / +0.94 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 872; ⚠ same locus (4.4 kb: neighbours can correlate without regulation) |
| [[IFI27]] | +0.88 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 829 |
| [[ISG15]] | +0.86 | +0.77 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 911 |
| [[UBE2L6]] | +0.86 | +0.75 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 451 |
| [[OAS1]] | +0.84 | +0.72 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 812 |
| [[SP110]] | +0.83 | +0.73 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[PARP9]] | +0.81 | +0.73 / +0.86 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 641 |
| [[IFIT1]] | +0.81 | +0.74 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 866 |
| [[PSMB9]] | +0.80 | +0.68 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[IFI44L]] | +0.80 | +0.72 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 846 |
| [[MX2]] | +0.80 | +0.71 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 700 |
| [[BST2]] | +0.80 | +0.67 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 699 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*16 arrows, 16 of them with an alert ⚠; grade A 0, B 16, C 0. Shown: the 12 strongest; 4 more arrows (4 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFITM1]] | B | IFITM1 activity raises IFITM3's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.97× lower at baseline in the lines without IFITM1 | 0.003 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IFI44L]] | B | IFI44L activity raises IFITM3's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.14× lower at baseline in the lines without IFI44L | 0.011 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[UBE2L6]] | B | UBE2L6 activity raises IFITM3's level | lines that do not express UBE2L6 (6) vs lines expressing it (44) | 2.65× lower at baseline in the lines without UBE2L6 | 0.015 | ⚠ within organs, on part of the lines; also absent: BLVRA, ADAMTSL4, HLA-B |
| [[HLA-B]] | B | HLA-B activity raises IFITM3's level | lines that do not express HLA-B (9) vs lines expressing it (41) | 2.98× lower at baseline in the lines without HLA-B | 0.022 | ⚠ within organs, on part of the lines; also absent: HLA-F, UBE2L6 |
| [[HLA-F]] | B | HLA-F activity raises IFITM3's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.41× lower at baseline in the lines without HLA-F | 0.026 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises IFITM3's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.04× lower at baseline in the lines without BATF2 | 0.031 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[EPSTI1]] | B | EPSTI1 activity raises IFITM3's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 2.45× lower at baseline in the lines without EPSTI1 | 0.033 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[SAMD9]] | B | SAMD9 activity raises IFITM3's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 2.30× lower at baseline in the lines without SAMD9 | 0.041 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[OAS3]] | B | OAS3 activity raises IFITM3's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 2.69× lower at baseline in the lines without OAS3 | 0.046 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[CCDC194]] | B | CCDC194 activity strengthens IFITM3's drug response | lines that do not express CCDC194 (15) vs lines expressing it (28) | the lines without CCDC194 respond 0.78× as strongly (z diff +0.77); strongest at Panobinostat 5 µM: 0.36x vs 0.25x (z diff +1.8) | 0.046 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22; target measured in part of the lines; the reference differs; artifact flags |
| [[SP110]] | B | SP110 activity raises IFITM3's level | lines that do not express SP110 (5) vs lines expressing it (45) | 3.00× lower at baseline in the lines without SP110 | 0.049 | ⚠ within organs, on part of the lines; also absent: IFIT1; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises IFITM3's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 1.65× lower at baseline in the lines without RSAD2 | 0.060 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.814). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.7, 51.8); signed map (65.7, 29.3). **Vector** length 115, 50.9% of its response variance represented; |z| ≥ 3 in 861 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.78 to 23); *Interferon gamma signaling* (reactome, mean cos +0.67 to 17); *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.72 to 21).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.9 | +2.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +3.7 | +1.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.0 | +1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +2.8 | -1.6 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +2.7 | -0.4 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.4 | +1.3 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +2.3 | +1.4 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +2.2 | +0.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.1 | +0.3 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.3 | -7.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -5.8 | -4.9 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.8 | -4.9 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -5.6 | -4.4 |
|  | [[Auranofin (drug)]] 5 µM |  | -5.6 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | interferon induced transmembrane protein 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11p15.5 — chr11:319,676-329,475 (-) |
| Ensembl biotype | protein_coding |
| Also known as | 1-8U, DSPA2b |
| Gene groups (HGNC) | Interferon induced transmembrane protein family; Dispanins |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, APOPTOSIS, IL2_STAT5_SIGNALING, INTERFERON_GAMMA_RESPONSE |
| Reactome | 3 pathways, smallest: Interferon alpha/beta signaling; Interferon Signaling; Cytokine Signaling in Immune system |
| Matched by | ensembl_id |

**Function**, from UniProt [Q01628](https://www.uniprot.org/uniprotkb/Q01628) (Interferon-induced transmembrane protein 3):

> IFN-induced antiviral protein which disrupts intracellular cholesterol homeostasis. Inhibits the entry of viruses to the host cell cytoplasm by preventing viral fusion with cholesterol depleted endosomes. May inactivate new enveloped viruses which buds out of the infected cell, by letting them go out with a cholesterol depleted membrane. Active against multiple viruses, including influenza A virus, SARS coronaviruses (SARS-CoV and SARS-CoV-2), Marburg virus (MARV), Ebola virus (EBOV), Dengue …

**Summary**, from NCBI Gene [10410](https://www.ncbi.nlm.nih.gov/gene/10410):

> Interferon-induced transmembrane (IFITM) proteins are a family of interferon induced antiviral proteins. The family contains five members, including IFITM1, IFITM2 and IFITM3 and belong to the CD225 superfamily. The protein encoded by this gene restricts cellular entry by diverse viral pathogens, such as influenza A virus, Ebola virus and Sars-CoV-2. [provided by RefSeq, Nov 2021]

**Accessions** — [HGNC:5414](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5414) · Entrez [10410](https://www.ncbi.nlm.nih.gov/gene/10410) · UniProt [Q01628](https://www.uniprot.org/uniprotkb/Q01628) · Ensembl [ENSG00000142089](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000142089)

## Data

Gene col 6595: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6595); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6595, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6595]; `tensor/DDL_lfc|DDL_z.npy` [6595]; `embed/gene_vectors.npy` [6595]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6595 or target_col == 6595). Every well: [[IFITM3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IFITM3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
