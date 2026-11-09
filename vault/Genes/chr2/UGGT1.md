---
symbol: "UGGT1"
type: "gene"
col: 5896
ensembl_id: "ENSG00000136731"
name: "UDP-glucose glycoprotein glucosyltransferase 1"
location: "2q14.3"
module: 20
arm: "+"
pooled_cpm: 92.3
n_lines_expressing: 50
n_dd_up: 19
n_dd_down: 2
n_dd_up_clean: 6
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# UGGT1

*UDP-glucose glycoprotein glucosyltransferase 1* — 2q14.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 19 drug-doses (13 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 2.36× (z +17.0, q 0e+00, up in 42 of 44 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.37× (z +9.3, q 1e-18, up in 42 of 49 measured lines).
> Pooled over the cell lines (median), lowered significantly by 2 drug-doses (none with an alert); the strongest is [[Verteporfin (drug)]] 5 µM: 0.777× (z -5.1, q 2e-04, down in 26 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.434×, hTERT-HPNE 0.434×, SK-MEL-2 0.510×, A498 0.671×; ⚠ cell-cycle shift, explains ~43% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0936×); [[Harringtonine (drug)]] 5 µM in 1 line (J82 0.470×; ⚠ cell-cycle shift, explains ~0% of this change); [[Fenofibrate (drug)]] 0.5 µM in 1 line (SW 1088 0.0658×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.121×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TXNDC5]] (+0.76, fdr 7e-06), [[RPN1]] (+0.75, fdr 7e-06), [[DNAJB11]] (+0.74, fdr 7e-06); moves opposite to [[ACAP1]] (-0.65, fdr 1e-05), [[SNHG9]] (-0.65, fdr 9e-06), [[SNHG8]] (-0.64, fdr 1e-05).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 17 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 19 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 13 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5896.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **2.36×** | +17.0 | 0e+00 | 42/44 (NCI-H1792, LOX-IMVI, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **2.26×** | +16.8 | 0e+00 | 48/49 (PANC-1, NCI-H1792, …) | all doses, stronger at high dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.93×** | +13.5 | 3e-39 | 47/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.72×** | +11.1 | 1e-26 | 43/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **1.71×** | +11.0 | 4e-26 | 43/48 (A549, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **1.71×** | +10.2 | 2e-22 | 34/45 (SK-MEL-2, SNU-423, …) | all doses, stronger at high dose | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **2.37×** | +9.3 | 1e-18 | 42/49 (SW480, Panc 03.27, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.22×** | +8.6 | 7e-16 | 40/48 (SW480, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.31×** | +5.6 | 1e-06 | 31/48 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~65% of this change | **1.29×** | +5.1 | 2e-05 | 29/48 (SNU-423, LOX-IMVI, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.27×** | +4.9 | 4e-05 | 26/48 (LOX-IMVI, NCI-H23, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.27×** | +4.8 | 1e-04 | 30/48 (NCI-H1792, SW480, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **1.25×** | +4.6 | 2e-04 | 25/48 (LOX-IMVI, SK-MEL-2, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~35% of this change | **1.25×** | +4.4 | 5e-04 | 23/47 (SNU-423, CFPAC-1, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.24×** | +4.3 | 6e-04 | 23/48 (SW480, A549, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.22×** | +3.8 | 0.005 | 22/48 (NCI-H23, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.009 | 20/48 (LOX-IMVI, NCI-H1792, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 5 µM |  | 1.18× | +3.4 | 0.020 | 13/48 (NCI-H1573, NCI-H23, …) | top dose only |  |
| [[Brivudine (drug)]] 5 µM |  | **1.35×** | +3.2 | 0.034 | 16/49 (AsPC-1, CFPAC-1, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.11× | +3.0 | 0.054 | 15/48 (A-172, CFPAC-1, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 2 with an alert ⚠. 2 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 5896.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 8 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (J82 0.434×, hTERT-HPNE 0.434×, SK-MEL-2 0.510×, A498 0.671×; ⚠ cell-cycle shift, explains ~43% of this change); [[Pyridoxine (drug)]] 0.5 µM in 1 line (SW 1271 0.0936×); [[Harringtonine (drug)]] 5 µM in 1 line (J82 0.470×; ⚠ cell-cycle shift, explains ~0% of this change); [[Fenofibrate (drug)]] 0.5 µM in 1 line (SW 1088 0.0658×); [[Glycyrrhizic acid (drug)]] 0.05 µM in 1 line (CHP-212 0.121×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Verteporfin (drug)]] 5 µM |  | **0.777×** | -5.1 | 2e-04 | 26/49 (HOP62, Hs 766T, …) | top dose only |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 0.877× | -3.9 | 0.028 | 17/48 (HEC-1-A, H4, …) | inconsistent across doses | low cells (technical?) |
| [[9-ING-41 (drug)]] 0.5 µM |  | **0.777×** | -3.7 | 0.034 | 27/48 (H4, J82, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | 0.886× | -3.6 | 0.046 | 20/48 (J82, hTERT-HPNE, …) | top dose only | composition shift |
| [[Vilanterol (drug)]] 0.5 µM |  | 0.847× | -3.5 | 0.057 | 14/48 (SK-MEL-2, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.42 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5896. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 92.1 | 8 (6 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.50× (z +14.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[TAK-901 (drug)]] 5 µM 3.37× (z +10.1) | — |
| [[LOX-IMVI (line)]] | wt | 78.3 | 6 (6 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.73× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[A549 (line)]] | wt | 78.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.50× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[AsPC-1 (line)]] | alt | 51.6 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.65× (z +11.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[CFPAC-1 (line)]] | alt | 62.7 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.91× (z +13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[MIA PaCa-2 (line)]] | alt | 76.6 | 5 (5 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.13× (z +11.1) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[SNU-423 (line)]] | alt | 51.8 | 5 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.48× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[HOP62 (line)]] | alt | 110 | 3 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.34× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | [[Verteporfin (drug)]] 5 µM 0.449× (z -8.6) |
| [[A-427 (line)]] | wt | 100 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.44× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1792 (line)]] | alt | 76.0 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.49× (z +16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[NCI-H460 (line)]] | wt | 125 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.16× (z +12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[PANC-1 (line)]] | alt | 108 | 3 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.96× (z +14.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A-172 (line)]] | wt | 100 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.76× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[C-33 A (line)]] | alt | 77.4 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.95× (z +12.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[C32 (line)]] | wt | 68.1 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.53× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[CHP-212 (line)]] | wt | 62.2 | 0 | 2 | — | [[Glycyrrhizic acid (drug)]] 0.05 µM 0.121× (z -9.2) |
| [[HEC-1-A (line)]] | alt | 119 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.30× (z +9.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HS-578T (line)]] | alt | 83.8 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.57× (z +10.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[hTERT-HPNE (line)]] | wt | 101 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 2.49× (z +8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -11.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[J82 (line)]] | alt | 125 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.434× (z -15.9) ⚠ cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 65.6 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +10.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H2030 (line)]] | alt | 111 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 100 | 2 (2 ⚠) | 0 | [[Panobinostat (drug)]] 5 µM 2.14× (z +9.3) ⚠ cell-cycle shift, explains ~38% of this change | — |
| [[NCI-H2347 (line)]] | alt | 56.7 | 2 (2 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 1.82× (z +9.9) ⚠ cell-cycle shift, explains ~73% of this change | — |
| [[Panc 03.27 (line)]] | alt | 69.9 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.69× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SK-MEL-2 (line)]] | alt | 86.9 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.05 µM 2.76× (z +10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | [[Homoharringtonine (drug)]] 5 µM 0.510× (z -11.1) ⚠ cell-cycle shift, explains ~43% of this change |
| [[SNU-1 (line)]] | wt | 68.2 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.63× (z +9.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[SW 1088 (line)]] | alt | 101 | 0 | 2 | — | [[Fenofibrate (drug)]] 0.5 µM 0.0658× (z -9.5) |
| [[SW 900 (line)]] | alt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.30× (z +9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[A498 (line)]] | wt | 141 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 1.86× (z +10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[AN3 CA (line)]] | alt | 124 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 3.98× (z +9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[HCT15 (line)]] | alt | 79.5 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.20× (z +10.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[LoVo (line)]] | wt | 87.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 2.49× (z +10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[LS 180 (line)]] | wt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.41× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H1573 (line)]] | alt | 50.3 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 5 µM 4.40× (z +12.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | — |
| [[RKO (line)]] | wt | 96.6 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.37× (z +10.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SHP-77 (line)]] | alt | 107 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.21× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[SW 1271 (line)]] | alt | 108 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.0936× (z -11.3) |
| [[BT-474 (line)]] | alt | 70.8 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 86.4 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 108 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 118 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 54.5 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 92.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 71.1 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 79.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 137 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 103 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 98.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 65.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5896), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*73 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TXNDC5]] | +0.76 | +0.65 / +0.82 | both halves | 7e-06 | STRING 598 |
| [[RPN1]] | +0.75 | +0.64 / +0.81 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 657 |
| [[DNAJB11]] | +0.74 | +0.71 / +0.72 | both halves | 7e-06 | STRING 746 |
| [[EMC1]] | +0.73 | +0.68 / +0.73 | both halves | 7e-06 | STRING 470 |
| [[BPNT2]] | +0.71 | +0.62 / +0.72 | both halves | 7e-06 |  |
| [[STT3A]] | +0.71 | +0.58 / +0.74 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation; STRING 738 |
| [[TMED7]] | +0.70 | +0.60 / +0.69 | both halves | 7e-06 | pathway: Asparagine N-linked glycosylation |
| [[PRKDC]] | +0.69 | +0.62 / +0.70 | both halves | 7e-06 |  |
| [[PIGK]] | +0.68 | +0.57 / +0.72 | both halves | 9e-06 |  |
| [[IPO5]] | +0.68 | +0.53 / +0.76 | both halves | 1e-05 |  |
| [[DNAJC10]] | +0.68 | +0.58 / +0.72 | both halves | 7e-06 | STRING 728 |
| [[MACROH2A1]] | +0.68 | +0.55 / +0.73 | both halves | 1e-05 |  |

## Genes that move opposite

*27 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ACAP1]] | -0.65 | -0.53 / -0.70 | both halves | 1e-05 |  |
| [[SNHG9]] | -0.65 | -0.57 / -0.67 | both halves | 9e-06 |  |
| [[SNHG8]] | -0.64 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[SMIM26]] ⚠ | -0.64 | -0.49 / -0.72 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[MRPL32]] | -0.63 | -0.35 / -0.74 | both halves | 1e-04 |  |
| [[CROCCP2-1]] | -0.63 | -0.54 / -0.66 | both halves | 1e-05 |  |
| [[POLR1H]] | -0.63 | -0.43 / -0.68 | both halves | 3e-05 |  |
| [[EIF1B]] | -0.62 | -0.49 / -0.68 | both halves | 1e-05 |  |
| [[ARRDC2]] | -0.62 | -0.49 / -0.58 | both halves | 1e-05 |  |
| [[TMEM265]] | -0.62 | -0.48 / -0.58 | both halves | 2e-05 |  |
| [[PIM3]] | -0.61 | -0.49 / -0.64 | both halves | 1e-05 |  |
| [[SIRT6]] | -0.60 | -0.47 / -0.66 | both halves | 2e-05 |  |
| [[INAFM1]] | -0.60 | -0.57 / -0.66 | both halves | 1e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.755). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-24.2, -23.0); signed map (-24.1, -39.8). **Vector** length 128, 39.4% of its response variance represented; |z| ≥ 3 in 1,070 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Maturation of DENV proteins* (reactome, mean cos +0.56 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +7.4 | +17.0 |
|  | [[TAK-901 (drug)]] 5 µM |  | +7.2 | +9.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | +7.1 | +16.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | +6.6 | +8.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | +6.3 | +10.2 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.0 | +4.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +2.7 | +1.9 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | +2.6 | +3.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | +2.4 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | -8.4 | -3.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -5.6 | -0.3 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.8 | -3.9 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.6 | -2.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | -4.4 | +0.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.2 | -2.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -3.6 | -2.7 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -2.7 | -3.7 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.7 | -5.1 |
|  | [[Osimertinib (mesylate) (drug)]] 5 µM |  | -2.7 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | UDP-glucose glycoprotein glucosyltransferase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q14.3 — chr2:128,091,200-128,195,677 (+) |
| Ensembl biotype | protein_coding |
| Also known as | HUGT1; previously UGCGL1 |
| Gene groups (HGNC) | UDP-glucose glycoprotein glucosyltransferases |
| Reactome | 4 pathways, smallest: ER Quality Control Compartment (ERQC); Calnexin/calreticulin cycle; N-glycan trimming in the ER and Calnexin/Calreticulin cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9NYU2](https://www.uniprot.org/uniprotkb/Q9NYU2) (UDP-glucose:glycoprotein glucosyltransferase 1):

> Recognizes glycoproteins with minor folding defects. Reglucosylates single N-glycans near the misfolded part of the protein, thus providing quality control for protein folding in the endoplasmic reticulum. Reglucosylated proteins are recognized by calreticulin for recycling to the endoplasmic reticulum and refolding or degradation.

**Summary**, from NCBI Gene [56886](https://www.ncbi.nlm.nih.gov/gene/56886):

> UDP-glucose:glycoprotein glucosyltransferase (UGT) is a soluble protein of the endoplasmic reticulum (ER) that selectively reglucosylates unfolded glycoproteins, thus providing quality control for protein transport out of the ER.[supplied by OMIM, Oct 2009]

**Accessions** — [HGNC:15663](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:15663) · Entrez [56886](https://www.ncbi.nlm.nih.gov/gene/56886) · UniProt [Q9NYU2](https://www.uniprot.org/uniprotkb/Q9NYU2) · Ensembl [ENSG00000136731](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000136731)

## Data

Gene col 5896: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5896); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5896, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5896]; `tensor/DDL_lfc|DDL_z.npy` [5896]; `embed/gene_vectors.npy` [5896]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5896 or target_col == 5896). Every well: [[UGGT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/UGGT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
