---
symbol: "HMGN2P46"
type: "gene"
col: 11024
ensembl_id: "ENSG00000179362"
name: "high mobility group nucleosomal binding domain 2 pseudogene 46"
location: "15q21.1"
module: 112
arm: "+"
pooled_cpm: 22.97
n_lines_expressing: 32
n_dd_up: 6
n_dd_down: 64
n_dd_up_clean: 5
n_dd_down_clean: 44
in_vector_space: true
direction_upstream: 28
direction_downstream: 25
tags: ["gene", "module/112"]
generated_by: "tahoemap"
---

# HMGN2P46

*high mobility group nucleosomal binding domain 2 pseudogene 46* — 15q21.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 6 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.06× (z +10.5, q 4e-23, up in 21 of 30 measured lines).
> Pooled over the cell lines (median), lowered significantly by 64 drug-doses (20 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.278× (z -13.1, q 1e-36, down in 28 of 30 measured lines) ⚠ cell-cycle shift, explains ~44% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.385× (z -9.8, q 2e-20, down in 24 of 30 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[C15orf48]] (+0.76, fdr 7e-06), [[SERPINB7]] (+0.71, fdr 7e-06), [[TRAF1]] (+0.69, fdr 7e-06); moves opposite to [[COPS8]] (-0.55, fdr 2e-05), [[PHKA1]] (-0.54, fdr 1e-05), [[SORT1]] (-0.53, fdr 3e-05).
> It is in [[Module 112]], a single-armed module (TNF-alpha signaling via NF-kB).
> Probable direction (from the cell lines, not proof of direct regulation): 28 arrows point to it, the strongest [[CTSS]] → it (grade B ⚠); 25 go from it, the strongest it → [[TRAF1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 7 in all, 1 with an alert ⚠. 6 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11024.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **2.06×** | +10.5 | 4e-23 | 21/30 (J82, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.94×** | +6.8 | 2e-09 | 20/29 (A-172, HS-578T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Rapamycin (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.021 | 9/30 (NCI-H1573, SK-MEL-2, …) | rises with dose |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **1.44×** | +3.7 | 0.024 | 15/30 (HOP62, hTERT-HPNE, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +3.7 | 0.024 | 16/30 (HS-578T, A-172, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.25×** | +3.3 | 0.098 | 13/30 (HOP62, MIA PaCa-2, …) | rises with dose |  |
| [[Temsirolimus (drug)]] 5 µM |  | 1.24× | +3.2 | 0.13 | 7/30 (NCI-H1573, RPMI-7951, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 64 in all, 20 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 64 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11024.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.278×** | -13.1 | 1e-36 | 28/30 (CFPAC-1, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.306×** | -12.1 | 2e-31 | 29/30 (CFPAC-1, Panc 03.27, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~47% of this change | **0.365×** | -10.3 | 1e-22 | 25/30 (CFPAC-1, Panc 03.27, …) | all doses, stronger at high dose |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.385×** | -9.8 | 2e-20 | 24/30 (HS-578T, PANC-1, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.375×** | -9.7 | 5e-20 | 23/29 (NCI-H1573, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~25% here) |
| [[Clobetasol propionate (drug)]] 5 µM |  | **0.399×** | -9.4 | 4e-19 | 25/30 (NCI-H1792, HOP62, …) | all doses, stronger at high dose |  |
| [[Betamethasone dipropionate (drug)]] 0.5 µM |  | **0.434×** | -8.6 | 9e-16 | 23/30 (A498, RPMI-7951, …) | all doses, flat |  |
| [[Betamethasone dipropionate (drug)]] 0.05 µM |  | **0.409×** | -8.5 | 2e-15 | 23/28 (HOP62, A498, …) | all doses, flat |  |
| [[Clobetasol propionate (drug)]] 0.5 µM |  | **0.462×** | -7.9 | 2e-13 | 23/30 (NCI-H1792, A498, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 0.05 µM |  | **0.463×** | -7.9 | 2e-13 | 22/30 (NCI-H1792, A498, …) | all doses, flat |  |
| [[NG25 (drug)]] 5 µM |  | **0.236×** | -7.7 | 5e-13 | 25/29 (NCI-H1792, A549, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dexamethasone (drug)]] 5 µM |  | **0.478×** | -7.6 | 2e-12 | 22/30 (A498, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **0.480×** | -7.5 | 2e-12 | 23/30 (SNU-423, HOP62, …) | all doses, stronger at high dose |  |
| [[Budesonide (drug)]] 5 µM |  | **0.487×** | -7.4 | 7e-12 | 23/30 (NCI-H1792, H4, …) | all doses, flat |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change | **0.494×** | -7.2 | 2e-11 | 20/26 (NCI-H1573, HS-578T, …) | inconsistent across doses | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.495×** | -7.2 | 2e-11 | 23/30 (HOP62, H4, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.506×** | -7.0 | 1e-10 | 22/30 (Panc 03.27, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Triamcinolone (drug)]] 0.5 µM |  | **0.515×** | -6.8 | 3e-10 | 24/30 (NCI-H1792, A498, …) | all doses, flat |  |
| [[Dexamethasone (drug)]] 0.5 µM |  | **0.520×** | -6.7 | 6e-10 | 21/30 (NCI-H1792, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.521×** | -6.3 | 7e-09 | 20/30 (J82, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.87 per unit of S-phase module lfc, +0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11024. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H1792 (line)]] | alt | 107 | 0 | 23 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0212× (z -24.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~76% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.293× (z -11.9) |
| [[HS-578T (line)]] | alt | 62.6 | 1 | 13 (8 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 6.49× (z +10.5) | [[Dinaciclib (drug)]] 0.5 µM 0.0359× (z -18.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.0867× (z -13.5) |
| [[HOP62 (line)]] | alt | 49.9 | 1 | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.91× (z +13.4) | [[Dinaciclib (drug)]] 0.5 µM 0.128× (z -12.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.134× (z -11.9) |
| [[J82 (line)]] | alt | 56.4 | 1 | 11 (9 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.69× (z +15.2) | [[Dinaciclib (drug)]] 5 µM 0.0720× (z -17.5) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.222× (z -10.4) |
| [[H4 (line)]] | wt | 64.6 | 0 | 10 (7 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0660× (z -12.5) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.112× (z -10.1) |
| [[NCI-H1573 (line)]] | alt | 122 | 0 | 10 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0161× (z -28.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change · without an alert: [[Budesonide (drug)]] 0.5 µM 0.251× (z -9.6) |
| [[CFPAC-1 (line)]] | alt | 107 | 1 | 8 (8 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.21× (z +9.1) | [[Panobinostat (drug)]] 5 µM 0.109× (z -17.8) ⚠ cell-cycle shift, explains ~44% of this change |
| [[A498 (line)]] | wt | 16.4 | 1 | 6 | [[Homoharringtonine (drug)]] 0.5 µM 7.36× (z +10.4) | [[Betamethasone dipropionate (drug)]] 0.5 µM 0.137× (z -10.3) |
| [[SNU-423 (line)]] | alt | 32.3 | 1 | 6 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.00× (z +11.8) | [[Panobinostat (drug)]] 0.5 µM 0.109× (z -13.3) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.184× (z -10.1) |
| [[Panc 03.27 (line)]] | alt | 51.6 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.107× (z -15.7) ⚠ cell-cycle shift, explains ~47% of this change |
| [[A549 (line)]] | wt | 25.6 | 0 | 5 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.128× (z -12.4) ⚠ cell-cycle shift, explains ~44% of this change · without an alert: [[NG25 (drug)]] 5 µM 0.0677× (z -8.5) |
| [[SW 900 (line)]] | alt | 25.1 | 0 | 5 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.0705× (z -12.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.252× (z -8.8) |
| [[HEC-1-A (line)]] | alt | 18.2 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0526× (z -16.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~87% of this change |
| [[PANC-1 (line)]] | alt | 13.6 | 1 | 3 | [[Homoharringtonine (drug)]] 0.5 µM 4.37× (z +9.7) | [[Ixazomib citrate (drug)]] 5 µM 0.156× (z -12.0) |
| [[A-172 (line)]] | wt | 13.2 | 1 | 2 (2 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 11.5× (z +11.0) | [[Panobinostat (drug)]] 0.5 µM 0.0562× (z -12.9) ⚠ cell-cycle shift, explains ~47% of this change |
| [[BT-474 (line)]] | alt | 22.5 | 0 | 3 (2 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.105× (z -8.9) ⚠ cell-cycle shift, explains ~47% of this change · without an alert: [[Ponatinib (drug)]] 5 µM 0.117× (z -8.5) |
| [[hTERT-HPNE (line)]] | wt | 27.5 | 0 | 3 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0590× (z -11.9) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.125× (z -9.1) |
| [[LS 180 (line)]] | wt | 13.5 | 0 | 3 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.137× (z -9.0) ⚠ cell-cycle shift, explains ~41% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.258× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 12.1 | 2 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 27.8× (z +14.4) | — |
| [[NCI-H23 (line)]] | alt | 9.64 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.03× (z +10.5) | — |
| [[RPMI-7951 (line)]] | alt | 32.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.130× (z -9.4) |
| [[A-427 (line)]] | wt | 1.93 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 4.56 n.m. | — | — | — | — |
| [[AsPC-1 (line)]] | alt | 2.83 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 2.76 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 2.11 n.m. | — | — | — | — |
| [[CHP-212 (line)]] | wt | 3.15 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 3.02 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 4.08 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 3.83 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 5.60 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 9.01 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 2.61 n.m. | — | — | — | — |
| [[MIA PaCa-2 (line)]] | alt | 7.33 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 7.64 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 11.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.6 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 3.64 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.45 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 2.50 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.29 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.18 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 63.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 22.5 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 2.58 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 2.67 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 1.75 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11024), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[C15orf48]] | +0.76 | +0.78 / +0.75 | both halves | 7e-06 |  |
| [[SERPINB7]] | +0.71 | +0.66 / +0.70 | both halves | 7e-06 |  |
| [[TRAF1]] | +0.69 | +0.63 / +0.68 | both halves | 7e-06 |  |
| [[DSE]] | +0.67 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[IL1B]] | +0.65 | +0.62 / +0.66 | both halves | 7e-06 |  |
| [[SLC41A2]] | +0.64 | +0.64 / +0.58 | both halves | 7e-06 |  |
| [[CRTAC1]] | +0.64 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[MSANTD3]] | +0.64 | +0.58 / +0.62 | both halves | 7e-06 |  |
| [[CPAMD8]] | +0.64 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[DNAH17]] | +0.63 | +0.57 / +0.62 | both halves | 1e-05 |  |
| [[GBP5]] | +0.62 | +0.61 / +0.54 | both halves | 1e-05 |  |
| [[LUCAT1]] | +0.60 | +0.60 / +0.59 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[COPS8]] | -0.55 | -0.47 / -0.56 | both halves | 2e-05 |  |
| [[PHKA1]] | -0.54 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[SORT1]] | -0.53 | -0.44 / -0.54 | both halves | 3e-05 |  |
| [[MSI2]] | -0.53 | -0.59 / -0.45 | both halves | 3e-05 |  |
| [[TMEM164]] | -0.53 | -0.57 / -0.48 | both halves | 2e-05 |  |
| [[ABHD2]] | -0.53 | -0.50 / -0.48 | both halves | 2e-05 |  |
| [[ATP1A1]] | -0.53 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[CLASP1]] | -0.52 | -0.52 / -0.53 | both halves | 1e-05 |  |
| [[CHPT1]] | -0.52 | -0.56 / -0.47 | both halves | 2e-05 |  |
| [[NFIA]] | -0.51 | -0.55 / -0.51 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*28 arrows, 28 of them with an alert ⚠; grade A 0, B 15, C 13. Shown: the 12 strongest; 16 more arrows (16 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTSS]] | B | CTSS activity raises HMGN2P46's level | lines that do not express CTSS (15) vs lines expressing it (35) | 3.61× lower at baseline in the lines without CTSS | 0.010 | ⚠ within organs, on part of the lines; also absent: LINC02257, NMRAL2P-1, CSF2; maybe low, not absent |
| [[BMP2]] | B | BMP2 activity raises HMGN2P46's level | lines that do not express BMP2 (20) vs lines expressing it (30) | 2.63× lower at baseline in the lines without BMP2 | 0.010 | ⚠ within organs, on part of the lines; also absent: PTGS2, PTPRB, IFI44 |
| [[HRH1]] | B | HRH1 activity raises HMGN2P46's level | lines that do not express HRH1 (10) vs lines expressing it (40) | 3.07× lower at baseline in the lines without HRH1 | 0.012 | ⚠ within organs, on part of the lines; also absent: PHLDA2, PLAUR, LRRK1; maybe low, not absent |
| [[ADAM7-AS1]] | B | ADAM7-AS1 activity raises HMGN2P46's level | lines that do not express ADAM7-AS1 (23) vs lines expressing it (27) | 3.39× lower at baseline in the lines without ADAM7-AS1 | 0.018 | ⚠ within organs, on part of the lines; also absent: SETBP1, KCNMA1, STC1; maybe low, not absent |
| [[PTGS2]] | B | PTGS2 activity raises HMGN2P46's level | lines that do not express PTGS2 (27) vs lines expressing it (23) | 2.73× lower at baseline in the lines without PTGS2 | 0.020 | ⚠ within organs, on part of the lines; also absent: ADAMTS9-AS2, CFH, ITGA4 |
| [[MIR155HG]] | B | MIR155HG activity raises HMGN2P46's level | lines that do not express MIR155HG (28) vs lines expressing it (22) | 2.96× lower at baseline in the lines without MIR155HG | 0.021 | ⚠ within organs, on part of the lines; also absent: MT1M, IL6, EDNRA |
| [[PLAU]] | B | PLAU activity raises HMGN2P46's level | lines that do not express PLAU (26) vs lines expressing it (24) | 3.05× lower at baseline in the lines without PLAU | 0.025 | ⚠ within organs, on part of the lines; also absent: ADAMTS16, C3, VGLL3 |
| [[IL1A]] | B | IL1A activity raises HMGN2P46's level | lines that do not express IL1A (27) vs lines expressing it (23) | 3.39× lower at baseline in the lines without IL1A | 0.027 | ⚠ within organs, on part of the lines; also absent: EDNRA, ABI3BP, PLAT |
| [[CACNG8]] | B | CACNG8 activity raises HMGN2P46's level | lines that do not express CACNG8 (14) vs lines expressing it (36) | 2.44× lower at baseline in the lines without CACNG8 | 0.042 | ⚠ within organs, on part of the lines; also absent: CACNG6, GAB3, KHDC1 |
| [[NTF3]] | B | NTF3 activity raises HMGN2P46's level | lines that do not express NTF3 (26) vs lines expressing it (24) | 2.98× lower at baseline in the lines without NTF3 | 0.048 | ⚠ within organs, on part of the lines; also absent: COL4A1, MME, HS3ST3A1 |
| [[KIAA1217]] | B | KIAA1217 activity raises HMGN2P46's level | lines that do not express KIAA1217 (10) vs lines expressing it (40) | 2.23× lower at baseline in the lines without KIAA1217 | 0.057 | ⚠ within organs, on part of the lines; also absent: FAM107B, MET, S100A16 |
| [[IRAG2]] | B | IRAG2 activity raises HMGN2P46's level | lines that do not express IRAG2 (39) vs lines expressing it (11) | 4.38× lower at baseline in the lines without IRAG2 | 0.061 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: CARMN, GDNF, LINC01411 |

### Downstream of this gene

*25 arrows, 25 of them with an alert ⚠; grade A 0, B 20, C 5. Shown: the 12 strongest; 13 more arrows (13 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TRAF1]] | B | HMGN2P46 activity raises TRAF1's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 3.34× lower at baseline in the lines without HMGN2P46 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[ISG20]] | B | HMGN2P46 activity raises ISG20's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.96× lower at baseline in the lines without HMGN2P46 | 0.010 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[LINC02363]] | B | HMGN2P46 activity raises LINC02363's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.42× lower at baseline in the lines without HMGN2P46 | 0.014 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[NBPF14]] | B | HMGN2P46 activity raises NBPF14's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.68× lower at baseline in the lines without HMGN2P46 | 0.020 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[IRAK2]] | B | HMGN2P46 activity raises IRAK2's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.81× lower at baseline in the lines without HMGN2P46 | 0.024 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[NFIA]] | B | HMGN2P46 activity lowers NFIA's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.99× higher at baseline in the lines without HMGN2P46 | 0.037 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[NOTCH2NLB]] | B | HMGN2P46 activity raises NOTCH2NLB's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.60× lower at baseline in the lines without HMGN2P46 | 0.042 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[LXN]] | B | HMGN2P46 activity raises LXN's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.05× lower at baseline in the lines without HMGN2P46 | 0.044 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| cells under [[Betamethasone dipropionate (drug)]] 5 µM | B | [[ENSG00000259354]], HMGN2P46 activity raises the cells' numbers under Betamethasone dipropionate 5 µM (protects the cells) | lines that do not express ENSG00000259354, HMGN2P46 (18) vs lines expressing them (30) | the lines without ENSG00000259354, HMGN2P46: 0.80× the cells of the other lines | 0.050 | ⚠ within organs, on part of the lines; also absent: C15orf48, IL1R1, STAC; co-absent genes |
| [[PLAU]] | B | HMGN2P46 activity raises PLAU's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 3.22× lower at baseline in the lines without HMGN2P46 | 0.057 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[AMPD3]] | B | HMGN2P46 activity raises AMPD3's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 2.13× lower at baseline in the lines without HMGN2P46 | 0.058 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |
| [[NBPF10]] | B | HMGN2P46 activity raises NBPF10's level | lines that do not express HMGN2P46 (18) vs lines expressing it (32) | 1.44× lower at baseline in the lines without HMGN2P46 | 0.062 | ⚠ within organs, on part of the lines; co-absent genes; also absent: C15orf48, IL1R1, STAC |

## Where it sits

- **Module**: [[Module 112]] — TNF-alpha signaling via NF-kB; 43 genes; every member is in the + arm (projection on the module's main direction 0.716). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (29.4, 0.4); signed map (40.4, 11.9). **Vector** length 136, 43.3% of its response variance represented; |z| ≥ 3 in 1,333 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *TNF-alpha signaling via NF-kB* (hallmark, mean cos +0.53 to 11); *Interleukin-10 signaling* (reactome, mean cos +0.54 to 5); *KRAS signaling up* (hallmark, mean cos +0.52 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 5 µM |  | +11.1 | +10.5 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +7.6 | +6.8 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +6.7 | +1.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +6.5 | +3.3 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | +5.9 | +3.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.7 | +2.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +3.4 | +2.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.2 | +0.7 |
|  | [[Cyclosporin A (drug)]] 5 µM |  | +2.2 | +1.9 |
| fall | [[NG25 (drug)]] 5 µM |  | -6.0 | -7.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -5.9 | -6.7 |
|  | [[Dexamethasone (drug)]] 5 µM |  | -5.3 | -7.6 |
|  | [[Clobetasol propionate (drug)]] 5 µM |  | -5.3 | -9.4 |
|  | [[Budesonide (drug)]] 5 µM |  | -5.1 | -7.4 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -4.7 | -6.8 |

## What is on record

|  |  |
|---|---|
| Name | high mobility group nucleosomal binding domain 2 pseudogene 46 |
| Locus type | pseudogene |
| Location | 15q21.1 — chr15:45,555,482-45,555,971 (+) |
| Ensembl biotype | transcribed_processed_pseudogene |
| Also known as | FLJ39426, D-PCa-2; previously C15orf21 |
| Gene groups (HGNC) | Small nucleolar RNA non-coding host genes |
| Matched by | ensembl_id |

UniProt [Q86SG4](https://www.uniprot.org/uniprotkb/Q86SG4) carries no function annotation.

**Summary**, from NCBI Gene [283651](https://www.ncbi.nlm.nih.gov/gene/283651):

> Predicted to enable chromatin binding activity. Predicted to be involved in chromatin organization. Predicted to be active in nucleus. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:26817](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:26817) · Entrez [283651](https://www.ncbi.nlm.nih.gov/gene/283651) · UniProt [Q86SG4](https://www.uniprot.org/uniprotkb/Q86SG4) · Ensembl [ENSG00000179362](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000179362)

## Data

Gene col 11024: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11024); `tables/drug_effects.parquet` (71 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11024, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11024]; `tensor/DDL_lfc|DDL_z.npy` [11024]; `embed/gene_vectors.npy` [11024]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11024 or target_col == 11024). Every well: [[HMGN2P46 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/HMGN2P46.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
