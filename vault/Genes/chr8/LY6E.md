---
symbol: "LY6E"
type: "gene"
col: 8395
ensembl_id: "ENSG00000160932"
name: "lymphocyte antigen 6 family member E"
location: "8q24.3"
module: 32
arm: "+"
pooled_cpm: 65.56
n_lines_expressing: 46
n_dd_up: 4
n_dd_down: 12
n_dd_up_clean: 0
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 14
direction_downstream: 2
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# LY6E

*lymphocyte antigen 6 family member E* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 3.21× (z +8.0, q 1e-12, up in 39 of 43 measured lines) ⚠ toxic; transcription drop. None of them is without an alert.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (J82 6.14×, NCI-H1573 11.1×, HOP62 5.60×, C32 5.92×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 5.92×, HEC-1-A 5.29×, SW480 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.61×; ⚠ position not correctable).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.184× (z -17.8, q 0e+00, down in 43 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFITM1]] (+0.77, fdr 7e-06), [[UBE2L6]] (+0.75, fdr 7e-06), [[IFITM2]] (+0.75, fdr 8e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 14 arrows point to it, the strongest [[MX1]] → it (grade B ⚠); 2 go from it, the strongest it → [[PARP12]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, 5 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 8395.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 7 lines (J82 6.14×, NCI-H1573 11.1×, HOP62 5.60×, C32 5.92×, …; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 5 µM in 3 lines (J82 5.92×, HEC-1-A 5.29×, SW480 5.70×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change); [[Adagrasib (drug)]] 0.05 µM in 1 line (MIA PaCa-2 1.61×; ⚠ position not correctable).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **3.21×** | +8.0 | 1e-12 | 39/43 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | **2.47×** | +6.5 | 3e-08 | 32/35 (J82, HEC-1-A, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~33% of this change | **2.09×** | +5.5 | 8e-06 | 39/44 (NCI-H2030, HOP62, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | **1.24×** | +4.8 | 2e-04 | 34/44 (MIA PaCa-2, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | 2.09× | +3.2 | 0.14 | 22/40 (J82, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; noisy plate (z scaled) |
| [[Arbutin (drug)]] 5 µM |  | 1.55× | +3.1 | 0.16 | 31/44 (A498, Panc 03.27, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 8395.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.184×** | -17.8 | 0e+00 | 43/43 (LOX-IMVI, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.283×** | -9.4 | 1e-18 | 42/43 (A498, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.616×** | -5.1 | 6e-05 | 34/44 (COLO 205, AsPC-1, …) | rises with dose | position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.440×** | -4.6 | 6e-04 | 36/44 (COLO 205, BT-474, …) | inconsistent across doses | cell-cycle shift (explains ~25% here); noisy plate (z scaled); position effect removed |
| [[Harringtonine (drug)]] 5 µM |  | **0.539×** | -4.4 | 0.001 | 31/44 (LoVo, MIA PaCa-2, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~61% of this change | **0.673×** | -4.2 | 0.003 | 32/44 (COLO 205, MIA PaCa-2, …) | rises with dose | low cells (technical?) |
| [[Belinostat (drug)]] 5 µM |  | **0.587×** | -4.0 | 0.006 | 28/44 (COLO 205, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **0.595×** | -3.9 | 0.007 | 25/44 (A-172, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.607×** | -3.7 | 0.012 | 30/44 (COLO 205, KATO III, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.628×** | -3.5 | 0.028 | 25/44 (AsPC-1, COLO 205, …) | rises with dose | position effect removed |
| [[Verteporfin (drug)]] 5 µM |  | **0.642×** | -3.2 | 0.072 | 29/44 (A-172, RPMI-7951, …) | top dose only | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.655×** | -3.2 | 0.072 | 23/44 (AsPC-1, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.667× | -3.0 | 0.11 | 25/43 (BT-474, HT-29, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.05 per unit of S-phase module lfc, +0.50 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 8395. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[COLO 205 (line)]] | alt | 119 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.125× (z -16.0) |
| [[AsPC-1 (line)]] | alt | 197 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.184× (z -16.6) |
| [[SW480 (line)]] | alt | 19.6 | 2 (2 ⚠) | 2 | [[Dinaciclib (drug)]] 5 µM 5.70× (z +9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -15.2) |
| [[A-172 (line)]] | wt | 129 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -16.2) |
| [[J82 (line)]] | alt | 83.7 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 5.92× (z +11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -11.9) |
| [[KATO III (line)]] | alt | 107 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.0903× (z -19.7) |
| [[MIA PaCa-2 (line)]] | alt | 51.7 | 1 (1 ⚠) | 2 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.61× (z +8.7) ⚠ position not correctable | [[Homoharringtonine (drug)]] 5 µM 0.0885× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 26.0 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 11.1× (z +10.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.0737× (z -17.9) |
| [[SW48 (line)]] | wt | 37.4 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -13.3) |
| [[A-427 (line)]] | wt | 45.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0976× (z -18.2) |
| [[A498 (line)]] | wt | 111 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -16.5) |
| [[C-33 A (line)]] | alt | 38.6 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.119× (z -15.4) |
| [[C32 (line)]] | wt | 72.8 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.92× (z +9.2) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -8.6) |
| [[CFPAC-1 (line)]] | alt | 176 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.219× (z -14.2) |
| [[CHP-212 (line)]] | wt | 65.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -11.7) |
| [[H4 (line)]] | wt | 46.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0762× (z -17.7) |
| [[HEC-1-A (line)]] | alt | 29.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 5.29× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~25% of this change | — |
| [[HOP62 (line)]] | alt | 44.7 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.60× (z +9.5) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -15.4) |
| [[HS-578T (line)]] | alt | 103 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.174× (z -15.0) |
| [[HT-29 (line)]] | alt | 26.3 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 6.00× (z +8.6) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -15.5) |
| [[LOX-IMVI (line)]] | wt | 40.0 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0487× (z -23.6) |
| [[NCI-H1792 (line)]] | alt | 41.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.278× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 34.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0974× (z -18.2) |
| [[Panc 03.27 (line)]] | alt | 277 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.345× (z -10.6) |
| [[RKO (line)]] | wt | 67.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.114× (z -18.0) |
| [[RPMI-7951 (line)]] | alt | 66.1 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.210× (z -12.0) |
| [[SW 900 (line)]] | alt | 132 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.192× (z -14.0) |
| [[A549 (line)]] | wt | 34.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.8) |
| [[BT-474 (line)]] | alt | 92.9 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.0952× (z -19.2) |
| [[Hs 766T (line)]] | wt | 86.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -13.5) |
| [[LoVo (line)]] | wt | 31.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.101× (z -16.7) |
| [[LS 180 (line)]] | wt | 22.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.145× (z -13.2) |
| [[NCI-H2030 (line)]] | alt | 37.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.206× (z -13.0) |
| [[NCI-H2347 (line)]] | alt | 177 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -17.1) |
| [[PANC-1 (line)]] | alt | 41.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.326× (z -10.0) |
| [[SK-MEL-2 (line)]] | alt | 44.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.296× (z -8.5) |
| [[SNU-423 (line)]] | alt | 34.1 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.236× (z -10.0) |
| [[SW1417 (line)]] | alt | 21.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -10.2) |
| [[AN3 CA (line)]] | alt | 27.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 15.4 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 16.0 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 38.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 34.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 37.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 3.00 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 19.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 54.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 14.6 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 8395), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFITM1]] | +0.77 | +0.60 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 614 |
| [[UBE2L6]] | +0.75 | +0.62 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 412 |
| [[IFITM2]] | +0.75 | +0.58 / +0.85 | both halves | 8e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 495 |
| [[BST2]] | +0.74 | +0.60 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_INFLAMMATORY_RESPONSE; STRING 539 |
| [[PSME1]] | +0.73 | +0.67 / +0.73 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE |
| [[SAMHD1]] | +0.73 | +0.52 / +0.82 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IFITM3]] | +0.73 | +0.53 / +0.86 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 717 |
| [[IFI6]] | +0.73 | +0.55 / +0.85 | both halves | 1e-05 | STRING 832 |
| [[OAS1]] | +0.71 | +0.50 / +0.84 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 814 |
| [[PML]] | +0.70 | +0.58 / +0.81 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[IFI35]] | +0.70 | +0.55 / +0.84 | both halves | 1e-05 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 620 |
| [[LGALS3BP]] | +0.69 | +0.69 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 502 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*14 arrows, 14 of them with an alert ⚠; grade A 0, B 14, C 0. Shown: the 12 strongest; 2 more arrows (2 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MX1]] | B | MX1 activity raises LY6E's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.83× lower at baseline in the lines without MX1 | 0.023 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[CD74]] | B | CD74 activity raises LY6E's level | lines that do not express CD74 (31) vs lines expressing it (19) | 1.61× lower at baseline in the lines without CD74 | 0.035 | ⚠ within organs, on part of the lines; also absent: HLA-DRA, SHROOM4, LAPTM5 |
| [[LY6E-DT]] | B | LY6E-DT activity raises LY6E's level | lines that do not express LY6E-DT (5) vs lines expressing it (45) | 3.25× lower at baseline in the lines without LY6E-DT | 0.041 | ⚠ within organs, on part of the lines; also absent: MBOAT1, CELSR1, RHPN2; maybe low, not absent |
| [[IFI44L]] | B | IFI44L activity raises LY6E's level | lines that do not express IFI44L (22) vs lines expressing it (28) | 2.31× lower at baseline in the lines without IFI44L | 0.050 | ⚠ within organs, on part of the lines; also absent: GBP1, EPSTI1, GBP4 |
| [[EPSTI1]] | B | EPSTI1 activity raises LY6E's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 1.90× lower at baseline in the lines without EPSTI1 | 0.051 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[TRIM22]] | B | TRIM22 activity raises LY6E's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 2.17× lower at baseline in the lines without TRIM22 | 0.051 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[GMPR]] | B | GMPR activity raises LY6E's level | lines that do not express GMPR (14) vs lines expressing it (36) | 1.76× lower at baseline in the lines without GMPR | 0.052 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[HLA-F]] | B | HLA-F activity raises LY6E's level | lines that do not express HLA-F (10) vs lines expressing it (40) | 2.10× lower at baseline in the lines without HLA-F | 0.055 | ⚠ within organs, on part of the lines; also absent: DUSP23, HLA-B, ENSG00000290574; maybe low, not absent |
| [[GBP4]] | B | GBP4 activity raises LY6E's level | lines that do not express GBP4 (20) vs lines expressing it (30) | 2.56× lower at baseline in the lines without GBP4 | 0.073 | ⚠ within organs, on part of the lines; also absent: SAMD9L, CD5L, GBP1 |
| [[IFITM1]] | B | IFITM1 activity raises LY6E's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 2.11× lower at baseline in the lines without IFITM1 | 0.080 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[IDO1]] | B | IDO1 activity raises LY6E's level | lines that do not express IDO1 (28) vs lines expressing it (22) | 2.25× lower at baseline in the lines without IDO1 | 0.082 | ⚠ within organs, on part of the lines; also absent: LOX, TNFAIP6, DKK3 |
| [[TRIM34]] | B | TRIM34 activity raises LY6E's level | lines that do not express TRIM34 (6) vs lines expressing it (44) | 2.70× lower at baseline in the lines without TRIM34 | 0.085 | ⚠ within organs, on part of the lines; also absent: BIRC3, FXYD5, TFAP2A; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 0, C 2.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PARP12]] | C | LY6E activity raises PARP12's level | lines that do not express LY6E (4) vs lines expressing it (46) | 2.64× lower at baseline in the lines without LY6E | 0.091 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ARHGEF10; maybe low, not absent |
| cells under [[Cepharanthine (drug)]] 5 µM | C | LY6E activity lowers the cells' numbers under Cepharanthine 5 µM (makes them more sensitive) | lines that do not express LY6E (4) vs lines expressing it (44) | the lines without LY6E: 1.18× the cells of the other lines | 0.098 | ⚠ few lines (4 vs 46); within organs, on part of the lines; also absent: ARHGEF10; maybe low, not absent |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.645). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (50.5, 51.4); signed map (66.4, 28.5). **Vector** length 99.3, 38.3% of its response variance represented; |z| ≥ 3 in 771 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.62 to 23); *Interferon Signaling* (reactome, mean cos +0.60 to 45); *Interferon alpha/beta signaling* (reactome, mean cos +0.63 to 27).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.6 | +2.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.0 | -1.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +3.2 | -0.2 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +2.6 | -3.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.5 | +1.3 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.5 | +0.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.3 | +0.3 |
|  | [[Binimetinib (drug)]] 5 µM |  | +2.3 | +1.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | +2.2 | -1.7 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -5.2 | -5.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -4.3 | -2.7 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -4.2 | -2.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -4.2 | -3.5 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.2 | -17.8 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.1 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | lymphocyte antigen 6 family member E |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,017,982-143,023,832 (+) |
| Ensembl biotype | protein_coding |
| Also known as | TSA-1, RIG-E, SCA-2 |
| Gene groups (HGNC) | LY6/PLAUR domain containing |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 4 pathways, smallest: Dengue Virus Attachment and Entry; Post-translational modification: synthesis of GPI-anchored proteins; Dengue Virus Infection |
| Matched by | ensembl_id |

