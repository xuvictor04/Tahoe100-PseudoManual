---
symbol: "EIF2AK2"
type: "gene"
col: 626
ensembl_id: "ENSG00000055332"
name: "eukaryotic translation initiation factor 2 alpha kinase 2"
location: "2p22.2"
module: 32
arm: "+"
pooled_cpm: 311.02
n_lines_expressing: 49
n_dd_up: 8
n_dd_down: 43
n_dd_up_clean: 8
n_dd_down_clean: 36
in_vector_space: true
direction_upstream: 40
direction_downstream: 46
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# EIF2AK2

*eukaryotic translation initiation factor 2 alpha kinase 2* — 2p22.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (none with an alert); the strongest is [[Cobimetinib (drug)]] 5 µM: 1.35× (z +5.2, q 1e-04, up in 33 of 46 measured lines).
> Pooled over the cell lines (median), lowered significantly by 43 drug-doses (7 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.279× (z -22.9, q 0e+00, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PARP9]] (+0.94, fdr 7e-06), [[MX1]] (+0.91, fdr 7e-06), [[PARP14]] (+0.90, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 40 arrows point to it, the strongest [[OAS2]] → it (grade B ⚠); 46 go from it, the strongest it → [[ADAR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, none with an alert; shown: the 15 strongest. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 626.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | **1.35×** | +5.2 | 1e-04 | 33/46 (HS-578T, PANC-1, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.28×** | +4.5 | 0.002 | 26/47 (NCI-H2347, KATO III, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.25×** | +4.1 | 0.010 | 29/46 (Hs 766T, AsPC-1, …) | rises with dose |  |
| [[venetoclax (drug)]] 0.05 µM |  | **1.24×** | +3.8 | 0.020 | 28/48 (PANC-1, Panc 03.27, …) | inconsistent across doses |  |
| [[Estrone sulfate (potassium) (drug)]] 5 µM |  | **1.22×** | +3.7 | 0.020 | 26/47 (A498, NCI-H1792, …) | top dose only |  |
| [[Binimetinib (drug)]] 0.05 µM |  | 1.15× | +3.6 | 0.020 | 12/48 (CFPAC-1, AsPC-1, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | 1.19× | +3.6 | 0.020 | 21/47 (AsPC-1, CFPAC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Binimetinib (drug)]] 0.5 µM |  | 1.17× | +3.6 | 0.020 | 15/47 (AsPC-1, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.22×** | +3.6 | 0.020 | 23/47 (A-172, Panc 03.27, …) | inconsistent across doses |  |
| [[Thymol (drug)]] 5 µM |  | 1.14× | +3.5 | 0.023 | 8/47 (HT-29, A-172, …) | top dose only |  |
| [[Binimetinib (drug)]] 5 µM |  | **1.20×** | +3.5 | 0.023 | 22/48 (CFPAC-1, AsPC-1, …) | all doses, flat | noisy plate (z scaled) |
| [[Omeprazole (drug)]] 0.05 µM |  | 1.19× | +3.3 | 0.048 | 19/47 (J82, NCI-H2347, …) | inconsistent across doses |  |
| [[Elimusertib hydrochloride (drug)]] 0.05 µM |  | **1.21×** | +3.2 | 0.048 | 18/47 (AsPC-1, NCI-H1792, …) | inconsistent across doses |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 1.19× | +3.2 | 0.048 | 15/47 (A-172, SW 1088, …) | inconsistent across doses |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | 1.20× | +3.2 | 0.048 | 21/47 (NCI-H23, Hs 766T, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 7 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 43 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 626.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.279×** | -22.9 | 0e+00 | 47/47 (LoVo, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.286×** | -22.5 | 0e+00 | 47/47 (LoVo, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Tofacitinib (drug)]] 5 µM |  | **0.418×** | -22.2 | 0e+00 | 33/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **0.294×** | -22.0 | 0e+00 | 47/47 (NCI-H23, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here) |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.510×** | -17.1 | 0e+00 | 35/48 (RPMI-7951, CFPAC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.553×** | -15.0 | 0e+00 | 37/47 (RKO, PANC-1, …) | rises with dose | cell-cycle shift (explains ~5% here); composition shift |
| [[Tofacitinib (drug)]] 0.5 µM |  | **0.455×** | -14.1 | 2e-43 | 35/48 (NCI-H1573, NCI-H23, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.471×** | -13.5 | 6e-40 | 36/47 (NCI-H1573, NCI-H23, …) | all doses, stronger at high dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.590×** | -13.4 | 6e-39 | 41/48 (A-172, A549, …) | top dose only | cell-cycle shift (explains ~5% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.479×** | -13.2 | 4e-38 | 32/48 (NCI-H23, RPMI-7951, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.515×** | -11.9 | 6e-31 | 43/47 (NCI-H23, BT-474, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.522×** | -11.7 | 8e-30 | 44/47 (NCI-H23, SNU-423, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **0.634×** | -11.5 | 4e-29 | 32/47 (SNU-423, NCI-H2347, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib (drug)]] 5 µM |  | **0.374×** | -9.3 | 9e-19 | 33/47 (RPMI-7951, C-33 A, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.644×** | -7.6 | 1e-12 | 32/46 (LoVo, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Brivudine (drug)]] 5 µM |  | **0.471×** | -7.1 | 5e-11 | 39/48 (A549, C-33 A, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 626. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H23 (line)]] | alt | 663 | 0 | 21 (5 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.112× (z -25.1) |
| [[A549 (line)]] | wt | 600 | 0 | 20 (4 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.118× (z -24.7) |
| [[LoVo (line)]] | wt | 513 | 0 | 20 (3 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.119× (z -28.7) |
| [[RKO (line)]] | wt | 444 | 0 | 19 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.128× (z -30.0) |
| [[HepG2_C3A (line)]] | wt | 422 | 0 | 18 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -19.8) |
| [[NCI-H1792 (line)]] | alt | 296 | 0 | 18 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.273× (z -20.7) |
| [[BT-474 (line)]] | alt | 303 | 0 | 17 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.181× (z -19.0) |
| [[RPMI-7951 (line)]] | alt | 639 | 0 | 17 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.266× (z -26.1) |
| [[SNU-423 (line)]] | alt | 448 | 0 | 17 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.261× (z -22.4) |
| [[A-172 (line)]] | wt | 485 | 0 | 16 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.292× (z -22.0) |
| [[C-33 A (line)]] | alt | 624 | 0 | 16 (2 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.160× (z -21.9) |
| [[NCI-H1573 (line)]] | alt | 428 | 0 | 16 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.299× (z -20.6) |
| [[A498 (line)]] | wt | 423 | 0 | 14 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.284× (z -20.6) |
| [[MIA PaCa-2 (line)]] | alt | 626 | 0 | 14 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.285× (z -20.8) |
| [[COLO 205 (line)]] | alt | 568 | 0 | 13 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.251× (z -21.0) |
| [[KATO III (line)]] | alt | 425 | 0 | 13 (1 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.154× (z -22.5) |
| [[NCI-H2347 (line)]] | alt | 372 | 3 (1 ⚠) | 10 | [[Harringtonine (drug)]] 5 µM 2.08× (z +9.4) ⚠ cell-cycle shift, explains ~15% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 2.02× (z +9.3) | [[Tofacitinib (drug)]] 5 µM 0.340× (z -20.1) |
| [[CFPAC-1 (line)]] | alt | 449 | 0 | 12 | — | [[Tofacitinib (drug)]] 5 µM 0.260× (z -24.6) |
| [[HS-578T (line)]] | alt | 272 | 0 | 12 (1 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.230× (z -17.1) |
| [[AsPC-1 (line)]] | alt | 426 | 0 | 11 | — | [[Panobinostat (drug)]] 5 µM 0.183× (z -19.4) |
| [[Hs 766T (line)]] | wt | 263 | 0 | 11 | — | [[Panobinostat (drug)]] 0.5 µM 0.255× (z -14.9) |
| [[Panc 03.27 (line)]] | alt | 385 | 0 | 11 | — | [[Tofacitinib (drug)]] 5 µM 0.378× (z -17.0) |
| [[CHP-212 (line)]] | wt | 322 | 0 | 10 | — | [[Panobinostat (drug)]] 5 µM 0.135× (z -15.5) |
| [[NCI-H460 (line)]] | wt | 128 | 2 (2 ⚠) | 8 (1 ⚠) | [[Dinaciclib (drug)]] 5 µM 2.60× (z +13.1) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Homoharringtonine (drug)]] 5 µM 0.354× (z -20.8) |
| [[SHP-77 (line)]] | alt | 291 | 0 | 10 | — | [[Belinostat (drug)]] 5 µM 0.164× (z -18.8) |
| [[HEC-1-A (line)]] | alt | 189 | 6 (4 ⚠) | 3 | [[Auranofin (drug)]] 5 µM 1.98× (z +12.1) | [[Panobinostat (drug)]] 5 µM 0.490× (z -12.6) |
| [[SNU-1 (line)]] | wt | 329 | 0 | 9 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.246× (z -12.6) |
| [[SW1417 (line)]] | alt | 342 | 0 | 9 | — | [[Panobinostat (drug)]] 0.5 µM 0.274× (z -16.1) |
| [[PANC-1 (line)]] | alt | 205 | 0 | 8 | — | [[Homoharringtonine (drug)]] 5 µM 0.264× (z -25.4) |
| [[SK-MEL-2 (line)]] | alt | 338 | 0 | 8 | — | [[Panobinostat (drug)]] 0.5 µM 0.252× (z -16.0) |
| [[J82 (line)]] | alt | 179 | 3 (3 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 4.13× (z +14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.388× (z -13.3) |
| [[LOX-IMVI (line)]] | wt | 189 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.364× (z -13.5) |
| [[SW 900 (line)]] | alt | 286 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.380× (z -13.7) |
| [[SW480 (line)]] | alt | 135 | 2 (2 ⚠) | 4 | [[Dinaciclib (drug)]] 5 µM 3.11× (z +16.8) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | [[Panobinostat (drug)]] 5 µM 0.291× (z -18.8) |
| [[C32 (line)]] | wt | 178 | 0 | 5 | — | [[Belinostat (drug)]] 5 µM 0.314× (z -10.8) |
| [[HOP62 (line)]] | alt | 99.7 | 2 (2 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 3.06× (z +12.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.446× (z -12.7) |
| [[A-427 (line)]] | wt | 223 | 0 | 4 | — | [[Belinostat (drug)]] 5 µM 0.416× (z -12.4) |
| [[HT-29 (line)]] | alt | 130 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.534× (z -11.1) |
| [[LS 180 (line)]] | wt | 136 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.04× (z +9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.346× (z -14.4) |
| [[SW48 (line)]] | wt | 144 | 1 (1 ⚠) | 3 | [[Dinaciclib (drug)]] 0.5 µM 2.51× (z +9.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Panobinostat (drug)]] 5 µM 0.282× (z -12.4) |
| [[NCI-H2030 (line)]] | alt | 123 | 1 (1 ⚠) | 2 | [[Dinaciclib (drug)]] 0.5 µM 2.31× (z +9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.414× (z -14.1) |
| [[HCT15 (line)]] | alt | 188 | 0 | 1 | — | [[Panobinostat (drug)]] 5 µM 0.396× (z -9.8) |
| [[hTERT-HPNE (line)]] | wt | 125 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.491× (z -9.5) |
| [[SW 1271 (line)]] | alt | 178 | 0 | 1 | — | [[4EGI-1 (drug)]] 5 µM 0.0507× (z -9.0) |
| [[AN3 CA (line)]] | alt | 155 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 64.6 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 198 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 228 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 128 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 125 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 626), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PARP9]] | +0.94 | +0.89 / +0.95 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 774 |
| [[MX1]] | +0.91 | +0.83 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 979 |
| [[PARP14]] | +0.90 | +0.85 / +0.93 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 672 |
| [[OAS3]] | +0.89 | +0.84 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 959 |
| [[OAS2]] | +0.89 | +0.79 / +0.92 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 934 |
| [[OAS1]] | +0.89 | +0.82 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 929 |
| [[IFI44]] | +0.89 | +0.80 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 951 |
| [[HERC6]] | +0.88 | +0.82 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 802 |
| [[STAT1]] | +0.88 | +0.83 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 980 |
| [[IFI35]] | +0.88 | +0.81 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 722 |
| [[CMPK2]] | +0.88 | +0.77 / +0.91 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 745 |
| [[IFIT1]] | +0.87 | +0.80 / +0.88 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE; STRING 993 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*40 arrows, 40 of them with an alert ⚠; grade A 0, B 30, C 10. Shown: the 12 strongest; 28 more arrows (28 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[OAS2]] | B | OAS2 activity raises EIF2AK2's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.01× lower at baseline in the lines without OAS2 | 6e-04 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[IFI6]] | B | IFI6 activity raises EIF2AK2's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.46× lower at baseline in the lines without IFI6 | 0.002 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises EIF2AK2's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.01× lower at baseline in the lines without BATF2 | 0.002 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises EIF2AK2's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.18× lower at baseline in the lines without OAS1 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[CMPK2]] | B | CMPK2 activity raises EIF2AK2's level | lines that do not express CMPK2 (11) vs lines expressing it (39) | 2.13× lower at baseline in the lines without CMPK2 | 0.003 | ⚠ within organs, on part of the lines; also absent: OAS2, NRIR, OAS1 |
| [[PARP9]] | B | PARP9 activity raises EIF2AK2's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.35× lower at baseline in the lines without PARP9 | 0.004 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[PLSCR1]] | B | PLSCR1 activity raises EIF2AK2's level | lines that do not express PLSCR1 (8) vs lines expressing it (42) | 2.21× lower at baseline in the lines without PLSCR1 | 0.007 | ⚠ within organs, on part of the lines; also absent: PARP9, ENSG00000279320, IFI6; maybe low, not absent |
| [[RASGRP3]] | B | RASGRP3 activity raises EIF2AK2's level | lines that do not express RASGRP3 (16) vs lines expressing it (34) | 2.01× lower at baseline in the lines without RASGRP3 | 0.008 | ⚠ within organs, on part of the lines; also absent: IFI6, SLC15A3, GBP4; maybe low, not absent |
| [[FBXO39]] | B | FBXO39 activity raises EIF2AK2's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 1.72× lower at baseline in the lines without FBXO39 | 0.011 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[MX1]] | B | MX1 activity raises EIF2AK2's level | lines that do not express MX1 (19) vs lines expressing it (31) | 1.91× lower at baseline in the lines without MX1 | 0.014 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[PARP9]] | B | PARP9 activity strengthens EIF2AK2's drug response | lines that do not express PARP9 (7) vs lines expressing it (41) | the lines without PARP9 respond 0.45× as strongly (z diff +2.82); strongest at Fedratinib (hydrochloride hydrate) 5 µM: 0.93x vs 0.48x (z diff +6.0) | 0.014 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent; target measured in part of the lines |
| [[TRIM22]] | B | TRIM22 activity raises EIF2AK2's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.61× lower at baseline in the lines without TRIM22 | 0.023 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |

### Downstream of this gene

*46 arrows, 46 of them with an alert ⚠; grade A 0, B 0, C 46. Shown: the 12 strongest; 34 more arrows (34 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAR]] | C | EIF2AK2's natural level strengthens ADAR's drug response | EIF2AK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.89, reverse +0.66; direction not clear | 3e-07 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PML]] | C | EIF2AK2's natural level strengthens PML's drug response | EIF2AK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.89, reverse +0.48; direction not clear | 5e-07 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IRF9]] | C | EIF2AK2's natural level strengthens IRF9's drug response | EIF2AK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.87, reverse +0.58; direction not clear | 2e-06 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TDRD7]] | C | EIF2AK2's natural level strengthens TDRD7's drug response | EIF2AK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.42; direction not clear | 2e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | EIF2AK2's natural level strengthens TRIM25's drug response | EIF2AK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.66; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | EIF2AK2's natural level strengthens HELZ2's drug response | EIF2AK2's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.67; direction not clear | 3e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | EIF2AK2's natural level strengthens USP18's drug response | EIF2AK2's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.86, reverse +0.41; direction not clear | 4e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | EIF2AK2's natural level strengthens IFIT5's drug response | EIF2AK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.83, reverse +0.56; direction not clear | 5e-05 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM14]] | C | EIF2AK2's natural level strengthens TRIM14's drug response | EIF2AK2's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.63; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PNPT1]] | C | EIF2AK2's natural level strengthens PNPT1's drug response | EIF2AK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.82, reverse +0.70; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[CMTR1]] | C | EIF2AK2's natural level strengthens CMTR1's drug response | EIF2AK2's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.81, reverse +0.42; direction not clear | 1e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFI35]] | C | EIF2AK2's natural level strengthens IFI35's drug response | EIF2AK2's natural level across 43 lines (lineage-adjusted; a glimpse) | r +0.84, reverse +0.46; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.914). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (48.5, 54.3); signed map (64.9, 32.3). **Vector** length 146, 61.2% of its response variance represented; |z| ≥ 3 in 2,002 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *interferon* (control, mean cos +0.84 to 23); *Interferon gamma signaling* (reactome, mean cos +0.76 to 17); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.78 to 10).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +9.1 | +4.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +8.2 | +5.2 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +6.9 | -4.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +6.5 | +2.7 |
|  | [[Cobimetinib (drug)]] 0.5 µM |  | +5.0 | +4.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +4.7 | +3.2 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | +4.7 | +3.6 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +4.6 | +1.0 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -11.4 | -22.2 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -10.3 | -17.1 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -10.0 | -13.5 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -9.9 | -14.1 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -8.0 | -13.2 |

## What is on record

|  |  |
|---|---|
| Name | eukaryotic translation initiation factor 2 alpha kinase 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p22.2 — chr2:37,099,210-37,157,522 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PKR, PPP1R83; previously PRKR |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; Eukaryotic translation initiation factor 2 alpha kinases |
| Hallmark sets | INTERFERON_ALPHA_RESPONSE, INFLAMMATORY_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 15 pathways, smallest: SUMOylation of immune response proteins; Evasion by RSV of host interferon responses; NS1 Mediated Effects on Host Pathways |
| Matched by | ensembl_id |

**Function**, from UniProt [P19525](https://www.uniprot.org/uniprotkb/P19525) (Interferon-induced, double-stranded RNA-activated protein kinase):

> IFN-induced dsRNA-dependent serine/threonine-protein kinase that phosphorylates the alpha subunit of eukaryotic translation initiation factor 2 (EIF2S1/eIF-2-alpha) and plays a key role in the innate immune response to viral infection. Inhibits viral replication via the integrated stress response (ISR): EIF2S1/eIF-2-alpha phosphorylation in response to viral infection converts EIF2S1/eIF-2-alpha into a global protein synthesis inhibitor, resulting to a shutdown of cellular and viral protein …

**Summary**, from NCBI Gene [5610](https://www.ncbi.nlm.nih.gov/gene/5610):

> The protein encoded by this gene is a serine/threonine protein kinase that is activated by autophosphorylation after binding to dsRNA. The activated form of the encoded protein can phosphorylate translation initiation factor EIF2S1, which in turn inhibits protein synthesis. This protein is also activated by manganese ions and heparin. The encoded protein plays an important role in the innate immune response against multiple DNA and RNA viruses. [provided by RefSeq, Jul 2021]

**Accessions** — [HGNC:9437](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9437) · Entrez [5610](https://www.ncbi.nlm.nih.gov/gene/5610) · UniProt [P19525](https://www.uniprot.org/uniprotkb/P19525) · Ensembl [ENSG00000055332](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000055332)

## Data

Gene col 626: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 626); `tables/drug_effects.parquet` (67 rows, flagged included); `relations/gene_relations.parquet` (col_a == 626, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 626]; `tensor/DDL_lfc|DDL_z.npy` [626]; `embed/gene_vectors.npy` [626]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 626 or target_col == 626). Every well: [[EIF2AK2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EIF2AK2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
