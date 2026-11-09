---
symbol: "FAM13A"
type: "gene"
col: 6200
ensembl_id: "ENSG00000138640"
name: "family with sequence similarity 13 member A"
location: "4q22.1"
module: 79
arm: "+"
pooled_cpm: 310.42
n_lines_expressing: 44
n_dd_up: 10
n_dd_down: 41
n_dd_up_clean: 8
n_dd_down_clean: 21
in_vector_space: true
direction_upstream: 7
direction_downstream: 13
tags: ["gene", "module/079"]
generated_by: "tahoemap"
---

# FAM13A

*family with sequence similarity 13 member A* — 4q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (2 with an alert ⚠); the strongest is [[NG25 (drug)]] 5 µM: 1.98× (z +5.0, q 3e-04, up in 35 of 41 measured lines).
> Pooled over the cell lines (median), lowered significantly by 41 drug-doses (20 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.273× (z -25.6, q 0e+00, down in 39 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MXI1]] (+0.77, fdr 7e-06), [[HERC3]] (+0.76, fdr 7e-06, ⚠ same locus), [[PDK3]] (+0.76, fdr 7e-06), [[P4HA1]] (+0.75, fdr 7e-06); moves opposite to [[AVEN]] (-0.60, fdr 1e-05), [[ACOT9]] (-0.57, fdr 1e-05), [[PTPN21]] (-0.56, fdr 1e-05).
> It is in [[Module 079]], a single-armed module (hypoxia).
> Probable direction (from the cell lines, not proof of direct regulation): 7 arrows point to it, the strongest [[RAB20]] → it (grade B ⚠); 13 go from it, the strongest it → [[XPNPEP1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6200.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[NG25 (drug)]] 5 µM |  | **1.98×** | +5.0 | 3e-04 | 35/41 (LoVo, NCI-H23, …) | top dose only | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[PF-06260933 (drug)]] 5 µM |  | **1.77×** | +4.2 | 0.006 | 27/42 (SHP-77, A-172, …) | top dose only | noisy plate (z scaled) |
| [[Dimethyl fumarate (drug)]] 5 µM |  | **1.40×** | +4.2 | 0.006 | 26/43 (HEC-1-A, A549, …) | top dose only | plate-row cell shift |
| [[Tucidinostat (drug)]] 5 µM |  | **1.21×** | +3.8 | 0.021 | 20/42 (KATO III, COLO 205, …) | rises with dose |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.36×** | +3.7 | 0.021 | 29/43 (SNU-1, AN3 CA, …) | top dose only |  |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.30×** | +3.7 | 0.021 | 22/43 (COLO 205, NCI-H1792, …) | rises with dose |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **1.41×** | +3.4 | 0.050 | 24/42 (NCI-H2347, HOP62, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fumaric acid (drug)]] 5 µM |  | **1.30×** | +3.2 | 0.088 | 20/43 (HT-29, CHP-212, …) | top dose only | plate-row cell shift |
| [[Bexarotene (drug)]] 5 µM |  | **1.25×** | +3.1 | 0.100 | 21/42 (HT-29, NCI-H460, …) | top dose only |  |
| [[Cobimetinib (drug)]] 5 µM |  | **1.29×** | +3.1 | 0.100 | 20/41 (NCI-H23, LoVo, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 45 in all, 21 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 41 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 20 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6200.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.273×** | -25.6 | 0e+00 | 39/42 (NCI-H1573, SHP-77, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.288×** | -17.4 | 0e+00 | 40/42 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.291×** | -17.2 | 0e+00 | 42/43 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.436×** | -16.4 | 0e+00 | 42/43 (A549, SHP-77, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.271×** | -15.9 | 0e+00 | 41/42 (NCI-H1573, A549, …) | rises with dose | cell-cycle shift (explains ~1% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.275×** | -15.7 | 0e+00 | 36/38 (CFPAC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.333×** | -14.2 | 1e-43 | 38/39 (NCI-H2347, CFPAC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.320×** | -13.9 | 5e-42 | 41/41 (NCI-H1573, A549, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.438×** | -11.5 | 7e-29 | 36/42 (SHP-77, CFPAC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.448×** | -11.2 | 3e-27 | 37/42 (hTERT-HPNE, NCI-H1792, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.423×** | -10.5 | 5e-24 | 40/41 (NCI-H1573, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.543×** | -7.4 | 5e-12 | 37/42 (hTERT-HPNE, SNU-423, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.687×** | -7.4 | 6e-12 | 41/42 (NCI-H2347, HepG2/C3A, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.608×** | -6.9 | 2e-10 | 38/42 (NCI-H1792, NCI-H2347, …) | inconsistent across doses |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | **0.623×** | -6.6 | 2e-09 | 30/42 (SHP-77, hTERT-HPNE, …) | rises with dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.674×** | -5.5 | 1e-06 | 27/42 (C32, A498, …) | top dose only |  |
| [[Peretinoin (drug)]] 0.5 µM |  | **0.708×** | -4.8 | 5e-05 | 29/41 (NCI-H23, AsPC-1, …) | two highest doses |  |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.713×** | -4.7 | 7e-05 | 30/42 (NCI-H2347, A549, …) | all doses, flat |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.717×** | -4.6 | 1e-04 | 23/42 (NCI-H460, A-172, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[TAK-733 (drug)]] 5 µM |  | **0.575×** | -4.0 | 0.001 | 25/42 (AsPC-1, SW 900, …) | rises with dose | noisy plate (z scaled) |
| [[Peretinoin (drug)]] 5 µM |  | **0.724×** | -3.9 | 0.002 | 26/41 (A-172, NCI-H2347, …) | two highest doses |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.756×** | -3.9 | 0.002 | 26/42 (HT-29, HEC-1-A, …) | top dose only |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.727×** | -3.9 | 0.002 | 26/42 (NCI-H2347, NCI-H1573, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.619×** | -3.5 | 0.009 | 25/42 (NCI-H2347, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.782×** | -3.4 | 0.012 | 23/43 (HS-578T, NCI-H2347, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.51 per unit of S-phase module lfc, +0.13 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6200. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H2347 (line)]] | alt | 684 | 0 | 18 (12 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0784× (z -27.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.184× (z -25.4) |
| [[CFPAC-1 (line)]] | alt | 787 | 0 | 13 (9 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0594× (z -27.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.170× (z -24.5) |
| [[hTERT-HPNE (line)]] | wt | 829 | 0 | 13 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0872× (z -27.2) |
| [[NCI-H1792 (line)]] | alt | 750 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -27.9) |
| [[SHP-77 (line)]] | alt | 487 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0963× (z -31.7) |
| [[NCI-H1573 (line)]] | alt | 959 | 0 | 11 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0764× (z -33.6) |
| [[NCI-H460 (line)]] | wt | 378 | 0 | 11 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.292× (z -19.4) |
| [[A549 (line)]] | wt | 319 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.157× (z -25.9) |
| [[CHP-212 (line)]] | wt | 951 | 0 | 10 (7 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.210× (z -17.0) |
| [[HT-29 (line)]] | alt | 325 | 0 | 10 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.269× (z -17.0) |
| [[BT-474 (line)]] | alt | 253 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.224× (z -15.2) |
| [[HOP62 (line)]] | alt | 867 | 0 | 9 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.131× (z -20.1) |
| [[KATO III (line)]] | alt | 256 | 1 | 8 (4 ⚠) | [[Tucidinostat (drug)]] 5 µM 2.06× (z +8.6) | [[Homoharringtonine (drug)]] 5 µM 0.102× (z -27.0) |
| [[SW 900 (line)]] | alt | 507 | 0 | 9 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.189× (z -19.9) |
| [[LoVo (line)]] | wt | 236 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.302× (z -22.0) |
| [[NCI-H23 (line)]] | alt | 162 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -19.5) |
| [[Panc 03.27 (line)]] | alt | 177 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.427× (z -11.0) |
| [[SNU-423 (line)]] | alt | 169 | 0 | 8 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -23.0) |
| [[A498 (line)]] | wt | 382 | 0 | 7 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.320× (z -18.1) |
| [[AsPC-1 (line)]] | alt | 348 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -19.7) |
| [[HepG2_C3A (line)]] | wt | 194 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.235× (z -13.0) |
| [[MIA PaCa-2 (line)]] | alt | 134 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.288× (z -11.2) |
| [[RPMI-7951 (line)]] | alt | 320 | 0 | 7 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.168× (z -16.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.160× (z -15.6) |
| [[SK-MEL-2 (line)]] | alt | 250 | 0 | 7 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.372× (z -14.9) |
| [[HS-578T (line)]] | alt | 191 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.351× (z -12.9) |
| [[A-172 (line)]] | wt | 128 | 0 | 5 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.195× (z -13.1) |
| [[AN3 CA (line)]] | alt | 332 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.141× (z -21.3) |
| [[H4 (line)]] | wt | 766 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.230× (z -15.0) |
| [[LS 180 (line)]] | wt | 577 | 0 | 5 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -17.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.406× (z -11.1) |
| [[PANC-1 (line)]] | alt | 123 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -28.2) |
| [[HEC-1-A (line)]] | alt | 177 | 0 | 4 (2 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.387× (z -10.3) |
| [[Hs 766T (line)]] | wt | 150 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -16.5) |
| [[NCI-H2030 (line)]] | alt | 90.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.318× (z -14.6) |
| [[C32 (line)]] | wt | 144 | 0 | 3 | — | [[Homoharringtonine (drug)]] 5 µM 0.390× (z -13.8) |
| [[COLO 205 (line)]] | alt | 109 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.138× (z -12.7) |
| [[HCT15 (line)]] | alt | 152 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.382× (z -9.2) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.512× (z -9.0) |
| [[SNU-1 (line)]] | wt | 306 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.290× (z -11.1) |
| [[C-33 A (line)]] | alt | 191 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.319× (z -10.4) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 180 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -9.7) |
| [[SW 1088 (line)]] | alt | 757 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0553× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.138× (z -13.4) |
| [[SW 1271 (line)]] | alt | 217 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.115× (z -9.0) |
| [[A-427 (line)]] | wt | 29.7 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 96.5 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 76.9 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 558 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 423 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 39.2 n.m. | — | — | — | — |
| [[SW1417 (line)]] | alt | 41.8 n.m. | — | — | — | — |
| [[SW48 (line)]] | wt | 48.7 n.m. | — | — | — | — |
| [[SW480 (line)]] | alt | 30.5 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6200), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MXI1]] | +0.77 | +0.81 / +0.69 | both halves | 7e-06 |  |
| [[HERC3]] | +0.76 | +0.80 / +0.66 | both halves | 7e-06 | STRING 578; ⚠ same locus (17.4 kb: neighbours can correlate without regulation) |
| [[PDK3]] | +0.76 | +0.79 / +0.69 | both halves | 7e-06 |  |
| [[P4HA1]] | +0.75 | +0.78 / +0.68 | both halves | 7e-06 |  |
| [[KDM3A]] | +0.74 | +0.77 / +0.67 | both halves | 7e-06 |  |
| [[INSIG2]] | +0.71 | +0.77 / +0.59 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.71 | +0.75 / +0.62 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.70 | +0.77 / +0.55 | both halves | 1e-05 |  |
| [[SAP30-DT]] | +0.70 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[PEX3]] | +0.69 | +0.72 / +0.55 | both halves | 1e-05 |  |
| [[ZNF292]] | +0.69 | +0.70 / +0.63 | both halves | 7e-06 |  |
| [[YEATS2]] | +0.69 | +0.74 / +0.59 | both halves | 7e-06 |  |
| [[DDIT4]] | +0.68 | +0.68 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AVEN]] | -0.60 | -0.63 / -0.54 | both halves | 1e-05 |  |
| [[ACOT9]] | -0.57 | -0.53 / -0.57 | both halves | 1e-05 |  |
| [[PTPN21]] | -0.56 | -0.55 / -0.56 | both halves | 1e-05 |  |
| [[GATAD2A]] | -0.56 | -0.45 / -0.63 | both halves | 3e-05 |  |
| [[MICALL1]] | -0.56 | -0.50 / -0.52 | both halves | 1e-05 |  |
| [[REXO1]] | -0.56 | -0.55 / -0.51 | both halves | 1e-05 |  |
| [[ARMC6]] | -0.55 | -0.50 / -0.50 | both halves | 1e-05 |  |
| [[KCTD13]] | -0.55 | -0.55 / -0.54 | both halves | 1e-05 |  |
| [[PCBD2]] | -0.55 | -0.51 / -0.52 | both halves | 1e-05 |  |
| [[PUS1]] | -0.54 | -0.56 / -0.50 | both halves | 1e-05 |  |
| [[PARVA]] | -0.54 | -0.53 / -0.44 | both halves | 3e-05 |  |
| [[CLCF1]] | -0.54 | -0.54 / -0.43 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*7 arrows, 7 of them with an alert ⚠; grade A 0, B 7, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[RAB20]] | B | RAB20 activity raises FAM13A's level | lines that do not express RAB20 (8) vs lines expressing it (42) | 2.69× lower at baseline in the lines without RAB20 | 0.011 | ⚠ within organs, on part of the lines; also absent: RPS6KA2, PRDX2, YPEL3; maybe low, not absent |
| [[MLLT3]] | B | MLLT3 activity raises FAM13A's level | lines that do not express MLLT3 (6) vs lines expressing it (44) | 2.61× lower at baseline in the lines without MLLT3 | 0.013 | ⚠ within organs, on part of the lines; also absent: KCNIP4, GCNT1, PTGFRN |
| [[DEPP1]] | B | DEPP1 activity raises FAM13A's level | lines that do not express DEPP1 (21) vs lines expressing it (29) | 2.38× lower at baseline in the lines without DEPP1 | 0.019 | ⚠ within organs, on part of the lines; co-occurs with SMARCA4; also absent: LOX, TNFAIP2, BST2 |
| [[NDRG1]] | B | NDRG1 activity raises FAM13A's level | lines that do not express NDRG1 (6) vs lines expressing it (44) | 2.46× lower at baseline in the lines without NDRG1 | 0.035 | ⚠ within organs, on part of the lines; also absent: SMOX, DELEC1, SLC2A1 |
| [[PAG1]] | B | PAG1 activity raises FAM13A's level | lines that do not express PAG1 (15) vs lines expressing it (35) | 2.13× lower at baseline in the lines without PAG1 | 0.073 | ⚠ within organs, on part of the lines; also absent: LINC02257, PALLD, TSC22D3 |
| [[TOP2A]] | B | TOP2A activity raises FAM13A's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 8.4% of all compounds | 0.084 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[EYA1]] | B | EYA1 activity raises FAM13A's level | lines that do not express EYA1 (29) vs lines expressing it (21) | 2.17× lower at baseline in the lines without EYA1 | 0.089 | ⚠ within organs, on part of the lines; also absent: ADAMTS3, ENSG00000233539, NAA11 |

### Downstream of this gene

*13 arrows, 13 of them with an alert ⚠; grade A 0, B 13, C 0. Shown: the 12 strongest; 1 more arrow (1 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[XPNPEP1]] | B | FAM13A activity raises XPNPEP1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.47× lower at baseline in the lines without FAM13A | 0.004 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| cells under [[TAK-901 (drug)]] 0.05 µM | B | FAM13A activity raises the cells' numbers under TAK-901 0.05 µM (protects the cells) | lines that do not express FAM13A (6) vs lines expressing it (42) | the lines without FAM13A: 0.69× the cells of the other lines | 0.018 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[NDRG1]] | B | FAM13A activity raises NDRG1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 2.58× lower at baseline in the lines without FAM13A | 0.033 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[MLLT3]] | B | FAM13A activity raises MLLT3's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.88× lower at baseline in the lines without FAM13A | 0.034 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[MYLIP]] | B | FAM13A activity raises MYLIP's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without FAM13A | 0.036 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[ANG]] | B | FAM13A activity raises ANG's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.71× lower at baseline in the lines without FAM13A | 0.051 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[SH3RF1]] | B | FAM13A activity raises SH3RF1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.59× lower at baseline in the lines without FAM13A | 0.060 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[NFIL3]] | B | FAM13A activity raises NFIL3's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.77× lower at baseline in the lines without FAM13A | 0.064 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[GBE1]] | B | FAM13A activity raises GBE1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 2.12× lower at baseline in the lines without FAM13A | 0.073 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[RBPJ]] | B | FAM13A activity raises RBPJ's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.42× lower at baseline in the lines without FAM13A | 0.080 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[SRP54-AS1]] | B | FAM13A activity lowers SRP54-AS1's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.27× higher at baseline in the lines without FAM13A | 0.084 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |
| [[RORA]] | B | FAM13A activity raises RORA's level | lines that do not express FAM13A (6) vs lines expressing it (44) | 1.74× lower at baseline in the lines without FAM13A | 0.094 | ⚠ within organs, on part of the lines; also absent: ZNF14, DDX60, UBA7 |

## Where it sits

- **Module**: [[Module 079]] — hypoxia; 57 genes; every member is in the + arm (projection on the module's main direction 0.820). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.34; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (11.7, -16.8); signed map (-35.3, 23.8). **Vector** length 131, 48.9% of its response variance represented; |z| ≥ 3 in 1,622 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *hypoxia* (hallmark, mean cos +0.61 to 16); *hypoxia* (control, mean cos +0.64 to 5); *glycolysis* (hallmark, mean cos +0.64 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +8.6 | +3.8 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | +7.3 | +3.7 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +6.5 | -1.0 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~57% of this change | +5.4 | -6.6 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.5 | -11.5 |
|  | [[Brivudine (drug)]] 5 µM |  | +3.8 | +0.4 |
|  | [[Terfenadine (drug)]] 5 µM |  | +3.6 | +2.2 |
|  | [[Betamethasone dipropionate (drug)]] 5 µM |  | +3.6 | +1.5 |
|  | [[Verteporfin (drug)]] 5 µM |  | +3.6 | +3.7 |
| fall | [[5-Azacytidine (drug)]] 5 µM |  | -6.0 | -3.9 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -4.7 | -3.6 |
|  | [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | -4.7 | -3.1 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -4.5 | -13.9 |
|  | [[Peretinoin (drug)]] 5 µM |  | -4.3 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -4.3 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -4.1 | -4.7 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -4.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 13 member A |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q22.1 — chr4:88,725,955-89,111,398 (-) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0914, ARHGAP48; previously FAM13A1 |
| Gene groups (HGNC) | Rho GTPase activating proteins |
| Reactome | 5 pathways, smallest: RHOA GTPase cycle; RAC1 GTPase cycle; RHO GTPase cycle |
| Matched by | ensembl_id |

UniProt [O94988](https://www.uniprot.org/uniprotkb/O94988) carries no function annotation.

**Summary**, from NCBI Gene [10144](https://www.ncbi.nlm.nih.gov/gene/10144):

> Predicted to enable GTPase activator activity. Predicted to be involved in regulation of small GTPase mediated signal transduction. Predicted to be located in cytosol. Implicated in chronic obstructive pulmonary disease. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:19367](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19367) · Entrez [10144](https://www.ncbi.nlm.nih.gov/gene/10144) · UniProt [O94988](https://www.uniprot.org/uniprotkb/O94988) · Ensembl [ENSG00000138640](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000138640)

## Data

Gene col 6200: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6200); `tables/drug_effects.parquet` (55 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6200, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6200]; `tensor/DDL_lfc|DDL_z.npy` [6200]; `embed/gene_vectors.npy` [6200]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6200 or target_col == 6200). Every well: [[FAM13A — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM13A.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
