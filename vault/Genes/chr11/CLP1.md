---
symbol: "CLP1"
type: "gene"
col: 10252
ensembl_id: "ENSG00000172409"
name: "cleavage factor polyribonucleotide kinase subunit 1"
location: "11q12.1"
module: 7
arm: "+"
pooled_cpm: 9.95
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 6
n_dd_up_clean: 9
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/007"]
generated_by: "tahoemap"
---

# CLP1

*cleavage factor polyribonucleotide kinase subunit 1* — 11q12.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (7 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.29× (z +16.8, q 0e+00, up in 38 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (5 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.728× (z -4.4, q 0.006, down in 14 of 18 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.755× (z -3.9, q 0.014, down in 14 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (J82 0.0572×, A-427 0.237×, HEC-1-A 0.270×, SNU-423 0.102×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.156×, J82 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.123×, NCI-H2030 0.176×; ⚠ toxic; transcription drop); [[Mifepristone (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0506×); [[Harringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.221×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (J82 0.136×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PRCC]] (+0.63, fdr 1e-05), [[MIR130AHG]] (+0.62, fdr 7e-06, ⚠ same locus), [[ZNF200]] (+0.62, fdr 1e-05), [[FASTKD5]] (+0.61, fdr 1e-05); moves opposite to [[TUBE1]] (-0.52, fdr 1e-04), [[HOOK1]] (-0.50, fdr 9e-05), [[EPB41]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 007]] (Dengue Virus-Host Interactions).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MIR130AHG]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 17 in all, 8 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10252.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.29×** | +16.8 | 0e+00 | 38/45 (SW480, A549, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.34×** | +11.7 | 3e-29 | 30/39 (NCI-H2347, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[TAK-901 (drug)]] 5 µM |  | **4.47×** | +11.2 | 4e-27 | 40/46 (SW480, PANC-1, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~5% here); composition shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.60×** | +9.5 | 3e-19 | 26/48 (HOP62, A-427, …) | top dose only |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.63×** | +7.0 | 3e-10 | 26/47 (SW480, LoVo, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~37% of this change | **1.60×** | +6.8 | 1e-09 | 27/47 (SW480, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.55×** | +6.3 | 3e-08 | 21/47 (NCI-H1792, NCI-H2347, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM |  | **1.34×** | +6.0 | 2e-07 | 23/47 (NCI-H2347, SW 900, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[PH-797804 (drug)]] 5 µM |  | **2.15×** | +5.8 | 6e-07 | 16/43 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.31×** | +5.4 | 4e-06 | 18/46 (NCI-H2030, C-33 A, …) | rises with dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.10× | +4.8 | 7e-05 | 6/48 (NCI-H23, RKO, …) | inconsistent across doses |  |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.40×** | +4.8 | 7e-05 | 14/45 (NCI-H460, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.38×** | +4.6 | 2e-04 | 15/45 (SW48, PANC-1, …) | top dose only |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **1.35×** | +4.1 | 0.001 | 16/44 (Panc 03.27, AN3 CA, …) | top dose only |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **1.33×** | +4.1 | 0.002 | 13/47 (A549, A-427, …) | all doses, stronger at high dose |  |
| [[Peretinoin (drug)]] 0.05 µM |  | **1.27×** | +3.1 | 0.062 | 2/46 (SW480, SW48) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 6 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10252.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 13 here, 4 with an alert ⚠; the 6 shown; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 4 lines (J82 0.0572×, A-427 0.237×, HEC-1-A 0.270×, SNU-423 0.102×; ⚠ toxic; transcription drop); [[Dinaciclib (drug)]] 0.05 µM in 2 lines (SW480 0.156×, J82 0.121×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change); [[Dinaciclib (drug)]] 5 µM in 2 lines (A498 0.123×, NCI-H2030 0.176×; ⚠ toxic; transcription drop); [[Mifepristone (drug)]] 0.05 µM in 1 line (RPMI-7951 0.0506×); [[Harringtonine (drug)]] 5 µM in 1 line (HEC-1-A 0.221×); [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM in 1 line (J82 0.136×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.728×** | -4.4 | 0.006 | 14/18 (A498, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.746×** | -4.1 | 0.012 | 10/39 (A-427, A549, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.755×** | -3.9 | 0.014 | 14/46 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Anethole trithione (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~5% of this change | **0.828×** | -3.9 | 0.014 | 5/47 (SW 1271, KATO III, …) | top dose only | position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.779×** | -3.6 | 0.032 | 17/33 (J82, A-427, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Pitavastatin (Calcium) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.781×** | -3.5 | 0.051 | 8/45 (NCI-H2030, CFPAC-1, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | 0.809× | -3.1 | 0.17 | 6/44 (SNU-1, H4, …) | inconsistent across doses |  |
| [[Radotinib (drug)]] 0.5 µM |  | 0.814× | -3.0 | 0.18 | 9/44 (SHP-77, HT-29, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.33 per unit of S-phase module lfc, -0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10252. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 29.8 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.221× (z -10.2) |
| [[J82 (line)]] | alt | 12.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0572× (z -15.6) ⚠ toxic; transcription drop · without an alert: [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.136× (z -10.0) |
| [[A-427 (line)]] | wt | 30.3 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.162× (z -12.5) ⚠ toxic |
| [[A498 (line)]] | wt | 5.92 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.123× (z -10.5) ⚠ toxic; transcription drop · without an alert: [[Tadalafil (drug)]] 5 µM 0.179× (z -8.6) |
| [[NCI-H2030 (line)]] | alt | 11.1 | 1 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.03× (z +11.3) | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.7) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 9.03 | 0 | 2 | — | [[Mifepristone (drug)]] 0.05 µM 0.0506× (z -11.5) |
| [[SW480 (line)]] | alt | 9.74 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.17× (z +11.4) | [[Dinaciclib (drug)]] 0.05 µM 0.156× (z -12.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[A549 (line)]] | wt | 11.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.27× (z +9.0) | — |
| [[C-33 A (line)]] | alt | 23.5 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.26× (z +9.7) | — |
| [[H4 (line)]] | wt | 12.9 | 0 | 1 | — | [[Apalutamide (drug)]] 0.05 µM 0.0540× (z -10.0) |
| [[LOX-IMVI (line)]] | wt | 21.0 | 0 | 1 | — | [[Cobimetinib (drug)]] 5 µM 0.197× (z -8.6) |
| [[NCI-H1573 (line)]] | alt | 6.93 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.86× (z +8.9) | — |
| [[NCI-H2347 (line)]] | alt | 6.28 | 1 (1 ⚠) | 0 | [[Topotecan (hydrochloride) (drug)]] 5 µM 5.72× (z +9.4) ⚠ toxic | — |
| [[NCI-H460 (line)]] | wt | 5.52 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.46× (z +9.3) | — |
| [[SNU-1 (line)]] | wt | 14.5 | 0 | 1 | — | [[Roxadustat (drug)]] 0.05 µM 0.0831× (z -8.8) |
| [[SNU-423 (line)]] | alt | 6.02 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -9.1) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 12.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.39 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.73 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 8.70 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 10.5 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 6.17 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.66 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 9.96 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 5.18 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 6.58 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 5.64 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 8.14 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 7.62 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 4.54 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.07 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.75 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.89 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 8.37 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.87 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.55 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.96 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.77 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.63 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.81 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10252), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRCC]] | +0.63 | +0.53 / +0.54 | both halves | 1e-05 | pathway: Dengue Virus-Host Interactions |
| [[MIR130AHG]] | +0.62 | +0.59 / +0.59 | both halves | 7e-06 | ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[ZNF200]] | +0.62 | +0.54 / +0.61 | both halves | 1e-05 |  |
| [[FASTKD5]] | +0.61 | +0.51 / +0.58 | both halves | 1e-05 |  |
| [[SMG8]] | +0.59 | +0.56 / +0.53 | both halves | 1e-05 |  |
| [[TRMT10C]] | +0.59 | +0.57 / +0.58 | both halves | 1e-05 | pathway: tRNA processing; STRING 555 |
| [[MRM2]] | +0.57 | +0.63 / +0.50 | both halves | 1e-05 |  |
| [[ZNF26]] | +0.57 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[CCNT1]] | +0.57 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[YRDC]] | +0.56 | +0.56 / +0.58 | both halves | 1e-05 | pathway: tRNA processing |
| [[POLR1C]] | +0.56 | +0.44 / +0.56 | both halves | 3e-05 | pathway: HALLMARK_DNA_REPAIR |
| [[TMEM115]] | +0.55 | +0.43 / +0.56 | both halves | 3e-05 |  |
| [[ZNF614]] | +0.55 | +0.59 / +0.49 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TUBE1]] | -0.52 | -0.58 / -0.33 | both halves | 1e-04 |  |
| [[HOOK1]] | -0.50 | -0.36 / -0.49 | both halves | 9e-05 |  |
| [[EPB41]] | -0.50 | -0.43 / -0.53 | both halves | 3e-05 |  |
| [[UBE2Q2P2]] | -0.49 | -0.52 / -0.36 | both halves | 1e-04 |  |
| [[CAT]] | -0.49 | -0.47 / -0.39 | both halves | 6e-05 |  |
| [[MPP1]] | -0.47 | -0.33 / -0.46 | both halves | 1e-04 |  |
| [[KIF16B]] | -0.47 | -0.43 / -0.44 | both halves | 4e-05 |  |
| [[FAM102A]] | -0.47 | -0.45 / -0.43 | both halves | 3e-05 |  |
| [[TPMT]] | -0.46 | -0.38 / -0.46 | both halves | 6e-05 |  |
| [[HMGN3]] | -0.46 | -0.35 / -0.36 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 1, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MIR130AHG]] | B | MIR130AHG activity raises CLP1's level | lines that do not express MIR130AHG (14) vs lines expressing it (36) | 1.54× lower at baseline in the lines without MIR130AHG | 0.040 | ⚠ within organs, on part of the lines; co-occurs with APC; also absent: SPART, RAB34, PYGO1 |
| [[FAM102A]] | C | FAM102A activity lowers CLP1's level | lines that do not express FAM102A (3) vs lines expressing it (47) | 2.16× higher at baseline in the lines without FAM102A | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: MBNL2, NINJ1, RPS6KA2; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 007]] — Dengue Virus-Host Interactions; 235 genes; this gene is in the **+** arm (projection on the module's main direction 0.543). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.22).
- **Nodal map** (x, y) = (-41.1, 3.2); signed map (-7.4, -26.8). **Vector** length 75.1, 12.6% of its response variance represented; |z| ≥ 3 in 963 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +6.0 | +11.2 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +5.5 | +16.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +4.5 | +5.8 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | +9.5 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.1 | +11.7 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | +2.5 | +2.2 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.2 | +1.8 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +1.3 | +1.9 |
| fall | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.1 | -3.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -3.4 | -4.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -3.2 | -1.7 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.2 | -4.1 |
|  | [[Harringtonine (drug)]] 5 µM |  | -2.3 | -3.9 |
|  | [[Ponatinib (drug)]] 5 µM |  | -1.9 | -2.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.9 | -1.5 |
|  | [[Radotinib (drug)]] 5 µM |  | -1.8 | -3.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.7 | -2.2 |

## What is on record

|  |  |
|---|---|
| Name | cleavage factor polyribonucleotide kinase subunit 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q12.1 — chr11:57,648,188-57,661,865 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HEAB, hClp1 |
| Gene groups (HGNC) | RNA kinases |
| Hallmark sets | DNA_REPAIR |
| Reactome | 12 pathways, smallest: Processing of Intronless Pre-mRNAs; Processing of Capped Intronless Pre-mRNA; RNA Polymerase II Transcription Termination |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92989](https://www.uniprot.org/uniprotkb/Q92989) (Polyribonucleotide 5'-hydroxyl-kinase Clp1):

> Polynucleotide kinase that can phosphorylate the 5'-hydroxyl groups of double-stranded RNA (dsRNA), single-stranded RNA (ssRNA), double-stranded DNA (dsDNA) and double-stranded DNA:RNA hybrids. dsRNA is phosphorylated more efficiently than dsDNA, and the RNA component of a DNA:RNA hybrid is phosphorylated more efficiently than the DNA component. Plays a key role in both tRNA splicing and mRNA 3'-end formation. Component of the tRNA splicing endonuclease complex: phosphorylates the 5'-terminus …

**Summary**, from NCBI Gene [10978](https://www.ncbi.nlm.nih.gov/gene/10978):

> This gene encodes a member of the Clp1 family. The encoded protein is a multifunctional kinase which is a component of the tRNA splicing endonuclease complex and a component of the pre-mRNA cleavage complex II. This protein is implicated in tRNA, mRNA, and siRNA maturation. Mutations in this gene are associated with pontocerebellar hypoplasia type 10 (PCH10). Alternatively splice transcript variants encoding different isoforms have been found for this gene. [provided by RefSeq, Sep 2014]

**Accessions** — [HGNC:16999](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16999) · Entrez [10978](https://www.ncbi.nlm.nih.gov/gene/10978) · UniProt [Q92989](https://www.uniprot.org/uniprotkb/Q92989) · Ensembl [ENSG00000172409](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000172409)

## Data

Gene col 10252: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10252); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10252, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10252]; `tensor/DDL_lfc|DDL_z.npy` [10252]; `embed/gene_vectors.npy` [10252]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10252 or target_col == 10252). Every well: [[CLP1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CLP1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