**Function**, from UniProt [Q16553](https://www.uniprot.org/uniprotkb/Q16553) (Lymphocyte antigen 6E):

> GPI-anchored cell surface protein that regulates T-lymphocytes proliferation, differentiation, and activation. Regulates the T-cell receptor (TCR) signaling by interacting with component CD3Z/CD247 at the plasma membrane, leading to CD3Z/CD247 phosphorylation modulation (By similarity). Restricts the entry of human coronaviruses, including SARS-CoV, MERS-CoV and SARS-CoV-2, by interfering with spike protein-mediated membrane fusion. Also plays an essential role in placenta formation by acting …

**Summary**, from NCBI Gene [4061](https://www.ncbi.nlm.nih.gov/gene/4061):

> This gene belongs to the human Ly6 gene family and encodes a glycosylphosphatidyl-inositol (GPI)-anchored cell surface protein. The protein plays an important role in T cell physiology, oncogenesis and immunological regulation. The protein is also involved in modulation of viral infection by coronaviruses, SARS-CoV, MERS-CoV and SARS-CoV-2. [provided by RefSeq, Aug 2021]

**Accessions** — [HGNC:6727](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6727) · Entrez [4061](https://www.ncbi.nlm.nih.gov/gene/4061) · UniProt [Q16553](https://www.uniprot.org/uniprotkb/Q16553) · Ensembl [ENSG00000160932](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000160932)

## Data

Gene col 8395: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 8395); `tables/drug_effects.parquet` (19 rows, flagged included); `relations/gene_relations.parquet` (col_a == 8395, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 8395]; `tensor/DDL_lfc|DDL_z.npy` [8395]; `embed/gene_vectors.npy` [8395]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 8395 or target_col == 8395). Every well: [[LY6E — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/LY6E.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
