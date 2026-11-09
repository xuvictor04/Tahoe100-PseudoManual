---
symbol: "OAS1"
type: "gene"
col: 1571
ensembl_id: "ENSG00000089127"
name: "2'-5'-oligoadenylate synthetase 1"
location: "12q24.13"
module: 32
arm: "+"
pooled_cpm: 56.76
n_lines_expressing: 37
n_dd_up: 23
n_dd_down: 63
n_dd_up_clean: 22
n_dd_down_clean: 52
in_vector_space: true
direction_upstream: 67
direction_downstream: 130
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# OAS1

*2'-5'-oligoadenylate synthetase 1* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 23 drug-doses (1 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.02× (z +6.9, q 3e-09, up in 27 of 35 measured lines).
> Pooled over the cell lines (median), lowered significantly by 63 drug-doses (11 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.324× (z -16.0, q 0e+00, down in 30 of 36 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK2]] (+0.95, fdr 7e-06), [[OAS2]] (+0.94, fdr 7e-06, ⚠ same locus), [[PARP9]] (+0.94, fdr 7e-06), [[MX1]] (+0.94, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 67 arrows point to it, the strongest [[IFI44]] → it (grade B ⚠); 130 go from it, the strongest it → [[PARP9]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 23 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1571.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.02×** | +6.9 | 3e-09 | 27/35 (KATO III, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **1.82×** | +5.8 | 1e-06 | 27/34 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Trametinib (drug)]] 0.5 µM |  | **1.43×** | +4.4 | 0.002 | 24/35 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +4.3 | 0.002 | 23/35 (RKO, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.35×** | +4.2 | 0.003 | 21/36 (CFPAC-1, RKO, …) | all doses, flat |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.49×** | +4.1 | 0.004 | 23/36 (CFPAC-1, Panc 03.27, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.51×** | +4.0 | 0.005 | 20/34 (HS-578T, Panc 03.27, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.51×** | +4.0 | 0.005 | 21/36 (Panc 03.27, AsPC-1, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **1.49×** | +3.9 | 0.005 | 21/36 (NCI-H23, CFPAC-1, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.46×** | +3.7 | 0.011 | 19/34 (NCI-H23, MIA PaCa-2, …) | rises with dose |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.47×** | +3.7 | 0.012 | 19/35 (AsPC-1, RKO, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 0.05 µM |  | **1.28×** | +3.6 | 0.018 | 20/35 (NCI-H23, AsPC-1, …) | all doses, flat |  |
| [[Docetaxel (drug)]] 5 µM |  | **1.27×** | +3.4 | 0.026 | 21/35 (SHP-77, NCI-H2347, …) | inconsistent across doses |  |
| [[Abiraterone acetate (drug)]] 0.05 µM |  | **1.39×** | +3.4 | 0.030 | 14/35 (SK-MEL-2, A-172, …) | inconsistent across doses |  |
| [[Trametinib (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.27×** | +3.2 | 0.048 | 16/36 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.38×** | +3.2 | 0.049 | 19/34 (SNU-1, HepG2/C3A, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 63 in all, 11 with an alert ⚠; shown: the 15 strongest. 63 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1571.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.324×** | -16.0 | 0e+00 | 30/36 (A498, CFPAC-1, …) | rises with dose | position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.220×** | -15.2 | 0e+00 | 33/35 (RPMI-7951, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.348×** | -15.0 | 0e+00 | 32/35 (A549, A498, …) | top dose only | cell-cycle shift (explains ~7% here); composition shift |
| [[Belinostat (drug)]] 5 µM |  | **0.236×** | -14.5 | 1e-45 | 31/34 (NCI-H23, SHP-77, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.242×** | -14.3 | 5e-44 | 33/35 (SNU-423, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.377×** | -13.8 | 2e-41 | 30/36 (MIA PaCa-2, A498, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.301×** | -12.1 | 1e-31 | 33/36 (MIA PaCa-2, RPMI-7951, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.315×** | -11.6 | 3e-29 | 30/34 (BT-474, A-172, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.461×** | -11.0 | 3e-26 | 27/35 (SNU-423, RKO, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.495×** | -10.0 | 1e-21 | 31/36 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.374×** | -9.9 | 3e-21 | 33/34 (LoVo, MIA PaCa-2, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.422×** | -8.7 | 2e-16 | 27/36 (BT-474, A498, …) | rises with dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.473×** | -7.5 | 3e-12 | 24/35 (LoVo, A549, …) | rises with dose | cell-cycle shift (explains ~16% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.454×** | -7.5 | 3e-12 | 29/35 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.484×** | -7.3 | 1e-11 | 26/34 (AsPC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.26 per unit of S-phase module lfc, -0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1571. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 64.7 | 0 | 21 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0690× (z -21.4) |
| [[SNU-423 (line)]] | alt | 67.7 | 0 | 21 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0973× (z -20.9) |
| [[LoVo (line)]] | wt | 153 | 0 | 18 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0837× (z -19.5) |
| [[MIA PaCa-2 (line)]] | alt | 74.9 | 0 | 18 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0512× (z -17.8) |
| [[A549 (line)]] | wt | 94.0 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0463× (z -29.0) |
| [[A498 (line)]] | wt | 81.8 | 0 | 15 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -22.7) |
| [[NCI-H1792 (line)]] | alt | 56.1 | 0 | 14 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.120× (z -19.2) |
| [[A-172 (line)]] | wt | 67.3 | 0 | 11 | — | [[Tofacitinib (drug)]] 5 µM 0.194× (z -14.8) |
| [[AsPC-1 (line)]] | alt | 212 | 0 | 11 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.164× (z -12.9) |
| [[NCI-H1573 (line)]] | alt | 82.3 | 0 | 11 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0933× (z -22.2) |
| [[CFPAC-1 (line)]] | alt | 121 | 0 | 10 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.192× (z -17.5) |
| [[COLO 205 (line)]] | alt | 308 | 0 | 10 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0741× (z -18.1) |
| [[HepG2_C3A (line)]] | wt | 60.3 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -15.0) |
| [[NCI-H2347 (line)]] | alt | 74.4 | 1 | 9 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 3.23× (z +8.7) | [[Tofacitinib (drug)]] 5 µM 0.209× (z -16.6) |
| [[SHP-77 (line)]] | alt | 34.0 | 0 | 10 | — | [[Belinostat (drug)]] 5 µM 0.0475× (z -15.2) |
| [[HS-578T (line)]] | alt | 32.3 | 2 (1 ⚠) | 7 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 5.16× (z +9.2) | [[Panobinostat (drug)]] 0.5 µM 0.0793× (z -14.4) |
| [[KATO III (line)]] | alt | 97.9 | 1 | 7 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.09× (z +10.3) | [[Panobinostat (drug)]] 5 µM 0.190× (z -12.4) |
| [[RPMI-7951 (line)]] | alt | 86.8 | 0 | 8 | — | [[Panobinostat (drug)]] 5 µM 0.0642× (z -19.3) |
| [[NCI-H23 (line)]] | alt | 33.4 | 0 | 7 | — | [[Belinostat (drug)]] 5 µM 0.0427× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 52.8 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.158× (z -15.2) |
| [[SW1417 (line)]] | alt | 111 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -14.3) |
| [[Panc 03.27 (line)]] | alt | 56.8 | 0 | 4 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.221× (z -13.5) |
| [[J82 (line)]] | alt | 24.7 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 9.71× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~46% of this change | — |
| [[NCI-H460 (line)]] | wt | 65.7 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -19.2) |
| [[RKO (line)]] | wt | 24.2 | 0 | 3 | — | [[Selinexor (drug)]] 5 µM 0.113× (z -12.8) |
| [[SNU-1 (line)]] | wt | 26.2 | 0 | 3 | — | [[Homoharringtonine (drug)]] 0.05 µM 0.0441× (z -11.6) |
| [[LS 180 (line)]] | wt | 62.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -9.9) |
| [[C-33 A (line)]] | alt | 19.2 | 0 | 1 | — | [[Belinostat (drug)]] 5 µM 0.0477× (z -11.9) |
| [[SW 900 (line)]] | alt | 22.1 | 0 | 1 | — | [[Belinostat (drug)]] 0.5 µM 0.144× (z -8.8) |
| [[A-427 (line)]] | wt | 4.61 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 9.63 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 25.3 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 8.42 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 7.83 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.96 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 91.8 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 30.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.75 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 12.4 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 25.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 88.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 46.9 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.42 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 9.66 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.12 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 10.2 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 6.33 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1571), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK2]] | +0.95 | +0.92 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 776 |
| [[OAS2]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999; ⚠ same locus (45.2 kb, same strand: neighbours can correlate without regulation) |
| [[PARP9]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 870 |
| [[MX1]] | +0.94 | +0.90 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 985 |
| [[IFI44]] | +0.94 | +0.87 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 961 |
| [[IFI35]] | +0.93 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 916 |
| [[IFIT1]] | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 960 |
| [[UBE2L6]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 769 |
| [[IFIT3]] | +0.91 | +0.84 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 947 |
| [[RSAD2]] | +0.91 | +0.85 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 967 |
| [[XAF1]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | pathway: Interferon Signaling; STRING 887 |
| [[SP110]] | +0.91 | +0.82 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 773 |
| [[USP18]] | +0.90 | +0.88 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 960 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*67 arrows, 67 of them with an alert ⚠; grade A 0, B 44, C 23. Shown: the 12 strongest; 55 more arrows (55 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI44]] | B | IFI44 activity raises OAS1's level | lines that do not express IFI44 (12) vs lines expressing it (38) | 3.20× lower at baseline in the lines without IFI44 | 0.001 | ⚠ within organs, on part of the lines; also absent: SAMD9, GBP1, BMP2 |
| [[GBP1]] | B | GBP1 activity raises OAS1's level | lines that do not express GBP1 (16) vs lines expressing it (34) | 3.13× lower at baseline in the lines without GBP1 | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, GBP2, SAMD9 |
| [[SAMD9L]] | B | SAMD9L activity raises OAS1's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 2.94× lower at baseline in the lines without SAMD9L | 0.001 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[GBP4]] | B | GBP4 activity raises OAS1's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.90× lower at baseline in the lines without GBP4 | 0.002 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[OAS3]] | B | OAS3 activity raises OAS1's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 5.74× lower at baseline in the lines without OAS3 | 0.002 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[PLAAT4]] | B | PLAAT4 activity raises OAS1's level | lines that do not express PLAAT4 (21) vs lines expressing it (29) | 2.63× lower at baseline in the lines without PLAAT4 | 0.002 | ⚠ within organs, on part of the lines; also absent: PTPRB, TNFSF10, EPSTI1 |
| [[FBXO39]] | B | FBXO39 activity raises OAS1's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.80× lower at baseline in the lines without FBXO39 | 0.005 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[ODF3B]] | B | ODF3B activity raises OAS1's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 3.07× lower at baseline in the lines without ODF3B | 0.006 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[CD5L]] | B | CD5L activity raises OAS1's level | lines that do not express CD5L (23) vs lines expressing it (27) | 2.82× lower at baseline in the lines without CD5L | 0.007 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[XAF1]] | B | XAF1 activity raises OAS1's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 3.09× lower at baseline in the lines without XAF1 | 0.008 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[HERC6]] | B | HERC6 activity raises OAS1's level | lines that do not express HERC6 (5) vs lines expressing it (45) | 4.88× lower at baseline in the lines without HERC6 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFIH1, IFI35, PARP9; maybe low, not absent |
| [[SAMD9]] | B | SAMD9 activity raises OAS1's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 3.06× lower at baseline in the lines without SAMD9 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |

### Downstream of this gene

*130 arrows, 130 of them with an alert ⚠; grade A 0, B 120, C 10. Shown: the 12 strongest; 118 more arrows (118 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP9]] | B | OAS1 activity raises PARP9's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.29× lower at baseline in the lines without OAS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[N4BP1]] | B | OAS1 activity raises N4BP1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.48× lower at baseline in the lines without OAS1 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[USP18]] | B | OAS1 activity raises USP18's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.15× lower at baseline in the lines without OAS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PLSCR1]] | B | OAS1 activity raises PLSCR1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.30× lower at baseline in the lines without OAS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[OAS3]] | B | OAS1 activity raises OAS3's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.60× lower at baseline in the lines without OAS1 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[NLRC5]] | B | OAS1 activity raises NLRC5's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.53× lower at baseline in the lines without OAS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[HERC6]] | B | OAS1 activity raises HERC6's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 3.06× lower at baseline in the lines without OAS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[HELZ2]] | B | OAS1 activity raises HELZ2's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.76× lower at baseline in the lines without OAS1 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[PARP14]] | B | OAS1 activity raises PARP14's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.55× lower at baseline in the lines without OAS1 | 7e-04 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[ZNFX1]] | B | OAS1 activity raises ZNFX1's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 1.96× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[TMEM140]] | B | OAS1 activity raises TMEM140's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.73× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[IRF9]] | B | OAS1 activity raises IRF9's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.957). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.8, 53.6); signed map (65.1, 31.4). **Vector** length 151, 60.3% of its response variance represented; |z| ≥ 3 in 1,522 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon gamma response* (hallmark, mean cos +0.82 to 60); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.85 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.86 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.2 | +6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~18% of this change | +6.4 | -0.7 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.5 | +5.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +3.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | +4.5 | -3.9 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.1 | +1.6 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.7 | +4.0 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.6 | +4.1 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.5 | +3.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -10.7 | -16.0 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.9 | -13.8 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -8.6 | -8.7 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -8.4 | -11.6 |
|  | [[Selinexor (drug)]] 5 µM |  | -7.3 | -11.0 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.3 | -12.1 |

## What is on record

|  |  |
|---|---|
| Name | 2'-5'-oligoadenylate synthetase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,905,856-112,933,219 (+) |
| Ensembl biotype | protein_coding |
| Also known as | OIASI, IFI-4; previously OIAS |
| Gene groups (HGNC) | 2'-5'-oligoadenylate synthetase family |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE |
| Reactome | 7 pathways, smallest: OAS antiviral response; IFIT antiviral response; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P00973](https://www.uniprot.org/uniprotkb/P00973) (2'-5'-oligoadenylate synthase 1):

> Interferon-induced, dsRNA-activated antiviral enzyme which plays a critical role in cellular innate antiviral response. In addition, it may also play a role in other cellular processes such as apoptosis, cell growth, differentiation and gene regulation. Catalyzes the formation of 2'-5'-oligoadenylates (2-5A) from polymerization of ATP which then bind to the inactive monomeric form of ribonuclease L (RNase L) leading to its dimerization and subsequent activation. Activation of RNase L leads to …

**Summary**, from NCBI Gene [4938](https://www.ncbi.nlm.nih.gov/gene/4938):

> This interferon-induced gene encodes a protein that synthesizes 2',5'-oligoadenylates (2-5As). This protein plays a key role in innate cellular antiviral response, and has been implicated in other cellular processes like cell growth and apoptosis. Alternative splicing results in multiple transcript variants with different enzymatic activities. Polymorphisms in this gene have been associated with susceptibility to viral infection, including SARS-CoV-2, and diabetes mellitus, type 1. This gene is …

**Accessions** — [HGNC:8086](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8086) · Entrez [4938](https://www.ncbi.nlm.nih.gov/gene/4938) · UniProt [P00973](https://www.uniprot.org/uniprotkb/P00973) · Ensembl [ENSG00000089127](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000089127)

## Data

Gene col 1571: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1571); `tables/drug_effects.parquet` (87 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1571, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1571]; `tensor/DDL_lfc|DDL_z.npy` [1571]; `embed/gene_vectors.npy` [1571]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1571 or target_col == 1571). Every well: [[OAS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
