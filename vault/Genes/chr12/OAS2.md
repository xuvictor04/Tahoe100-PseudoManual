---
symbol: "OAS2"
type: "gene"
col: 3222
ensembl_id: "ENSG00000111335"
name: "2'-5'-oligoadenylate synthetase 2"
location: "12q24.13"
module: 32
arm: "+"
pooled_cpm: 52.16
n_lines_expressing: 36
n_dd_up: 12
n_dd_down: 62
n_dd_up_clean: 12
n_dd_down_clean: 51
in_vector_space: true
direction_upstream: 55
direction_downstream: 127
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# OAS2

*2'-5'-oligoadenylate synthetase 2* — 12q24.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 0.5 µM: 2.27× (z +6.2, q 3e-07, up in 24 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 62 drug-doses (11 with an alert ⚠); the strongest is [[Tofacitinib (drug)]] 5 µM: 0.179× (z -18.1, q 0e+00, down in 30 of 34 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CMPK2]] (+0.97, fdr 7e-06), [[MX1]] (+0.96, fdr 7e-06), [[OAS3]] (+0.95, fdr 7e-06, ⚠ same locus), [[XAF1]] (+0.94, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 55 arrows point to it, the strongest [[CD5L]] → it (grade B ⚠); 127 go from it, the strongest it → [[OAS3]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, none with an alert. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 3222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **2.27×** | +6.2 | 3e-07 | 24/34 (NCI-H2347, CFPAC-1, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.29×** | +6.0 | 5e-07 | 29/33 (J82, RKO, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.84×** | +4.4 | 0.002 | 27/34 (LoVo, NCI-H460, …) | inconsistent across doses | position effect removed |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.76×** | +4.3 | 0.003 | 27/33 (AsPC-1, A549, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.66×** | +3.7 | 0.025 | 21/33 (AsPC-1, A549, …) | all doses, stronger at high dose | position effect removed |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.61×** | +3.6 | 0.029 | 23/34 (SK-MEL-2, AsPC-1, …) | inconsistent across doses |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.57×** | +3.5 | 0.040 | 21/34 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Trametinib (drug)]] 0.05 µM |  | **1.37×** | +3.4 | 0.046 | 20/34 (AsPC-1, A549, …) | all doses, flat |  |
| [[Larotrectinib (drug)]] 5 µM |  | **1.36×** | +3.4 | 0.046 | 20/34 (HS-578T, KATO III, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.55×** | +3.3 | 0.046 | 22/34 (A-172, NCI-H2347, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **1.54×** | +3.3 | 0.050 | 17/34 (AsPC-1, COLO 205, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.41×** | +3.3 | 0.050 | 21/34 (AsPC-1, LoVo, …) | all doses, flat | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 62 in all, 11 with an alert ⚠; shown: the 15 strongest. 62 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 3222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tofacitinib (drug)]] 5 µM |  | **0.179×** | -18.1 | 0e+00 | 30/34 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.0904×** | -17.9 | 0e+00 | 32/33 (NCI-H1792, HS-578T, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.0913×** | -17.8 | 0e+00 | 34/34 (LoVo, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.0924×** | -17.8 | 0e+00 | 33/34 (RPMI-7951, MIA PaCa-2, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.215×** | -16.2 | 0e+00 | 30/34 (CFPAC-1, COLO 205, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.118×** | -15.9 | 0e+00 | 34/34 (LoVo, SNU-423, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.174×** | -13.0 | 9e-37 | 33/34 (HS-578T, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.186×** | -12.5 | 3e-34 | 30/34 (BT-474, LoVo, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.198×** | -12.1 | 1e-31 | 29/34 (KATO III, BT-474, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.335×** | -11.5 | 7e-29 | 32/34 (LoVo, COLO 205, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.225×** | -11.1 | 6e-27 | 30/33 (LoVo, SNU-423, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.370×** | -10.4 | 8e-24 | 25/34 (NCI-H1573, A498, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift; position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.260×** | -10.0 | 5e-22 | 29/33 (LoVo, MIA PaCa-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.261×** | -10.0 | 6e-22 | 32/33 (BT-474, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.292×** | -8.6 | 2e-16 | 30/34 (COLO 205, MIA PaCa-2, …) | all doses, flat | cell-cycle shift (explains ~0% here); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.23 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 3222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 78.7 | 0 | 28 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0119× (z -21.0) |
| [[LoVo (line)]] | wt | 96.6 | 0 | 25 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0160× (z -23.9) |
| [[A-172 (line)]] | wt | 133 | 0 | 21 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0284× (z -21.6) |
| [[A498 (line)]] | wt | 157 | 0 | 21 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0347× (z -19.8) |
| [[NCI-H1573 (line)]] | alt | 62.2 | 0 | 21 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0495× (z -23.0) |
| [[SNU-423 (line)]] | alt | 115 | 0 | 21 (6 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0156× (z -22.2) |
| [[NCI-H1792 (line)]] | alt | 81.2 | 0 | 20 (6 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.00680× (z -27.8) |
| [[A549 (line)]] | wt | 41.9 | 0 | 19 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0654× (z -17.5) |
| [[HS-578T (line)]] | alt | 58.4 | 0 | 19 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0188× (z -22.9) |
| [[MIA PaCa-2 (line)]] | alt | 108 | 0 | 19 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0110× (z -22.1) |
| [[AsPC-1 (line)]] | alt | 68.3 | 0 | 16 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0285× (z -17.1) |
| [[COLO 205 (line)]] | alt | 181 | 0 | 16 | — | [[Panobinostat (drug)]] 0.5 µM 0.0120× (z -22.4) |
| [[KATO III (line)]] | alt | 69.8 | 0 | 16 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0141× (z -21.8) |
| [[CFPAC-1 (line)]] | alt | 115 | 0 | 14 (4 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0745× (z -23.5) |
| [[RPMI-7951 (line)]] | alt | 159 | 0 | 14 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0271× (z -23.9) |
| [[SK-MEL-2 (line)]] | alt | 85.7 | 0 | 13 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0262× (z -20.0) |
| [[NCI-H2347 (line)]] | alt | 97.0 | 1 | 11 (1 ⚠) | [[Harringtonine (drug)]] 0.5 µM 4.16× (z +9.4) | [[Tofacitinib (drug)]] 5 µM 0.100× (z -21.3) |
| [[Panc 03.27 (line)]] | alt | 65.3 | 0 | 10 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.148× (z -15.2) |
| [[RKO (line)]] | wt | 23.8 | 0 | 10 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0102× (z -16.4) |
| [[SW1417 (line)]] | alt | 51.8 | 0 | 9 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0913× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 39.9 | 0 | 8 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0331× (z -13.2) |
| [[SW 900 (line)]] | alt | 40.1 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.0841× (z -11.1) |
| [[NCI-H23 (line)]] | alt | 22.3 | 0 | 6 | — | [[Belinostat (drug)]] 5 µM 0.0458× (z -11.9) |
| [[J82 (line)]] | alt | 51.6 | 3 (3 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 13.5× (z +14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change | [[Tofacitinib (drug)]] 5 µM 0.182× (z -12.9) |
| [[SHP-77 (line)]] | alt | 19.2 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.133× (z -10.4) |
| [[Hs 766T (line)]] | wt | 89.2 | 0 | 4 | — | [[Panobinostat (drug)]] 0.5 µM 0.0963× (z -15.0) |
| [[NCI-H460 (line)]] | wt | 17.6 | 0 | 4 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0904× (z -14.5) |
| [[LOX-IMVI (line)]] | wt | 20.7 | 0 | 3 | — | [[Belinostat (drug)]] 5 µM 0.0223× (z -12.7) |
| [[C32 (line)]] | wt | 21.8 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0755× (z -10.3) |
| [[LS 180 (line)]] | wt | 14.7 | 0 | 2 | — | [[Panobinostat (drug)]] 0.5 µM 0.0526× (z -14.8) |
| [[H4 (line)]] | wt | 21.1 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0583× (z -10.8) ⚠ unreliable plate only |
| [[A-427 (line)]] | wt | 2.85 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 6.68 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 5.06 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 4.69 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 5.65 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 9.02 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.11 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 7.15 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 29.0 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.18 n.m. | — | — | — | — |
| [[PANC-1 (line)]] | alt | 8.52 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 12.6 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 6.83 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 4.75 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 3.34 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 3222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 2 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CMPK2]] | +0.97 | +0.93 / +0.97 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 794 |
| [[MX1]] | +0.96 | +0.94 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 978 |
| [[OAS3]] | +0.95 | +0.92 / +0.96 | both halves | 7e-06 | same gene group; pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 999; ⚠ same locus (1.9 kb, same strand: neighbours can correlate without regulation) |
| [[OAS1]] | +0.94 | +0.92 / +0.95 | both halves | 7e-06 | same gene group; pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 999; ⚠ same locus (45.2 kb, same strand: neighbours can correlate without regulation) |
| [[XAF1]] | +0.94 | +0.86 / +0.96 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 933 |
| [[PARP9]] | +0.94 | +0.86 / +0.96 | both halves | 7e-06 | STRING 875 |
| [[IFIT1]] | +0.94 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 966 |
| [[IFI44]] | +0.93 | +0.88 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 941 |
| [[IFIT3]] | +0.93 | +0.88 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 947 |
| [[IFI44L]] | +0.92 | +0.86 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 935 |
| [[USP18]] | +0.92 | +0.87 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 916 |
| [[SAMD9L]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 835 |
| [[MX2]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 948 |
| [[STAT1]] | +0.91 | +0.87 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 972 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*55 arrows, 55 of them with an alert ⚠; grade A 0, B 38, C 17. Shown: the 12 strongest; 43 more arrows (43 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CD5L]] | B | CD5L activity raises OAS2's level | lines that do not express CD5L (23) vs lines expressing it (27) | 4.23× lower at baseline in the lines without CD5L | 1e-03 | ⚠ within organs, on part of the lines; also absent: GBP4, TRIM22, GBP5; maybe low, not absent |
| [[RSAD2]] | B | RSAD2 activity raises OAS2's level | lines that do not express RSAD2 (14) vs lines expressing it (36) | 3.91× lower at baseline in the lines without RSAD2 | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS |
| [[XAF1]] | B | XAF1 activity raises OAS2's level | lines that do not express XAF1 (14) vs lines expressing it (36) | 4.80× lower at baseline in the lines without XAF1 | 0.002 | ⚠ within organs, on part of the lines; also absent: SLC15A3, TRIM22, FBXO39 |
| [[SAMD9]] | B | SAMD9 activity raises OAS2's level | lines that do not express SAMD9 (11) vs lines expressing it (39) | 4.69× lower at baseline in the lines without SAMD9 | 0.004 | ⚠ within organs, on part of the lines; also absent: IFI44, GBP1, TLR6 |
| [[CCDC194]] | B | CCDC194 activity raises OAS2's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 3.59× lower at baseline in the lines without CCDC194 | 0.007 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |
| [[OAS3]] | B | OAS3 activity raises OAS2's level | lines that do not express OAS3 (5) vs lines expressing it (45) | 6.17× lower at baseline in the lines without OAS3 | 0.007 | ⚠ within organs, on part of the lines; also absent: ENSG00000280007, PARP9, USP18 |
| [[IFITM1]] | B | IFITM1 activity raises OAS2's level | lines that do not express IFITM1 (19) vs lines expressing it (31) | 4.13× lower at baseline in the lines without IFITM1 | 0.007 | ⚠ within organs, on part of the lines; also absent: TRIM22, IFI6, SLC15A3 |
| [[PLSCR1]] | B | PLSCR1 activity raises OAS2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 5.42× lower at baseline in the lines without PLSCR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[ODF3B]] | B | ODF3B activity raises OAS2's level | lines that do not express ODF3B (13) vs lines expressing it (37) | 2.95× lower at baseline in the lines without ODF3B | 0.007 | ⚠ within organs, on part of the lines; also absent: TYMP, RPP25, CGAS |
| [[MMP13]] | B | MMP13 activity raises OAS2's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 2.59× lower at baseline in the lines without MMP13 | 0.008 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[BST2]] | B | BST2 activity raises OAS2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 3.70× lower at baseline in the lines without BST2 | 0.013 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[TNFSF10]] | B | TNFSF10 activity raises OAS2's level | lines that do not express TNFSF10 (24) vs lines expressing it (26) | 2.85× lower at baseline in the lines without TNFSF10 | 0.014 | ⚠ within organs, on part of the lines; also absent: PLAAT4, TMEM92, LY75 |

### Downstream of this gene

*127 arrows, 127 of them with an alert ⚠; grade A 0, B 111, C 16. Shown: the 12 strongest; 115 more arrows (115 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS3]] | B | OAS2 activity raises OAS3's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.68× lower at baseline in the lines without OAS2 | 5e-05 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[HERC6]] | B | OAS2 activity raises HERC6's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.02× lower at baseline in the lines without OAS2 | 7e-05 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[DDX60L]] | B | OAS2 activity raises DDX60L's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.96× lower at baseline in the lines without OAS2 | 1e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[USP18]] | B | OAS2 activity raises USP18's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.89× lower at baseline in the lines without OAS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP10]] | B | OAS2 activity raises PARP10's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.00× lower at baseline in the lines without OAS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP9]] | B | OAS2 activity raises PARP9's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.16× lower at baseline in the lines without OAS2 | 2e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[HELZ2]] | B | OAS2 activity raises HELZ2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.69× lower at baseline in the lines without OAS2 | 3e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP14]] | B | OAS2 activity raises PARP14's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.56× lower at baseline in the lines without OAS2 | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[HERC6]] | B | OAS2 activity strengthens HERC6's drug response | lines that do not express OAS2 (9) vs lines expressing it (35) | the lines without OAS2 respond 0.40× as strongly (z diff +3.02); strongest at Panobinostat 5 µM: 0.38x vs 0.14x (z diff +3.7) | 4e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[MX2]] | B | OAS2 activity strengthens MX2's drug response | lines that do not express OAS2 (5) vs lines expressing it (28) | the lines without OAS2 respond 0.45× as strongly (z diff +4.40); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.65x vs 0.17x (z diff +7.3) | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[PLSCR1]] | B | OAS2 activity raises PLSCR1's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 3.39× lower at baseline in the lines without OAS2 | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[PARP10]] | B | OAS2 activity strengthens PARP10's drug response | lines that do not express OAS2 (13) vs lines expressing it (33) | the lines without OAS2 respond 0.24× as strongly (z diff +2.86); strongest at Auranofin 5 µM: 1.03x vs 0.39x (z diff +4.7) | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.963). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 53.8); signed map (64.8, 31.7). **Vector** length 159, 67.3% of its response variance represented; |z| ≥ 3 in 1,647 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.81 to 56); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.84 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.87 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +10.9 | +6.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +9.0 | +0.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.0 | +2.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.4 | +6.0 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.2 | +1.4 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.8 | +1.6 |
|  | [[Docetaxel (drug)]] 5 µM |  | +4.0 | +2.1 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +3.9 | +4.4 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -12.0 | -18.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.6 | -16.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -9.9 | -12.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.2 | -12.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -9.2 | -15.9 |

## What is on record

|  |  |
|---|---|
| Name | 2'-5'-oligoadenylate synthetase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q24.13 — chr12:112,978,395-113,011,723 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | 2'-5'-oligoadenylate synthetase family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 10 pathways, smallest: OAS antiviral response; IFIT antiviral response; Interferon alpha/beta signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [P29728](https://www.uniprot.org/uniprotkb/P29728) (2'-5'-oligoadenylate synthase 2):

> Interferon-induced, dsRNA-activated antiviral enzyme which plays a critical role in cellular innate antiviral response. Activated by detection of double stranded RNA (dsRNA): catalyzes the formation of 2'-5'-oligoadenylates (2-5A) from polymerization of ATP which then bind to the inactive monomeric form of ribonuclease L (RNASEL) leading to its dimerization and subsequent activation. Activation of RNASEL leads to degradation of cellular as well as viral RNA, resulting in the inhibition of …

**Summary**, from NCBI Gene [4939](https://www.ncbi.nlm.nih.gov/gene/4939):

> This gene encodes a member of the 2-5A synthetase family, essential proteins involved in the innate immune response to viral infection. The encoded protein is induced by interferons and uses adenosine triphosphate in 2'-specific nucleotidyl transfer reactions to synthesize 2',5'-oligoadenylates (2-5As). These molecules activate latent RNase L, which results in viral RNA degradation and the inhibition of viral replication. The three known members of this gene family are located in a cluster on …

**Accessions** — [HGNC:8087](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:8087) · Entrez [4939](https://www.ncbi.nlm.nih.gov/gene/4939) · UniProt [P29728](https://www.uniprot.org/uniprotkb/P29728) · Ensembl [ENSG00000111335](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000111335)

## Data

Gene col 3222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 3222); `tables/drug_effects.parquet` (74 rows, flagged included); `relations/gene_relations.parquet` (col_a == 3222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 3222]; `tensor/DDL_lfc|DDL_z.npy` [3222]; `embed/gene_vectors.npy` [3222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 3222 or target_col == 3222). Every well: [[OAS2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/OAS2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
