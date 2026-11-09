---
symbol: "HSP90AB1"
type: "gene"
col: 1765
ensembl_id: "ENSG00000096384"
name: "heat shock protein 90 alpha family class B member 1"
location: "6p21.1"
module: 60
arm: "+"
pooled_cpm: 1055.72
n_lines_expressing: 50
n_dd_up: 24
n_dd_down: 0
n_dd_up_clean: 12
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/060"]
generated_by: "tahoemap"
---

# HSP90AB1

*heat shock protein 90 alpha family class B member 1* — 6p21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 24 drug-doses (12 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 4.26× (z +17.4, q 0e+00, up in 48 of 48 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.396×, C-33 A 0.367×, CHP-212 0.470×, SHP-77 0.520×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.471×; ⚠ cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.540×; ⚠ cell-cycle shift, explains ~80% of this change).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSP90AB3P]] (+0.86, fdr 7e-06), [[HSPD1]] (+0.86, fdr 7e-06), [[HSP90AB2P]] (+0.85, fdr 7e-06); moves opposite to [[GORASP1]] (-0.54, fdr 3e-05), [[ZCCHC3]] (-0.53, fdr 2e-05), [[UNK]] (-0.53, fdr 5e-05).
> It sits in the **+** arm of [[Module 060]] (heat shock).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CHORDC1]] → it (grade C ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 25 in all, 13 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 24 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1765.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **4.26×** | +17.4 | 0e+00 | 48/48 (SW1417, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Auranofin (drug)]] 5 µM |  | **4.26×** | +17.4 | 0e+00 | 48/48 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **3.83×** | +16.2 | 0e+00 | 48/48 (HT-29, A-172, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change | **2.93×** | +12.9 | 4e-36 | 49/49 (COLO 205, MIA PaCa-2, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.51×** | +11.5 | 2e-28 | 48/48 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **2.60×** | +11.0 | 2e-26 | 44/44 (NCI-H460, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **5.34×** | +10.5 | 5e-24 | 45/45 (SW1417, HEC-1-A, …) | all doses, flat | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.15×** | +8.5 | 1e-15 | 45/45 (MIA PaCa-2, HT-29, …) | all doses, stronger at high dose | composition shift |
| [[Bortezomib (drug)]] 0.5 µM |  | **2.53×** | +8.0 | 1e-13 | 48/49 (CFPAC-1, HT-29, …) | all doses, flat | noisy plate (z scaled) |
| [[NG25 (drug)]] 5 µM |  | **3.42×** | +7.7 | 6e-13 | 47/47 (KATO III, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~34% of this change | **1.73×** | +6.3 | 2e-08 | 45/47 (COLO 205, SHP-77, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.49×** | +4.8 | 9e-05 | 33/48 (AsPC-1, HS-578T, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **1.47×** | +4.7 | 1e-04 | 34/48 (AsPC-1, KATO III, …) | rises with dose |  |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.11× | +4.4 | 4e-04 | 1/50 (NCI-H2122) | inconsistent across doses |  |
| [[Mebendazole (drug)]] 5 µM |  | **1.41×** | +3.9 | 0.003 | 46/48 (HOP62, HS-578T, …) | top dose only |  |
| [[Infigratinib (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.003 | 41/48 (AsPC-1, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 5 µM |  | **1.86×** | +3.9 | 0.003 | 47/48 (HT-29, KATO III, …) | top dose only | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 0.5 µM |  | **1.31×** | +3.2 | 0.033 | 37/47 (HT-29, SK-MEL-2, …) | rises with dose |  |
| [[NG25 (drug)]] 0.05 µM |  | **1.42×** | +3.2 | 0.036 | 43/49 (BT-474, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | **1.20×** | +2.9 | 0.087 | 24/48 (C-33 A, RKO, …) | top dose only | position effect removed |

## Drugs that lower it

No drug-dose lowers it in the pooled data (pooled over the cell lines, median: none with |z| ≥ 3 or q < 0.10). A response seen in fewer than about half of the measured lines does not reach the pooled data; see [[#In which cell lines]].

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (A-427 0.396×, C-33 A 0.367×, CHP-212 0.470×, SHP-77 0.520×; ⚠ cell-cycle shift, would explain all of this change); [[Homoharringtonine (drug)]] 0.5 µM in 1 line (A-427 0.471×; ⚠ cell-cycle shift, explains ~48% of this change); [[Idarubicin (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H23 0.540×; ⚠ cell-cycle shift, explains ~80% of this change).

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.23 per unit of S-phase module lfc, +0.40 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1765. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 1,006 | 11 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.92× (z +20.4) | — |
| [[AsPC-1 (line)]] | alt | 682 | 10 (6 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.80× (z +14.6) | — |
| [[HT-29 (line)]] | alt | 796 | 10 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.86× (z +23.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 1,297 | 10 (5 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.73× (z +16.9) | — |
| [[A-172 (line)]] | wt | 1,022 | 9 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 7.08× (z +21.6) | — |
| [[LoVo (line)]] | wt | 887 | 9 (5 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.77× (z +17.8) | — |
| [[COLO 205 (line)]] | alt | 299 | 8 (4 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 8.23× (z +16.1) ⚠ toxic; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 7.53× (z +16.1) | — |
| [[HepG2_C3A (line)]] | wt | 1,290 | 8 (5 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.87× (z +11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +11.5) | — |
| [[Hs 766T (line)]] | wt | 646 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.31× (z +14.9) | — |
| [[HS-578T (line)]] | alt | 936 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.96× (z +18.8) | — |
| [[J82 (line)]] | alt | 843 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.43× (z +16.4) | — |
| [[NCI-H1573 (line)]] | alt | 429 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.37× (z +16.0) | — |
| [[RPMI-7951 (line)]] | alt | 804 | 8 (4 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.77× (z +19.3) | — |
| [[SW1417 (line)]] | alt | 887 | 8 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.85× (z +22.4) | — |
| [[A498 (line)]] | wt | 803 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.25× (z +14.8) | — |
| [[CFPAC-1 (line)]] | alt | 1,006 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 6.12× (z +17.9) | — |
| [[HEC-1-A (line)]] | alt | 864 | 7 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.89× (z +21.7) | — |
| [[HOP62 (line)]] | alt | 1,601 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.13× (z +14.0) | — |
| [[hTERT-HPNE (line)]] | wt | 757 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.77× (z +15.4) | — |
| [[LOX-IMVI (line)]] | wt | 1,146 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.39× (z +16.5) | — |
| [[NCI-H1792 (line)]] | alt | 665 | 7 (6 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 4.70× (z +17.0) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 2.77× (z +8.7) | — |
| [[NCI-H2347 (line)]] | alt | 1,359 | 7 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.29× (z +16.2) | — |
| [[Panc 03.27 (line)]] | alt | 1,297 | 7 (3 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 5.57× (z +18.6) | — |
| [[SK-MEL-2 (line)]] | alt | 1,333 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.48× (z +20.4) | — |
| [[SNU-423 (line)]] | alt | 1,392 | 7 (4 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.11× (z +16.0) | — |
| [[SW 900 (line)]] | alt | 723 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.16× (z +15.8) | — |
| [[SW480 (line)]] | alt | 1,137 | 7 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.64× (z +17.2) | — |
| [[A-427 (line)]] | wt | 1,715 | 4 (1 ⚠) | 2 (2 ⚠) | [[Auranofin (drug)]] 5 µM 3.96× (z +15.6) | [[Homoharringtonine (drug)]] 5 µM 0.396× (z -13.1) ⚠ cell-cycle shift, would explain all of this change |
| [[A549 (line)]] | wt | 940 | 6 (3 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.99× (z +14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 3.74× (z +12.1) | — |
| [[H4 (line)]] | wt | 1,489 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.62× (z +15.4) | — |
| [[LS 180 (line)]] | wt | 1,077 | 6 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.66× (z +16.0) | — |
| [[RKO (line)]] | wt | 1,332 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.23× (z +15.0) | — |
| [[SHP-77 (line)]] | alt | 865 | 5 (3 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 4.69× (z +18.0) | [[Homoharringtonine (drug)]] 5 µM 0.520× (z -9.6) ⚠ cell-cycle shift, would explain all of this change |
| [[SNU-1 (line)]] | wt | 893 | 6 (2 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.92× (z +19.1) | — |
| [[C-33 A (line)]] | alt | 1,034 | 4 (1 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 5.28× (z +15.2) | [[Homoharringtonine (drug)]] 5 µM 0.367× (z -11.6) ⚠ cell-cycle shift, would explain all of this change |
| [[CHP-212 (line)]] | wt | 1,391 | 4 (1 ⚠) | 1 (1 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.37× (z +12.5) | [[Homoharringtonine (drug)]] 5 µM 0.470× (z -9.8) ⚠ cell-cycle shift, would explain all of this change |
| [[HCT15 (line)]] | alt | 1,146 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.90× (z +13.7) | — |
| [[NCI-H2030 (line)]] | alt | 1,169 | 5 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 3.76× (z +13.4) | — |
| [[NCI-H460 (line)]] | wt | 949 | 5 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 5.02× (z +14.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~34% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 3.24× (z +10.6) | — |
| [[PANC-1 (line)]] | alt | 1,150 | 5 (2 ⚠) | 0 | [[Ixazomib citrate (drug)]] 5 µM 4.02× (z +14.2) | — |
| [[BT-474 (line)]] | alt | 957 | 4 | 0 | [[Auranofin (drug)]] 5 µM 6.56× (z +21.2) | — |
| [[C32 (line)]] | wt | 1,043 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 6.85× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 2,101 | 3 (2 ⚠) | 1 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.50× (z +13.2) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.540× (z -8.5) ⚠ cell-cycle shift, explains ~80% of this change |
| [[SW 1088 (line)]] | alt | 656 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 7.26× (z +13.3) | — |
| [[SW 1271 (line)]] | alt | 742 | 4 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 9.39× (z +18.0) | — |
| [[SW48 (line)]] | wt | 1,575 | 4 (1 ⚠) | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.77× (z +12.9) | — |
| [[AN3 CA (line)]] | alt | 1,588 | 3 (1 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 4.83× (z +17.3) | — |
| [[NCI-H661 (line)]] | alt | 1,409 | 2 | 0 | [[Ixazomib citrate (drug)]] 0.5 µM 3.58× (z +9.4) | — |
| [[NCI-H2122 (line)]] | alt | 777 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 990 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1765), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*77 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSP90AB3P]] | +0.86 | +0.88 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[HSPD1]] | +0.86 | +0.83 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 970 |
| [[HSP90AB2P]] | +0.85 | +0.86 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[HSP90AA1]] | +0.80 | +0.75 / +0.82 | both halves | 7e-06 | same gene group; pathway: Assembly and release of respiratory syncytial virus (RSV) virions; STRING 997 |
| [[CCT4]] | +0.79 | +0.77 / +0.78 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 946 |
| [[HSPA8]] | +0.76 | +0.76 / +0.75 | both halves | 7e-06 | pathway: Attenuation phase; STRING 999 |
| [[TCP1]] | +0.72 | +0.72 / +0.71 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 956 |
| [[CCT3]] | +0.70 | +0.68 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 940 |
| [[HSP90AA2P]] | +0.68 | +0.65 / +0.66 | both halves | 7e-06 |  |
| [[CACYBP]] | +0.67 | +0.63 / +0.70 | both halves | 7e-06 | STRING 677 |
| [[PTGES3]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_MYC_TARGETS_V1; STRING 999 |
| [[FXR1]] | +0.64 | +0.59 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*23 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GORASP1]] | -0.54 | -0.43 / -0.54 | both halves | 3e-05 |  |
| [[ZCCHC3]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[UNK]] | -0.53 | -0.40 / -0.53 | both halves | 5e-05 |  |
| [[CHKB]] | -0.52 | -0.46 / -0.44 | both halves | 3e-05 |  |
| [[HARBI1]] | -0.52 | -0.43 / -0.47 | both halves | 3e-05 |  |
| [[YY1AP1]] | -0.51 | -0.41 / -0.51 | both halves | 4e-05 |  |
| [[RBX1]] | -0.50 | -0.45 / -0.47 | both halves | 3e-05 | pathway: G2/M Transition; STRING 661 |
| [[TNRC6C]] | -0.50 | -0.51 / -0.41 | both halves | 4e-05 | pathway: ESR-mediated signaling |
| [[SUSD6]] | -0.50 | -0.59 / -0.48 | both halves | 2e-05 |  |
| [[CTDNEP1]] | -0.50 | -0.49 / -0.36 | both halves | 9e-05 |  |
| [[UQCRFS1]] | -0.49 | -0.28 / -0.51 | both halves | 3e-04 |  |
| [[HIVEP1]] | -0.49 | -0.45 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CHORDC1]] | C | CHORDC1's natural level strengthens HSP90AB1's drug response | CHORDC1's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.61, reverse -0.06; direction not clear | 0.099 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 060]] — heat shock; 78 genes; this gene is in the **+** arm (projection on the module's main direction 0.787). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (-19.6, -11.6); signed map (-26.3, -29.0). **Vector** length 120, 59.1% of its response variance represented; |z| ≥ 3 in 1,219 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *heat shock* (control, mean cos +0.53 to 13); *Mitochondrial unfolded protein response (UPRmt)* (reactome, mean cos +0.56 to 5); *Formation of tubulin folding intermediates by CCT/TriC* (reactome, mean cos +0.60 to 5).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.3 | +11.5 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +9.7 | +17.4 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.5 | +16.2 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | +8.3 | +10.5 |
|  | [[Auranofin (drug)]] 5 µM |  | +7.0 | +17.4 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +5.2 | +8.0 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +4.3 | +1.4 |
|  | [[Infigratinib (drug)]] 5 µM |  | +2.2 | +3.9 |
| fall | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -8.2 | -0.2 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.9 | +0.1 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift | -7.2 | +1.8 |
|  | [[TAK-901 (drug)]] 5 µM | ⚠ cell-cycle shift | -6.5 | -1.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift | -6.5 | +1.8 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -5.6 | -1.9 |
|  | [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | -4.5 | -2.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.8 | +0.2 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.7 | -0.6 |
|  | [[Thymol (drug)]] 0.5 µM |  | -3.6 | -1.1 |

## What is on record

|  |  |
|---|---|
| Name | heat shock protein 90 alpha family class B member 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6p21.1 — chr6:44,246,166-44,253,888 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously HSPC2, HSPCB |
| Gene groups (HGNC) | Heat shock 90kDa proteins |
| Hallmark sets | MYC_TARGETS_V1 |
| Reactome | 57 pathways, smallest: Assembly and release of respiratory syncytial virus (RSV) virions; Respiratory syncytial virus genome replication; Uptake and function of diphtheria toxin |
| Matched by | ensembl_id |

**Function**, from UniProt [P08238](https://www.uniprot.org/uniprotkb/P08238) (Heat shock protein HSP 90-beta):

> Molecular chaperone that promotes the maturation, structural maintenance and proper regulation of specific target proteins involved for instance in cell cycle control and signal transduction. Undergoes a functional cycle linked to its ATPase activity. This cycle probably induces conformational changes in the client proteins, thereby causing their activation. Interacts dynamically with various co-chaperones that modulate its substrate recognition, ATPase cycle and chaperone function. Engages …

**Summary**, from NCBI Gene [3326](https://www.ncbi.nlm.nih.gov/gene/3326):

> This gene encodes a member of the heat shock protein 90 family; these proteins are involved in signal transduction, protein folding and degradation and morphological evolution. This gene encodes the constitutive form of the cytosolic 90 kDa heat-shock protein and is thought to play a role in gastric apoptosis and inflammation. Alternative splicing results in multiple transcript variants. Pseudogenes have been identified on multiple chromosomes. [provided by RefSeq, Dec 2012]

**Accessions** — [HGNC:5258](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:5258) · Entrez [3326](https://www.ncbi.nlm.nih.gov/gene/3326) · UniProt [P08238](https://www.uniprot.org/uniprotkb/P08238) · Ensembl [ENSG00000096384](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000096384)

## Data

Gene col 1765: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1765); `tables/drug_effects.parquet` (25 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1765, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1765]; `tensor/DDL_lfc|DDL_z.npy` [1765]; `embed/gene_vectors.npy` [1765]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1765 or target_col == 1765). Every well: [[HSP90AB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HSP90AB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
