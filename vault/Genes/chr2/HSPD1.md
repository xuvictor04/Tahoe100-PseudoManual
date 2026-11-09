---
symbol: "HSPD1"
type: "gene"
col: 6873
ensembl_id: "ENSG00000144381"
name: "heat shock protein family D (Hsp60) member 1"
location: "2q33.1"
module: 60
arm: "+"
pooled_cpm: 475.95
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 1
n_dd_up_clean: 15
n_dd_down_clean: 1
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSPD1

*heat shock protein family D (Hsp60) member 1* — 2q33.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (11 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 5.57× (z +18.6, q 0e+00, up in 48 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 1 drug-dose (none with an alert); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.740× (z -4.6, q 0.002, down in 28 of 48 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (A-427 0.315×, C-33 A 0.234×, NCI-H23 0.313×, SNU-1 0.349×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.383×; ⚠ cell-cycle shift, would explain all of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AB1]] (+0.86, fdr 7e-06), [[CCT4]] (+0.85, fdr 7e-06), [[CCT3]] (+0.84, fdr 7e-06); moves opposite to [[TNRC6C]] (-0.64, fdr 1e-05), [[CHKB]] (-0.59, fdr 1e-05), [[H2AJ]] (-0.58, fdr 1e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HLA-A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 11 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6873.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **5.57×** | +18.6 | 0e+00 | 48/48 (SW1417, KATO III, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **5.44×** | +18.3 | 0e+00 | 48/48 (BT-474, A-172, …) | top dose only | position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **4.59×** | +16.5 | 0e+00 | 48/48 (SW1417, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | **4.57×** | +16.4 | 0e+00 | 49/49 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **4.69×** | +15.8 | 0e+00 | 48/48 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **4.19×** | +14.9 | 0e+00 | 44/44 (SW 900, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.95×** | +10.8 | 2e-25 | 45/45 (MIA PaCa-2, J82, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here); composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **6.68×** | +10.7 | 5e-25 | 44/45 (SW1417, KATO III, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **3.39×** | +9.4 | 3e-19 | 48/49 (SW1417, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **2.00×** | +7.2 | 3e-11 | 45/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **3.28×** | +6.7 | 1e-09 | 47/47 (KATO III, SW1417, …) | inconsistent across doses | cell-cycle shift (explains ~20% here); noisy plate (z scaled) |
| [[Infigratinib (drug)]] 5 µM |  | **2.57×** | +5.3 | 5e-06 | 45/48 (AsPC-1, BT-474, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **2.28×** | +4.7 | 1e-04 | 47/48 (HT-29, MIA PaCa-2, …) | rises with dose | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.54×** | +4.7 | 1e-04 | 41/48 (CFPAC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Darinaparsin (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.29×** | +3.9 | 0.003 | 45/48 (RPMI-7951, MIA PaCa-2, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **1.87×** | +3.6 | 0.014 | 42/48 (CFPAC-1, Panc 03.27, …) | inconsistent across doses | noisy plate (z scaled) |
| [[NG25 (drug)]] 0.05 µM |  | **1.40×** | +3.4 | 0.020 | 38/49 (KATO III, HEC-1-A, …) | inconsistent across doses |  |
| [[Belumosudil (drug)]] 5 µM |  | **1.36×** | +3.2 | 0.042 | 32/48 (C32, NCI-H1792, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **1.72×** | +3.1 | 0.053 | 34/48 (CFPAC-1, MIA PaCa-2, …) | all doses, flat | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **1.34×** | +3.0 | 0.058 | 30/48 (HS-578T, A549, …) | top dose only |  |
| [[venetoclax (drug)]] 5 µM |  | **1.68×** | +2.9 | 0.074 | 31/48 (CFPAC-1, AsPC-1, …) | top dose only | noisy plate (z scaled); position effect removed |
| [[TAK-733 (drug)]] 5 µM |  | **1.66×** | +2.9 | 0.087 | 28/48 (NCI-H1573, CFPAC-1, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 1 of them lowers it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6873.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 2 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 15 lines (A-427 0.315×, C-33 A 0.234×, NCI-H23 0.313×, SNU-1 0.349×, …); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.383×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.740×** | -4.6 | 0.002 | 28/48 (A-427, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.32 per unit of S-phase module lfc, +0.39 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6873. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 457 | 10 (4 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 7.40× (z +22.8) | [[Homoharringtonine (drug)]] 5 µM 0.477× (z -11.8) |
| [[A-172 (line)]] | wt | 249 | 11 (6 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 14.3× (z +25.7) | — |
| [[CFPAC-1 (line)]] | alt | 297 | 11 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.4× (z +20.7) | — |
| [[C32 (line)]] | wt | 207 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 21.0× (z +25.4) | — |
| [[HepG2_C3A (line)]] | wt | 778 | 9 (5 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.34× (z +15.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.51× (z +13.0) | [[Homoharringtonine (drug)]] 5 µM 0.530× (z -9.1) |
| [[MIA PaCa-2 (line)]] | alt | 514 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.22× (z +18.4) | — |
| [[NCI-H2347 (line)]] | alt | 308 | 10 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.19× (z +18.6) | — |
| [[SW 900 (line)]] | alt | 284 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.17× (z +19.7) | — |
| [[A498 (line)]] | wt | 595 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.68× (z +17.6) | — |
| [[AsPC-1 (line)]] | alt | 336 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.85× (z +18.1) | — |
| [[HOP62 (line)]] | alt | 357 | 9 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.37× (z +18.4) | — |
| [[HS-578T (line)]] | alt | 287 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.85× (z +19.8) | — |
| [[HT-29 (line)]] | alt | 536 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 7.42× (z +20.8) | — |
| [[Panc 03.27 (line)]] | alt | 286 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.06× (z +20.0) | — |
| [[SW1417 (line)]] | alt | 522 | 9 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.32× (z +25.7) | — |
| [[Hs 766T (line)]] | wt | 303 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.31× (z +15.5) | — |
| [[hTERT-HPNE (line)]] | wt | 228 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.22× (z +15.8) | — |
| [[J82 (line)]] | alt | 465 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.92× (z +19.0) | — |
| [[LS 180 (line)]] | wt | 812 | 6 (3 ⚠) | 2 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 5.00× (z +14.3) | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -10.3) |
| [[NCI-H1573 (line)]] | alt | 229 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.04× (z +18.1) | — |
| [[RKO (line)]] | wt | 714 | 5 (1 ⚠) | 3 (2 ⚠) | [[Auranofin (drug)]] 5 µM 4.74× (z +13.8) | [[Homoharringtonine (drug)]] 5 µM 0.399× (z -11.6) |
| [[RPMI-7951 (line)]] | alt | 251 | 8 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.64× (z +17.6) | — |
| [[SW480 (line)]] | alt | 679 | 7 (3 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 6.27× (z +16.6) | [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.7) |
| [[A-427 (line)]] | wt | 751 | 5 (2 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.19× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -16.9) |
| [[HEC-1-A (line)]] | alt | 400 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 8.50× (z +22.7) | — |
| [[LoVo (line)]] | wt | 816 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Bortezomib (drug)]] 0.05 µM 4.46× (z +13.0) | — |
| [[LOX-IMVI (line)]] | wt | 404 | 6 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 7.20× (z +17.0) | [[Homoharringtonine (drug)]] 5 µM 0.423× (z -10.6) |
| [[NCI-H2030 (line)]] | alt | 351 | 7 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.32× (z +13.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.21× (z +13.4) | — |
| [[SK-MEL-2 (line)]] | alt | 358 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.37× (z +17.1) | — |
| [[SNU-1 (line)]] | wt | 615 | 6 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 5.45× (z +16.1) | [[Homoharringtonine (drug)]] 5 µM 0.349× (z -14.3) |
| [[SNU-423 (line)]] | alt | 301 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 8.99× (z +16.7) | — |
| [[A549 (line)]] | wt | 494 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 7.38× (z +16.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 4.64× (z +12.6) | — |
| [[BT-474 (line)]] | alt | 388 | 5 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 14.5× (z +26.1) | [[Homoharringtonine (drug)]] 5 µM 0.457× (z -10.7) |
| [[CHP-212 (line)]] | wt | 473 | 5 (1 ⚠) | 1 | [[Ixazomib citrate (drug)]] 5 µM 5.29× (z +14.9) | [[Homoharringtonine (drug)]] 5 µM 0.408× (z -11.2) |
| [[COLO 205 (line)]] | alt | 166 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 10.5× (z +16.6) | — |
| [[H4 (line)]] | wt | 392 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.10× (z +14.0) | — |
| [[PANC-1 (line)]] | alt | 513 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.28× (z +15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.42× (z +12.8) | — |
| [[SW48 (line)]] | wt | 792 | 5 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.31× (z +11.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 2.86× (z +9.9) | [[Homoharringtonine (drug)]] 5 µM 0.439× (z -10.8) |
| [[HCT15 (line)]] | alt | 517 | 4 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 5.00× (z +13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +10.1) | [[Homoharringtonine (drug)]] 5 µM 0.417× (z -10.3) |
| [[SHP-77 (line)]] | alt | 522 | 4 (3 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 4.49× (z +14.7) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Auranofin (drug)]] 5 µM 4.22× (z +14.7) | [[Homoharringtonine (drug)]] 5 µM 0.448× (z -11.5) |
| [[SW 1088 (line)]] | alt | 220 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 14.0× (z +12.5) | — |
| [[AN3 CA (line)]] | alt | 428 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.84× (z +14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 5.80× (z +14.6) | — |
| [[C-33 A (line)]] | alt | 653 | 2 (1 ⚠) | 2 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.15× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.234× (z -16.6) |
| [[NCI-H1792 (line)]] | alt | 264 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 10.1× (z +15.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change | — |
| [[NCI-H23 (line)]] | alt | 576 | 3 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 3.72× (z +12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Auranofin (drug)]] 5 µM 3.06× (z +10.4) | [[Homoharringtonine (drug)]] 5 µM 0.313× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 784 | 4 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.93× (z +15.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.86× (z +9.2) | — |
| [[SW 1271 (line)]] | alt | 227 | 4 | 0 | [[Auranofin (drug)]] 5 µM 11.6× (z +13.0) | — |
| [[NCI-H661 (line)]] | alt | 1,018 | 3 | 0 | [[Bortezomib (drug)]] 0.05 µM 4.48× (z +9.3) | — |
| [[NCI-H2122 (line)]] | alt | 341 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 459 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6873), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB1]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 970 |
| [[CCT4]] | +0.85 | +0.83 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 623 |
| [[CCT3]] | +0.84 | +0.83 / +0.83 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 755 |
| [[PTGES3]] | +0.80 | +0.79 / +0.77 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 491 |
| [[HSP90AB3P]] | +0.79 | +0.79 / +0.70 | both halves | 7e-06 | **novel candidate** |
| [[CACYBP]] | +0.79 | +0.78 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 436 |
| [[HSP90AA1]] | +0.78 | +0.75 / +0.79 | both halves | 7e-06 | STRING 963 |
| [[HSP90AB2P]] | +0.76 | +0.77 / +0.68 | both halves | 7e-06 | **novel candidate** |
| [[HSPA8]] | +0.76 | +0.76 / +0.74 | both halves | 7e-06 | STRING 933 |
| [[CCT6A]] | +0.75 | +0.71 / +0.79 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 871 |
| [[HSPE1]] | +0.72 | +0.76 / +0.70 | both halves | 7e-06 | same gene group; pathway: HALLMARK_MTORC1_SIGNALING; STRING 999; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[TCP1]] | +0.72 | +0.74 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 958 |
| [[CCT5]] | +0.72 | +0.78 / +0.67 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 588 |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TNRC6C]] | -0.64 | -0.66 / -0.53 | both halves | 1e-05 |  |
| [[CHKB]] | -0.59 | -0.54 / -0.52 | both halves | 1e-05 |  |
| [[H2AJ]] | -0.58 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[YY1AP1]] | -0.56 | -0.50 / -0.51 | both halves | 1e-05 |  |
| [[HARBI1]] | -0.56 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[METTL25B]] | -0.56 | -0.47 / -0.53 | both halves | 2e-05 |  |
| [[SUSD6]] | -0.56 | -0.64 / -0.52 | both halves | 1e-05 |  |
| [[GORASP1]] | -0.55 | -0.44 / -0.59 | both halves | 3e-05 |  |
| [[RPS6KB2]] | -0.55 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[NR1D1]] | -0.55 | -0.45 / -0.53 | both halves | 3e-05 |  |
| [[RELB]] | -0.54 | -0.56 / -0.48 | both halves | 2e-05 |  |
| [[POLR1H]] | -0.54 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HLA-A]] | B | HLA-A activity lowers HSPD1's level | lines that do not express HLA-A (6) vs lines expressing it (44) | 1.26× higher at baseline in the lines without HLA-A | 0.096 | ⚠ within organs, on part of the lines; also absent: PHLDA1, S100A6, HLA-H |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.820). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.7, -11.7); signed map (-26.3, -29.2). **Vector** length 118, 56.0% of its response variance represented; |z| ≥ 3 in 1,329 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Attenuation phase* (reactome, mean cos +0.54 to 13); *HSF1-dependent transactivation* (reactome, mean cos +0.53 to 14); *Cellular response to heat stress* (reactome, mean cos +0.52 to 18).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +11.5 | +15.8 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +11.0 | +18.6 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +10.1 | +16.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +8.0 | +18.3 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.0 | +10.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.3 | +9.4 |
|  | [[EX229 (drug)]] 5 µM |  | +3.4 | +3.1 |
|  | [[c-Kit-IN-1 (drug)]] 5 µM |  | +3.4 | +3.6 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -7.6 | +0.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -7.5 | -0.3 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -6.4 | +0.8 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -6.1 | -4.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, would explain all of this change | -5.9 | +0.4 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.7 | -2.0 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | -4.5 | +0.3 |
|  | [[9-ING-41 (drug)]] 0.5 µM |  | -4.2 | +1.0 |
|  | [[Thymol (drug)]] 0.5 µM |  | -4.2 | -1.1 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -3.4 | -0.8 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein family D (Hsp60) member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2q33.1 — chr2:197,486,584-197,516,737 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GroEL, HSP60; previously SPG13 |
| Gene groups (HGNC) | Chaperonins; Mitochondrial nucleoid associated proteins |
| Hallmark sets | MYC_TARGETS_V2, MTORC1_SIGNALING, MYC_TARGETS_V1 |
| Reactome | 8 pathways, smallest: TFAP2A acts as a transcriptional repressor during retinoic acid induced cell differentiation; Mitochondrial unfolded protein response (UPRmt); Transcriptional regulation by the AP-2 (TFAP2) family of transcription factors |
| Matched by | ensembl_id |

**Function**, from UniProt [P10809](https://www.uniprot.org/uniprotkb/P10809) (60 kDa heat shock protein, mitochondrial):

> Chaperonin implicated in mitochondrial protein import and macromolecular assembly. Together with Hsp10, facilitates the correct folding of imported proteins. May also prevent misfolding and promote the refolding and proper assembly of unfolded polypeptides generated under stress conditions in the mitochondrial matrix. The functional units of these chaperonins consist of heptameric rings of the large subunit Hsp60, which function as a back-to-back double ring. In a cyclic reaction, Hsp60 ring …

**Summary**, from NCBI Gene [3329](https://www.ncbi.nlm.nih.gov/gene/3329):

> This gene encodes a member of the chaperonin family. The encoded mitochondrial protein may function as a signaling molecule in the innate immune system. This protein is essential for the folding and assembly of newly imported proteins in the mitochondria. This gene is adjacent to a related family member and the region between the 2 genes functions as a bidirectional promoter. Several pseudogenes have been associated with this gene. Two transcript variants encoding the same protein have been …

**Accessions** — [HGNC:5261](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5261) · Entrez [3329](https://www.ncbi.nlm.nih.gov/gene/3329) · UniProt [P10809](https://www.uniprot.org/uniprotkb/P10809) · Ensembl [ENSG00000144381](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000144381)

## Data

Gene col 6873: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6873); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6873, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6873]; `tensor/DDL_lfc|DDL_z.npy` [6873]; `embed/gene_vectors.npy` [6873]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6873 or target_col == 6873). Every well: [[HSPD1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSPD1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
