---
symbol: "IRF9"
type: "gene"
col: 13150
ensembl_id: "ENSG00000213928"
name: "interferon regulatory factor 9"
location: "14q12"
module: 32
arm: "+"
pooled_cpm: 51.14
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 27
in_vector_space: true
direction_upstream: 71
direction_downstream: 26
tags: ["gene", "module/032"]
generated_by: "tahoemap"
---

# IRF9

*interferon regulatory factor 9* — 14q12

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 2.22×, MIA PaCa-2 1.97×, KATO III 1.88×, CFPAC-1 1.72×; ⚠ cell-cycle shift, explains ~23% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H2347 2.16×, MIA PaCa-2 3.03×, HS-578T 3.75×; ⚠ cell-cycle shift, explains ~45% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 2.64×, KATO III 2.47×; ⚠ cell-cycle shift, would explain all of this change).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (11 with an alert ⚠); the strongest is [[Belinostat (drug)]] 5 µM: 0.328× (z -20.2, q 0e+00, down in 40 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SP110]] (+0.88, fdr 7e-06), [[HELZ2]] (+0.86, fdr 7e-06), [[MX1]] (+0.86, fdr 7e-06).
> It is in [[Module 032]], a single-armed module (interferon alpha response).
> Probable direction (from the cell lines, not proof of direct regulation): 71 arrows point to it, the strongest [[IFI6]] → it (grade B ⚠); 26 go from it, the strongest it → [[ADAR]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 1 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13150.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 3 here, 3 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 4 lines (NCI-H2347 2.22×, MIA PaCa-2 1.97×, KATO III 1.88×, CFPAC-1 1.72×; ⚠ cell-cycle shift, explains ~23% of this change); [[Homoharringtonine (drug)]] 0.5 µM in 3 lines (NCI-H2347 2.16×, MIA PaCa-2 3.03×, HS-578T 3.75×; ⚠ cell-cycle shift, explains ~45% of this change); [[Harringtonine (drug)]] 5 µM in 2 lines (NCI-H2347 2.64×, KATO III 2.47×; ⚠ cell-cycle shift, would explain all of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Anethole trithione (drug)]] 0.05 µM |  | 1.20× | +3.3 | 0.55 | 13/48 (Panc 03.27, RKO, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 15 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13150.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Belinostat (drug)]] 5 µM |  | **0.328×** | -20.2 | 0e+00 | 40/48 (NCI-H2347, RPMI-7951, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here); position effect removed |
| [[Tofacitinib (drug)]] 5 µM |  | **0.465×** | -19.5 | 0e+00 | 39/48 (BT-474, NCI-H2347, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM |  | **0.390×** | -17.0 | 0e+00 | 37/48 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~23% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change | **0.409×** | -15.5 | 0e+00 | 30/38 (LoVo, BT-474, …) | all doses, stronger at high dose | composition shift |
| [[Tofacitinib (citrate) (drug)]] 5 µM |  | **0.547×** | -15.4 | 0e+00 | 37/49 (BT-474, NCI-H2347, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.458×** | -14.1 | 3e-43 | 39/48 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.479×** | -13.3 | 2e-38 | 39/48 (BT-474, SNU-423, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.480×** | -13.3 | 3e-38 | 42/48 (NCI-H2347, NCI-H23, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change | **0.481×** | -13.2 | 5e-38 | 38/46 (COLO 205, CFPAC-1, …) | all doses, stronger at high dose | composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.511×** | -11.6 | 1e-29 | 33/47 (SNU-423, NCI-H23, …) | rises with dose | cell-cycle shift (explains ~20% here); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.532×** | -11.4 | 3e-28 | 40/47 (NCI-H2347, RKO, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.643×** | -11.3 | 1e-27 | 32/48 (NCI-H1792, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~19% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.646×** | -11.1 | 3e-27 | 40/48 (RPMI-7951, CFPAC-1, …) | rises with dose |  |
| [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | **0.557×** | -10.6 | 2e-24 | 35/48 (BT-474, RKO, …) | all doses, stronger at high dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.568×** | -9.8 | 3e-21 | 34/46 (NCI-H23, BT-474, …) | top dose only | cell-cycle shift (explains ~18% here); position effect removed |
| [[Selinexor (drug)]] 5 µM |  | **0.694×** | -9.3 | 4e-19 | 31/48 (NCI-H2347, SNU-423, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.604×** | -9.1 | 3e-18 | 38/48 (BT-474, RKO, …) | rises with dose |  |
| [[Brivudine (drug)]] 5 µM |  | **0.412×** | -8.4 | 2e-15 | 33/48 (NCI-H2347, NCI-H1792, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.36 per unit of S-phase module lfc, +0.02 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13150. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 114 | 0 | 22 (6 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.159× (z -24.8) |
| [[NCI-H2347 (line)]] | alt | 139 | 3 (3 ⚠) | 18 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.22× (z +17.3) ⚠ cell-cycle shift, explains ~23% of this change | [[Belinostat (drug)]] 5 µM 0.207× (z -24.5) |
| [[CFPAC-1 (line)]] | alt | 127 | 1 (1 ⚠) | 14 (4 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.72× (z +9.5) ⚠ cell-cycle shift, explains ~23% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.167× (z -22.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.327× (z -14.0) |
| [[MIA PaCa-2 (line)]] | alt | 94.2 | 2 (2 ⚠) | 13 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.03× (z +11.5) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.141× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.342× (z -15.8) |
| [[RKO (line)]] | wt | 68.3 | 0 | 15 (3 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.194× (z -17.8) |
| [[NCI-H1792 (line)]] | alt | 71.2 | 0 | 14 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.109× (z -19.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.180× (z -15.8) |
| [[NCI-H23 (line)]] | alt | 76.6 | 0 | 14 (5 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.165× (z -17.0) |
| [[RPMI-7951 (line)]] | alt | 85.6 | 0 | 14 (4 ⚠) | — | [[Belinostat (drug)]] 5 µM 0.149× (z -18.4) |
| [[SNU-423 (line)]] | alt | 64.9 | 0 | 14 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.115× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.184× (z -15.2) |
| [[HS-578T (line)]] | alt | 45.2 | 1 (1 ⚠) | 11 (4 ⚠) | [[Homoharringtonine (drug)]] 0.5 µM 3.75× (z +11.3) ⚠ cell-cycle shift, explains ~45% of this change | [[Dinaciclib (drug)]] 0.5 µM 0.202× (z -13.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.233× (z -12.4) |
| [[C-33 A (line)]] | alt | 72.8 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -15.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.272× (z -14.4) |
| [[LoVo (line)]] | wt | 79.9 | 0 | 11 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0537× (z -30.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.293× (z -18.5) |
| [[COLO 205 (line)]] | alt | 111 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0718× (z -25.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Panobinostat (drug)]] 0.5 µM 0.212× (z -15.2) |
| [[SK-MEL-2 (line)]] | alt | 55.8 | 0 | 9 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.102× (z -19.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.199× (z -13.4) |
| [[A549 (line)]] | wt | 72.3 | 0 | 8 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.240× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.382× (z -13.6) |
| [[NCI-H1573 (line)]] | alt | 74.6 | 0 | 7 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.125× (z -18.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Panobinostat (drug)]] 5 µM 0.172× (z -16.5) |
| [[SHP-77 (line)]] | alt | 69.1 | 0 | 7 (2 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.238× (z -16.6) |
| [[SW 900 (line)]] | alt | 50.7 | 0 | 7 | — | [[Auranofin (drug)]] 5 µM 0.183× (z -13.0) |
| [[SW1417 (line)]] | alt | 65.8 | 0 | 7 (1 ⚠) | — | [[Tofacitinib (drug)]] 5 µM 0.353× (z -14.3) |
| [[CHP-212 (line)]] | wt | 64.7 | 0 | 6 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0916× (z -11.0) ⚠ toxic; cell-cycle shift, explains ~31% of this change · without an alert: [[Tofacitinib (citrate) (drug)]] 5 µM 0.249× (z -9.4) |
| [[KATO III (line)]] | alt | 65.1 | 2 (2 ⚠) | 4 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 1.88× (z +9.5) ⚠ cell-cycle shift, explains ~23% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -11.1) ⚠ cell-cycle shift, explains ~30% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.420× (z -9.2) |
| [[A-172 (line)]] | wt | 41.3 | 0 | 5 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0800× (z -21.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.148× (z -17.1) |
| [[A498 (line)]] | wt | 35.6 | 0 | 5 (1 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.235× (z -15.2) |
| [[C32 (line)]] | wt | 45.6 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.185× (z -11.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.316× (z -11.5) |
| [[Panc 03.27 (line)]] | alt | 71.4 | 0 | 5 | — | [[Tofacitinib (drug)]] 5 µM 0.442× (z -11.1) |
| [[AsPC-1 (line)]] | alt | 48.0 | 0 | 4 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.182× (z -15.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Belinostat (drug)]] 5 µM 0.291× (z -11.4) |
| [[HepG2_C3A (line)]] | wt | 49.8 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.108× (z -15.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~35% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.399× (z -9.0) |
| [[PANC-1 (line)]] | alt | 25.1 | 0 | 4 | — | [[Tofacitinib (drug)]] 5 µM 0.464× (z -10.2) |
| [[SNU-1 (line)]] | wt | 52.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.05 µM 0.128× (z -11.8) |
| [[A-427 (line)]] | wt | 19.9 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.115× (z -16.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[H4 (line)]] | wt | 28.2 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.106× (z -11.0) ⚠ toxic |
| [[Hs 766T (line)]] | wt | 43.6 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.220× (z -11.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change · without an alert: [[Tofacitinib (drug)]] 5 µM 0.447× (z -9.1) |
| [[AN3 CA (line)]] | alt | 17.6 | 0 | 1 (1 ⚠) | — | [[Rimonabant (Hydrochloride) (drug)]] 0.05 µM 0.0589× (z -8.7) ⚠ unreliable plate only |
| [[HCT15 (line)]] | alt | 39.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.201× (z -9.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[NCI-H2030 (line)]] | alt | 39.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.437× (z -11.0) ⚠ cell-cycle shift, explains ~23% of this change |
| [[SW48 (line)]] | wt | 16.7 | 0 | 1 | — | [[Tofacitinib (citrate) (drug)]] 0.5 µM 0.0404× (z -12.8) |
| [[SW480 (line)]] | alt | 14.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.145× (z -14.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~27% of this change |
| [[HEC-1-A (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 19.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 36.7 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 28.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 13.4 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 41.7 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 44.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 18.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 31.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 35.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13150), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SP110]] | +0.88 | +0.76 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 489 |
| [[HELZ2]] | +0.86 | +0.84 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 531 |
| [[MX1]] | +0.86 | +0.75 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 982 |
| [[PARP9]] | +0.86 | +0.73 / +0.90 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 843 |
| [[STAT1]] | +0.84 | +0.74 / +0.85 | both halves | 7e-06 | pathway: HALLMARK_IL6_JAK_STAT3_SIGNALING; STRING 999 |
| [[PARP10]] | +0.83 | +0.72 / +0.88 | both halves | 7e-06 |  |
| [[CMPK2]] | +0.83 | +0.66 / +0.89 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 474 |
| [[IFIH1]] | +0.83 | +0.67 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 896 |
| [[ZNFX1]] | +0.83 | +0.69 / +0.84 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_GAMMA_RESPONSE |
| [[PLSCR1]] | +0.83 | +0.70 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 482 |
| [[OAS1]] | +0.83 | +0.70 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 944 |
| [[USP18]] | +0.82 | +0.68 / +0.87 | both halves | 7e-06 | pathway: HALLMARK_INTERFERON_ALPHA_RESPONSE; STRING 773 |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*71 arrows, 71 of them with an alert ⚠; grade A 0, B 44, C 27. Shown: the 12 strongest; 59 more arrows (59 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[IFI6]] | B | IFI6 activity raises IRF9's level | lines that do not express IFI6 (13) vs lines expressing it (37) | 2.84× lower at baseline in the lines without IFI6 | 2e-04 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent |
| [[OAS1]] | B | OAS1 activity raises IRF9's level | lines that do not express OAS1 (13) vs lines expressing it (37) | 2.40× lower at baseline in the lines without OAS1 | 0.001 | ⚠ within organs, on part of the lines; also absent: OAS2, TRIM22, IFI27; maybe low, not absent |
| [[BATF2]] | B | BATF2 activity raises IRF9's level | lines that do not express BATF2 (13) vs lines expressing it (37) | 2.10× lower at baseline in the lines without BATF2 | 0.001 | ⚠ within organs, on part of the lines; also absent: RSAD2; maybe low, not absent |
| [[OAS2]] | B | OAS2 activity raises IRF9's level | lines that do not express OAS2 (14) vs lines expressing it (36) | 2.27× lower at baseline in the lines without OAS2 | 0.002 | ⚠ within organs, on part of the lines; also absent: OAS1, CMPK2, MX1 |
| [[FBXO39]] | B | FBXO39 activity raises IRF9's level | lines that do not express FBXO39 (16) vs lines expressing it (34) | 2.03× lower at baseline in the lines without FBXO39 | 0.003 | ⚠ within organs, on part of the lines; also absent: XAF1, TRIM22, SLC15A3 |
| [[MX1]] | B | MX1 activity raises IRF9's level | lines that do not express MX1 (19) vs lines expressing it (31) | 2.07× lower at baseline in the lines without MX1 | 0.005 | ⚠ within organs, on part of the lines; also absent: OAS2, SRMS, EPSTI1 |
| [[IFI27]] | B | IFI27 activity raises IRF9's level | lines that do not express IFI27 (21) vs lines expressing it (29) | 1.91× lower at baseline in the lines without IFI27 | 0.006 | ⚠ within organs, on part of the lines; also absent: TRIM22, OAS2, RSAD2 |
| [[SLC15A3]] | B | SLC15A3 activity raises IRF9's level | lines that do not express SLC15A3 (16) vs lines expressing it (34) | 1.85× lower at baseline in the lines without SLC15A3 | 0.010 | ⚠ within organs, on part of the lines; also absent: XAF1, MX2, GBP4 |
| [[PARP9]] | B | PARP9 activity raises IRF9's level | lines that do not express PARP9 (7) vs lines expressing it (43) | 2.41× lower at baseline in the lines without PARP9 | 0.010 | ⚠ within organs, on part of the lines; also absent: PLSCR1, OAS3, SRMS; maybe low, not absent |
| [[IFI6]] | B | IFI6 activity strengthens IRF9's drug response | lines that do not express IFI6 (13) vs lines expressing it (36) | the lines without IFI6 respond 0.24× as strongly (z diff +4.77); strongest at Panobinostat 5 µM: 0.90x vs 0.35x (z diff +7.1) | 0.012 | ⚠ within organs, on part of the lines; also absent: RASGRP3, MX1, IFITM1; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TRIM22]] | B | TRIM22 activity raises IRF9's level | lines that do not express TRIM22 (18) vs lines expressing it (32) | 1.94× lower at baseline in the lines without TRIM22 | 0.013 | ⚠ within organs, on part of the lines; also absent: CD5L, XAF1, IFITM1 |
| [[CCDC194]] | B | CCDC194 activity raises IRF9's level | lines that do not express CCDC194 (19) vs lines expressing it (31) | 1.71× lower at baseline in the lines without CCDC194 | 0.018 | ⚠ within organs, on part of the lines; also absent: BST2, DEPP1, TRIM22 |

### Downstream of this gene

*26 arrows, 26 of them with an alert ⚠; grade A 0, B 0, C 26. Shown: the 12 strongest; 14 more arrows (14 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAR]] | C | IRF9's natural level strengthens ADAR's drug response | IRF9's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.79, reverse +0.83; direction not clear | 2e-04 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[HELZ2]] | C | IRF9's natural level strengthens HELZ2's drug response | IRF9's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.83; direction not clear | 0.002 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT5]] | C | IRF9's natural level strengthens IFIT5's drug response | IRF9's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.78; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[TRIM25]] | C | IRF9's natural level strengthens TRIM25's drug response | IRF9's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.71; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SAMHD1]] | C | IRF9's natural level strengthens SAMHD1's drug response | IRF9's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.77, reverse +0.69; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP14]] | C | IRF9's natural level strengthens PARP14's drug response | IRF9's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.74; direction not clear | 0.003 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP12]] | C | IRF9's natural level strengthens PARP12's drug response | IRF9's natural level across 47 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.77; direction not clear | 0.004 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[SHISA5]] | C | IRF9's natural level strengthens SHISA5's drug response | IRF9's natural level across 49 lines (lineage-adjusted; a glimpse) | r +0.72, reverse +0.44; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[IFIT1]] | C | IRF9's natural level strengthens IFIT1's drug response | IRF9's natural level across 45 lines (lineage-adjusted; a glimpse) | r +0.74, reverse +0.32; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[USP18]] | C | IRF9's natural level strengthens USP18's drug response | IRF9's natural level across 44 lines (lineage-adjusted; a glimpse) | r +0.75, reverse +0.73; direction not clear | 0.006 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[PARP10]] | C | IRF9's natural level strengthens PARP10's drug response | IRF9's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.73; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |
| [[REC8]] | C | IRF9's natural level strengthens REC8's drug response | IRF9's natural level across 46 lines (lineage-adjusted; a glimpse) | r +0.73, reverse +0.85; direction not clear | 0.007 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 032]] — interferon alpha response; 139 genes; every member is in the + arm (projection on the module's main direction 0.860). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (49.3, 53.1); signed map (65.5, 30.7). **Vector** length 113, 33.1% of its response variance represented; |z| ≥ 3 in 1,452 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Antimicrobial mechanism of IFN-stimulated genes* (reactome, mean cos +0.77 to 21); *Modulation of host responses by IFN-stimulated genes* (reactome, mean cos +0.76 to 10); *ISG15 antiviral mechanism* (reactome, mean cos +0.78 to 11).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +6.3 | +1.0 |
|  | [[Harringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.6 | +1.4 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, would explain all of this change | +5.2 | -0.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~23% of this change | +5.0 | -3.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.6 | +2.3 |
|  | [[Docetaxel (drug)]] 5 µM |  | +3.0 | +1.8 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +2.7 | +3.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.5 | -0.3 |
|  | [[venetoclax (drug)]] 0.05 µM |  | +2.4 | +2.0 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +2.3 | +2.5 |
| fall | [[Tofacitinib (drug)]] 5 µM |  | -7.5 | -19.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -6.9 | -11.1 |
|  | [[Tofacitinib (citrate) (drug)]] 5 µM |  | -6.3 | -15.4 |
|  | [[Selinexor (drug)]] 5 µM |  | -6.2 | -9.3 |
|  | [[Tofacitinib (citrate) (drug)]] 0.5 µM |  | -6.2 | -10.6 |
|  | [[Tofacitinib (drug)]] 0.5 µM |  | -5.3 | -7.9 |

## What is on record

|  |  |
|---|---|
| Name | interferon regulatory factor 9 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q12 — chr14:24,161,234-24,168,043 (+) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously ISGF3G |
| Gene groups (HGNC) | Interferon regulatory factors |
| Hallmark sets | IL6_JAK_STAT3_SIGNALING, INTERFERON_ALPHA_RESPONSE, INTERFERON_GAMMA_RESPONSE |
| Reactome | 4 pathways, smallest: Interferon alpha/beta signaling; Interferon gamma signaling; Interferon Signaling |
| Matched by | ensembl_id |

**Function**, from UniProt [Q00978](https://www.uniprot.org/uniprotkb/Q00978) (Interferon regulatory factor 9):

> Transcription factor that plays an essential role in anti-viral immunity. It mediates signaling by type I IFNs (IFN-alpha and IFN-beta). Following type I IFN binding to cell surface receptors, Jak kinases (TYK2 and JAK1) are activated, leading to tyrosine phosphorylation of STAT1 and STAT2. IRF9/ISGF3G associates with the phosphorylated STAT1:STAT2 dimer to form a complex termed ISGF3 transcription factor, that enters the nucleus. ISGF3 binds to the IFN stimulated response element (ISRE) to …

**Summary**, from NCBI Gene [10379](https://www.ncbi.nlm.nih.gov/gene/10379):

> This gene encodes a member of the interferon regulatory factor (IRF) family, a group of transcription factors with diverse roles, including virus-mediated activation of interferon, and modulation of cell growth, differentiation, apoptosis, and immune system activity. Members of the IRF family are characterized by a conserved N-terminal DNA-binding domain containing tryptophan (W) repeats. Mutations in this gene result in Immunodeficiency 65. [provided by RefSeq, Jul 2020]

**Accessions** — [HGNC:6131](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6131) · Entrez [10379](https://www.ncbi.nlm.nih.gov/gene/10379) · UniProt [Q00978](https://www.uniprot.org/uniprotkb/Q00978) · Ensembl [ENSG00000213928](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213928)

## Data

Gene col 13150: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13150); `tables/drug_effects.parquet` (48 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13150, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13150]; `tensor/DDL_lfc|DDL_z.npy` [13150]; `embed/gene_vectors.npy` [13150]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13150 or target_col == 13150). Every well: [[IRF9 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/IRF9.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
