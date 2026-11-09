---
symbol: "MX2"
type: "gene"
col: 11408
ensembl_id: "ENSG00000183486"
name: "MX dynamin like GTPase 2"
location: "21q22.3"
module: 32
arm: "+"
pooled_cpm: 89.15
n_lines_expressing: 34
n_dd_up: 24
n_dd_down: 67
n_dd_up_clean: 24
n_dd_down_clean: 55
in_vector_space: true
direction_upstream: 54
direction_downstream: 46
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# MX2

*MX dynamin like GTPase 2* — 21q22.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.90× (z +5.4, q 4e-05, up in 26 of 31 measured lines).
> Pooled over the cell lines (median), lowered significantly by 67 drug-doses (12 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.140× (z -17.1, q 0e+00, down in 32 of 32 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[IFIT3]] (+0.92, fdr 7e-06), [[XAF1]] (+0.92, fdr 7e-06), [[RSAD2]] (+0.92, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 54 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 46 go from it, the strongest it → [[PLSCR1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 24 in all, none with an alert; shown: the 15 strongest. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11408.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.90×** | +5.4 | 4e-05 | 26/31 (AsPC-1, CFPAC-1, …) | rises with dose |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.64×** | +4.3 | 0.003 | 23/33 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.62×** | +4.2 | 0.003 | 27/32 (NCI-H1792, Panc 03.27, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.46×** | +4.2 | 0.003 | 23/32 (CFPAC-1, Hs 766T, …) | all doses, flat | noisy plate (z scaled) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.60×** | +4.1 | 0.005 | 22/31 (Hs 766T, CFPAC-1, …) | rises with dose |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.57×** | +3.9 | 0.007 | 21/32 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Omeprazole (drug)]] 0.05 µM |  | **1.58×** | +3.7 | 0.015 | 20/32 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.35×** | +3.7 | 0.015 | 18/32 (KATO III, AsPC-1, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | **1.36×** | +3.6 | 0.021 | 21/33 (CFPAC-1, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.52×** | +3.5 | 0.025 | 17/32 (AsPC-1, Hs 766T, …) | rises with dose |  |
| [[L-Eflornithine (monohydrochloride) (drug)]] 5 µM |  | **1.48×** | +3.4 | 0.033 | 21/32 (NCI-H2347, A-172, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.47×** | +3.4 | 0.036 | 16/32 (SW480, H4, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Apalutamide (drug)]] 0.5 µM |  | **1.46×** | +3.3 | 0.038 | 21/32 (NCI-H2347, Panc 03.27, …) | inconsistent across doses |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.49×** | +3.3 | 0.045 | 19/33 (LoVo, RKO, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.47×** | +3.2 | 0.052 | 18/32 (AsPC-1, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 67 in all, 12 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 67 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11408.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.140×** | -17.1 | 0e+00 | 32/32 (A-172, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.144×** | -16.9 | 0e+00 | 32/32 (A-172, HS-578T, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.155×** | -16.2 | 0e+00 | 32/32 (A-172, CHP-212, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.273×** | -15.9 | 0e+00 | 29/33 (CFPAC-1, LoVo, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **0.298×** | -14.9 | 0e+00 | 28/32 (LoVo, KATO III, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.348×** | -13.0 | 2e-36 | 28/33 (CFPAC-1, KATO III, …) | all doses, stronger at high dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.240×** | -12.4 | 2e-33 | 29/32 (LoVo, KATO III, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.254×** | -11.9 | 8e-31 | 31/33 (LoVo, A-172, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.257×** | -11.8 | 2e-30 | 29/32 (LoVo, AsPC-1, …) | rises with dose |  |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.275×** | -11.2 | 2e-27 | 29/33 (LoVo, RKO, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.268×** | -11.0 | 2e-26 | 29/31 (HS-578T, RKO, …) | rises with dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.319×** | -9.9 | 2e-21 | 30/32 (RKO, SHP-77, …) | rises with dose | cell-cycle shift (explains ~4% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.455×** | -9.7 | 2e-20 | 25/32 (RKO, SNU-423, …) | top dose only | cell-cycle shift (explains ~13% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.367×** | -8.1 | 2e-14 | 29/32 (A-172, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.392×** | -7.7 | 6e-13 | 26/32 (RKO, LoVo, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **0.440×** | -7.1 | 3e-11 | 23/32 (LoVo, SHP-77, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.19 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11408. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[RKO (line)]] | wt | 110 | 0 | 31 (8 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0194× (z -19.8) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Belinostat (drug)]] 0.5 µM 0.0226× (z -19.0) |
| [[LoVo (line)]] | wt | 170 | 0 | 25 (5 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0205× (z -22.0) |
| [[NCI-H1792 (line)]] | alt | 212 | 0 | 23 (6 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0518× (z -19.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.0685× (z -18.3) |
| [[SHP-77 (line)]] | alt | 98.4 | 0 | 20 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0933× (z -17.0) |
| [[A-172 (line)]] | wt | 484 | 0 | 19 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0386× (z -25.4) |
| [[SNU-423 (line)]] | alt | 128 | 0 | 19 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0536× (z -17.1) |
| [[HS-578T (line)]] | alt | 162 | 0 | 18 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0457× (z -20.2) |
| [[CFPAC-1 (line)]] | alt | 257 | 0 | 16 (5 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.0914× (z -20.1) |
| [[CHP-212 (line)]] | wt | 167 | 0 | 14 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.0124× (z -18.2) |
| [[KATO III (line)]] | alt | 130 | 0 | 14 (3 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.107× (z -18.1) |
| [[AsPC-1 (line)]] | alt | 99.8 | 0 | 12 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.0378× (z -14.6) |
| [[COLO 205 (line)]] | alt | 533 | 0 | 12 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.115× (z -16.9) |
| [[Panc 03.27 (line)]] | alt | 194 | 0 | 11 (1 ⚠) | — | [[Auranofin (drug)]] 5 µM 0.113× (z -12.8) |
| [[NCI-H2347 (line)]] | alt | 183 | 1 | 9 (1 ⚠) | [[Harringtonine (drug)]] 5 µM 3.88× (z +8.5) | [[Tofacitinib (drug)]] 5 µM 0.210× (z -14.4) |
| [[SW1417 (line)]] | alt | 176 | 0 | 10 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.0) |
| [[HepG2_C3A (line)]] | wt | 138 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -16.3) |
| [[Hs 766T (line)]] | wt | 69.0 | 0 | 8 | — | [[Selinexor (drug)]] 5 µM 0.123× (z -15.0) |
| [[RPMI-7951 (line)]] | alt | 280 | 0 | 8 (2 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.145× (z -15.9) |
| [[SK-MEL-2 (line)]] | alt | 51.9 | 0 | 8 | — | [[Tofacitinib (drug)]] 5 µM 0.186× (z -11.8) |
| [[A549 (line)]] | wt | 26.7 | 0 | 7 | — | [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.8) |
| [[J82 (line)]] | alt | 61.5 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 6.14× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | [[Tofacitinib (drug)]] 5 µM 0.281× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 34.1 | 0 | 4 | — | [[Selinexor (drug)]] 5 µM 0.198× (z -11.8) |
| [[SW 900 (line)]] | alt | 144 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.121× (z -13.7) |
| [[HT-29 (line)]] | alt | 37.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -11.9) |
| [[LOX-IMVI (line)]] | wt | 29.1 | 0 | 2 | — | [[Belinostat (drug)]] 5 µM 0.0669× (z -10.4) |
| [[PANC-1 (line)]] | alt | 42.4 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.442× (z -10.9) |
| [[H4 (line)]] | wt | 64.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0487× (z -15.0) ⚠ toxic |
| [[hTERT-HPNE (line)]] | wt | 44.8 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.207× (z -8.7) ⚠ toxic |
| [[A-427 (line)]] | wt | 4.95 n.m. | — | — | — | — |
| [[A498 (line)]] | wt | 18.0 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.3 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 40.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 20.5 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 12.0 n.m. | — | — | — | — |
| [[HCT15 (line)]] | alt | 16.3 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 6.58 n.m. | — | — | — | — |
| [[HOP62 (line)]] | alt | 28.2 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 20.2 n.m. | — | — | — | — |
| [[NCI-H1573 (line)]] | alt | 11.1 n.m. | — | — | — | — |
| [[NCI-H2030 (line)]] | alt | 5.72 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 68.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.71 n.m. | — | — | — | — |
| [[NCI-H460 (line)]] | wt | 6.51 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 62.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.58 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 89.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.23 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 8.26 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 28.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11408), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[IFIT3]] | +0.92 | +0.86 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 888 |
| [[XAF1]] | +0.92 | +0.85 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 869 |
| [[RSAD2]] | +0.92 | +0.87 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 963 |
| [[MX1]] | +0.92 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 979; ⚠ same locus (10.6 kb, same strand: neighbours can correlate without regulation) |
| [[OAS2]] | +0.91 | +0.84 / +0.94 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 948 |
| [[IFI44]] | +0.91 | +0.86 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 872 |
| [[EPSTI1]] | +0.91 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 667 |
| [[CMPK2]] | +0.90 | +0.80 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 758 |
| [[PARP9]] | +0.89 | +0.80 / +0.92 | both halves | 7e-06 | STRING 605 |
| [[SAMD9L]] | +0.89 | +0.82 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 636 |
| [[IFIT1]] | +0.89 | +0.81 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 961 |
| [[OAS1]] | +0.89 | +0.78 / +0.92 | both halves | 7e-06 | pathway: Antimicrobial mechanism of IFN-stimulated genes; STRING 918 |
| [[IFI35]] | +0.89 | +0.77 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 820 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*54 arrows, 54 of them with an alert ⚠; grade A 0, B 48, C 6. Shown: the 12 strongest; 42 more arrows (42 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity strengthens MX2's drug response | lines that do not express OAS2 (5) vs lines expressing it (28) | the lines without OAS2 respond 0.45× as strongly (z diff +4.40); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.65x vs 0.17x (z diff +7.3) | 5e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1; target measured in part of the lines; artifact flags |
| [[RSAD2]] | B | RSAD2 activity strengthens MX2's drug response | lines that do not express RSAD2 (6) vs lines expressing it (27) | the lines without RSAD2 respond 0.53× as strongly (z diff +3.79); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.53x vs 0.17x (z diff +6.8) | 0.002 | ⚠ within organs, on part of the lines; also absent: SH3TC1, IFI27, SRMS; target measured in part of the lines; artifact flags |
| [[NRIR]] | B | NRIR activity strengthens MX2's drug response | lines that do not express NRIR (9) vs lines expressing it (24) | the lines without NRIR respond 0.63× as strongly (z diff +3.24); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.47x vs 0.15x (z diff +6.0) | 0.003 | ⚠ within organs, on part of the lines; also absent: CMPK2, TSPAN7; target measured in part of the lines; artifact flags |
| [[BST2]] | B | BST2 activity raises MX2's level | lines that do not express BST2 (18) vs lines expressing it (32) | 4.43× lower at baseline in the lines without BST2 | 0.003 | ⚠ within organs, on part of the lines; also absent: CCDC194, DEPP1, SLC15A3 |
| [[MMP13]] | B | MMP13 activity raises MX2's level | lines that do not express MMP13 (30) vs lines expressing it (20) | 3.09× lower at baseline in the lines without MMP13 | 0.003 | ⚠ within organs, on part of the lines; also absent: SOX11, AGT, STEAP4 |
| [[OAS1]] | B | OAS1 activity strengthens MX2's drug response | lines that do not express OAS1 (6) vs lines expressing it (27) | the lines without OAS1 respond 0.49× as strongly (z diff +3.75); strongest at Selinexor 5 µM: 0.63x vs 0.25x (z diff +5.9) | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[MX1]] | B | MX1 activity raises MX2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 3.68× lower at baseline in the lines without MX1 | 0.004 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI6]] | B | IFI6 activity raises MX2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 5.15× lower at baseline in the lines without IFI6 | 0.004 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[SAMD9L]] | B | SAMD9L activity raises MX2's level | lines that do not express SAMD9L (18) vs lines expressing it (32) | 3.88× lower at baseline in the lines without SAMD9L | 0.005 | ⚠ within organs, on part of the lines; also absent: GBP4, CD5L, TRIM22 |
| [[IFI27]] | B | IFI27 activity raises MX2's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 4.04× lower at baseline in the lines without IFI27 | 0.006 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[EPSTI1]] | B | EPSTI1 activity raises MX2's level | lines that do not express EPSTI1 (25) vs lines expressing it (25) | 4.23× lower at baseline in the lines without EPSTI1 | 0.006 | ⚠ within organs, on part of the lines; also absent: UGT1A6, PKP1, ENSG00000271933 |
| [[TRIM22]] | B | TRIM22 activity raises MX2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 4.50× lower at baseline in the lines without TRIM22 | 0.006 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 41, C 5. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PLSCR1]] | B | MX2 activity raises PLSCR1's level | lines that do not express MX2 (16) vs lines expressing it (34) | 2.60× lower at baseline in the lines without MX2 | 0.011 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[TMEM140]] | B | MX2 activity raises TMEM140's level | lines that do not express MX2 (16) vs lines expressing it (34) | 2.31× lower at baseline in the lines without MX2 | 0.017 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[TNFSF10]] | B | MX2 activity raises TNFSF10's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.17× lower at baseline in the lines without MX2 | 0.018 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[OAS2]] | B | MX2 activity raises OAS2's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.27× lower at baseline in the lines without MX2 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[BST2]] | B | MX2 activity raises BST2's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.57× lower at baseline in the lines without MX2 | 0.024 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[MX1]] | B | MX2 activity raises MX1's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.04× lower at baseline in the lines without MX2 | 0.025 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[PML]] | B | MX2 activity raises PML's level | lines that do not express MX2 (16) vs lines expressing it (34) | 1.71× lower at baseline in the lines without MX2 | 0.030 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[IFI27]] | B | MX2 activity raises IFI27's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.69× lower at baseline in the lines without MX2 | 0.033 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[UBE2L6]] | B | MX2 activity strengthens UBE2L6's drug response | lines that do not express MX2 (12) vs lines expressing it (30) | the lines without MX2 respond 0.48× as strongly (z diff +2.04); strongest at Tofacitinib 5 µM: 0.72x vs 0.37x (z diff +2.7) | 0.033 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1; target measured in part of the lines; the reference differs; artifact flags |
| [[HELZ2]] | B | MX2 activity raises HELZ2's level | lines that do not express MX2 (16) vs lines expressing it (34) | 1.80× lower at baseline in the lines without MX2 | 0.036 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[CMPK2]] | B | MX2 activity raises CMPK2's level | lines that do not express MX2 (16) vs lines expressing it (34) | 2.18× lower at baseline in the lines without MX2 | 0.038 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |
| [[GBP1]] | B | MX2 activity raises GBP1's level | lines that do not express MX2 (16) vs lines expressing it (34) | 3.12× lower at baseline in the lines without MX2 | 0.039 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: NRP1, SLC15A3, DEPP1 |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.932). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.4, 53.4); signed map (64.6, 31.3). **Vector** length 144, 54.7% of its response variance represented; |z| ≥ 3 in 1,559 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon alpha response* (hallmark, mean cos +0.78 to 56); *Interferon gamma signaling* (reactome, mean cos +0.76 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.82 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +7.2 | +0.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +7.0 | +3.7 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.3 | +1.9 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +5.0 | +5.4 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.9 | +3.1 |
|  | [[Binimetinib (drug)]] 5 µM |  | +3.8 | +4.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.2 | +3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +3.2 | +3.1 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -9.7 | -15.9 |
|  | [[Selinexor (drug)]] 5 µM |  | -8.5 | -14.9 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -8.2 | -13.0 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -7.8 | -11.2 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -7.5 | -12.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -7.2 | -11.9 |

## What is on record

|  |  |
|---|---|
| Name | MX dynamin like GTPase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 21q22.3 — chr21:41,361,999-41,409,393 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MXB |
| Gene groups (HGNC) | MX dynamin like GTPase family |
| Hallmark sets | INTERFERON_GAMMA_RESPONSE |
| Reactome | 5 pathways, smallest: Interferon alpha/beta signaling; ISG15 antiviral mechanism; Antimicrobial mechanism of IFN-stimulated genes |
| Matched by | ensembl_id |

**Function**, from UniProt [P20592](https://www.uniprot.org/uniprotkb/P20592) (Interferon-induced GTP-binding protein Mx2):

> Interferon-induced dynamin-like GTPase with potent antiviral activity against human immunodeficiency virus type 1 (HIV-1). Acts by targeting the viral capsid and affects the nuclear uptake and/or stability of the HIV-1 replication complex and the subsequent chromosomal integration of the proviral DNA. Exhibits antiviral activity also against simian immunodeficiency virus (SIV-mnd). May play a role in regulating nucleocytoplasmic transport and cell-cycle progression.

**Summary**, from NCBI Gene [4600](https://www.ncbi.nlm.nih.gov/gene/4600):

> The protein encoded by this gene has a nuclear and a cytoplasmic form and is a member of both the dynamin family and the family of large GTPases. The nuclear form is localized in a granular pattern in the heterochromatin region beneath the nuclear envelope. A nuclear localization signal (NLS) is present at the amino terminal end of the nuclear form but is lacking in the cytoplasmic form due to use of an alternate translation start codon. This protein is upregulated by interferon-alpha but does …

**Accessions** — [HGNC:7533](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:7533) · Entrez [4600](https://www.ncbi.nlm.nih.gov/gene/4600) · UniProt [P20592](https://www.uniprot.org/uniprotkb/P20592) · Ensembl [ENSG00000183486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000183486)

## Data

Gene col 11408: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11408); `tables/drug_effects.parquet` (91 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11408, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11408]; `tensor/DDL_lfc|DDL_z.npy` [11408]; `embed/gene_vectors.npy` [11408]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11408 or target_col == 11408). Every well: [[MX2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MX2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
