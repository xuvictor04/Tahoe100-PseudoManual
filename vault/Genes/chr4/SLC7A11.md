---
symbol: "SLC7A11"
type: "gene"
col: 7476
ensembl_id: "ENSG00000151012"
name: "solute carrier family 7 member 11"
location: "4q28.3"
module: 117
arm: "+"
pooled_cpm: 216.29
n_lines_expressing: 44
n_dd_up: 38
n_dd_down: 13
n_dd_up_clean: 31
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 5
direction_downstream: 2
tags: ["gene", "module/117"]
generated_by: "tahoemap"
---

# SLC7A11

*solute carrier family 7 member 11* — 4q28.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (7 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.95× (z +16.8, q 0e+00, up in 41 of 42 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.361× (z -17.7, q 0e+00, down in 32 of 42 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[HSPA9]] (+0.73, fdr 7e-06), [[IARS1]] (+0.72, fdr 7e-06), [[NMRAL2P]] (+0.70, fdr 7e-06); moves opposite to [[NBPF14]] (-0.48, fdr 3e-05).
> It is in [[Module 117]], a single-armed module (NRF2).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[AKR1B10]] → it (grade B ⚠); 2 go from it, the strongest it → [[TXNRD1]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 7 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 7476.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.95×** | +16.8 | 0e+00 | 41/42 (NCI-H2347, SW1417, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.96×** | +12.7 | 9e-35 | 39/41 (HOP62, Hs 766T, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.49×** | +10.5 | 1e-23 | 33/42 (COLO 205, LoVo, …) | all doses, flat | cell-cycle shift (explains ~13% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.06×** | +8.8 | 2e-16 | 29/42 (HOP62, COLO 205, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.93×** | +8.0 | 1e-13 | 33/42 (LOX-IMVI, NCI-H2347, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.89×** | +7.8 | 6e-13 | 29/42 (HOP62, COLO 205, …) | rises with dose |  |
| [[Artesunate (drug)]] 5 µM |  | **1.55×** | +7.6 | 2e-12 | 30/42 (SNU-1, HCT15, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.53×** | +7.3 | 2e-11 | 34/42 (LOX-IMVI, HEC-1-A, …) | rises with dose |  |
| [[Auranofin (drug)]] 0.5 µM |  | **1.79×** | +7.1 | 9e-11 | 34/42 (BT-474, LoVo, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.75×** | +6.8 | 5e-10 | 32/42 (LOX-IMVI, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.75×** | +6.6 | 2e-09 | 22/38 (NCI-H1792, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Artesunate (drug)]] 0.5 µM |  | **1.69×** | +6.4 | 7e-09 | 32/42 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.72×** | +6.1 | 3e-08 | 24/39 (NCI-H1792, HS-578T, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.65×** | +6.1 | 3e-08 | 36/42 (LOX-IMVI, Hs 766T, …) | top dose only |  |
| [[Neratinib (drug)]] 5 µM |  | **1.65×** | +6.1 | 4e-08 | 25/42 (LOX-IMVI, RKO, …) | rises with dose |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.61×** | +5.8 | 2e-07 | 28/42 (SHP-77, RKO, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.54×** | +5.2 | 5e-06 | 26/41 (HEC-1-A, HepG2/C3A, …) | rises with dose |  |
| [[Infigratinib (drug)]] 5 µM |  | **2.10×** | +4.7 | 6e-05 | 26/42 (NCI-H2347, HT-29, …) | top dose only | noisy plate (z scaled) |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.30×** | +4.6 | 1e-04 | 25/43 (SNU-1, MIA PaCa-2, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 7476.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.361×** | -17.7 | 0e+00 | 32/42 (PANC-1, LoVo, …) | top dose only | cell-cycle shift (explains ~17% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.403×** | -11.1 | 3e-26 | 41/42 (LS 180, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.545×** | -10.5 | 1e-23 | 33/43 (LoVo, LS 180, …) | top dose only | cell-cycle shift (explains ~9% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.426×** | -10.4 | 3e-23 | 39/42 (LS 180, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~22% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.430×** | -10.3 | 6e-23 | 38/42 (LS 180, LoVo, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.428×** | -10.0 | 1e-21 | 29/42 (PANC-1, LoVo, …) | inconsistent across doses | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.618×** | -5.7 | 1e-06 | 28/41 (KATO III, LoVo, …) | rises with dose | cell-cycle shift (explains ~10% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.663×** | -4.7 | 2e-04 | 25/41 (LoVo, RKO, …) | inconsistent across doses | low cells (technical?); position effect removed |
| [[Belinostat (drug)]] 0.5 µM |  | **0.685×** | -4.6 | 2e-04 | 24/42 (SW1417, PANC-1, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.734×** | -3.8 | 0.008 | 20/42 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Selinexor (drug)]] 0.5 µM |  | **0.737×** | -3.7 | 0.009 | 19/42 (LoVo, PANC-1, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.748×** | -3.4 | 0.028 | 21/42 (LS 180, SW480, …) | top dose only |  |
| [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.770×** | -3.2 | 0.057 | 20/42 (LS 180, COLO 205, …) | all doses, stronger at high dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.27 per unit of S-phase module lfc, -0.20 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 7476. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[LS 180 (line)]] | wt | 806 | 1 | 18 (11 ⚠) | [[Auranofin (drug)]] 5 µM 2.93× (z +10.0) | [[Homoharringtonine (drug)]] 5 µM 0.0880× (z -32.0) |
| [[LoVo (line)]] | wt | 619 | 3 (1 ⚠) | 14 (6 ⚠) | [[Auranofin (drug)]] 5 µM 3.95× (z +14.4) | [[Homoharringtonine (drug)]] 5 µM 0.0900× (z -35.6) |
| [[SW480 (line)]] | alt | 150 | 2 | 12 (6 ⚠) | [[Auranofin (drug)]] 5 µM 2.57× (z +10.3) | [[Homoharringtonine (drug)]] 5 µM 0.247× (z -21.7) |
| [[KATO III (line)]] | alt | 574 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0990× (z -28.4) |
| [[PANC-1 (line)]] | alt | 239 | 0 | 12 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0547× (z -36.4) |
| [[HT-29 (line)]] | alt | 572 | 1 | 10 (3 ⚠) | [[Auranofin (drug)]] 5 µM 3.70× (z +12.2) | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -27.5) |
| [[SW1417 (line)]] | alt | 134 | 2 | 9 (3 ⚠) | [[Auranofin (drug)]] 5 µM 5.84× (z +16.1) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.299× (z -15.6) |
| [[COLO 205 (line)]] | alt | 169 | 4 | 5 | [[Auranofin (drug)]] 5 µM 5.70× (z +10.2) | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -15.0) |
| [[HOP62 (line)]] | alt | 82.8 | 8 (5 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 12.6× (z +13.4) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 6.73× (z +10.5) | — |
| [[AsPC-1 (line)]] | alt | 111 | 2 | 4 | [[Auranofin (drug)]] 5 µM 5.48× (z +12.0) | [[Homoharringtonine (drug)]] 5 µM 0.178× (z -17.2) |
| [[LOX-IMVI (line)]] | wt | 77.6 | 6 (3 ⚠) | 0 | [[Auranofin (drug)]] 5 µM 5.32× (z +12.4) | — |
| [[SW48 (line)]] | wt | 238 | 0 | 6 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -17.1) |
| [[HS-578T (line)]] | alt | 128 | 4 (3 ⚠) | 1 | [[Dinaciclib (drug)]] 0.5 µM 4.72× (z +12.0) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 3.11× (z +8.8) | [[Homoharringtonine (drug)]] 5 µM 0.458× (z -8.5) |
| [[RKO (line)]] | wt | 122 | 3 (1 ⚠) | 2 (1 ⚠) | [[Niclosamide (olamine) (drug)]] 5 µM 4.83× (z +9.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 4.26× (z +8.7) | [[Homoharringtonine (drug)]] 5 µM 0.111× (z -18.7) |
| [[HEC-1-A (line)]] | alt | 87.2 | 3 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 5.38× (z +10.5) | [[Homoharringtonine (drug)]] 5 µM 0.325× (z -10.0) |
| [[NCI-H1792 (line)]] | alt | 130 | 4 (4 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 11.5× (z +13.5) ⚠ toxic; transcription drop | — |
| [[NCI-H2030 (line)]] | alt | 254 | 0 | 4 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.435× (z -10.5) |
| [[NCI-H2347 (line)]] | alt | 85.3 | 3 (2 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 8.39× (z +16.8) | [[Homoharringtonine (drug)]] 5 µM 0.436× (z -9.4) |
| [[HCT15 (line)]] | alt | 296 | 3 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 3.51× (z +10.1) | — |
| [[HepG2_C3A (line)]] | wt | 146 | 2 (1 ⚠) | 1 | [[Auranofin (drug)]] 5 µM 7.25× (z +13.6) | [[Homoharringtonine (drug)]] 5 µM 0.280× (z -12.3) |
| [[RPMI-7951 (line)]] | alt | 68.7 | 2 (1 ⚠) | 1 | [[Niclosamide (olamine) (drug)]] 5 µM 5.70× (z +9.1) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 5.29× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -10.2) |
| [[SNU-1 (line)]] | wt | 154 | 3 (1 ⚠) | 0 | [[Artesunate (drug)]] 5 µM 3.69× (z +10.6) | — |
| [[A-172 (line)]] | wt | 117 | 1 | 1 | [[Auranofin (drug)]] 5 µM 7.36× (z +13.2) | [[Homoharringtonine (drug)]] 5 µM 0.270× (z -12.2) |
| [[A498 (line)]] | wt | 320 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -10.1) |
| [[A549 (line)]] | wt | 127 | 2 (2 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 6.43× (z +9.3) ⚠ toxic; transcription drop | — |
| [[CFPAC-1 (line)]] | alt | 185 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.75× (z +12.5) | [[Panobinostat (drug)]] 0.5 µM 0.268× (z -10.6) |
| [[CHP-212 (line)]] | wt | 133 | 1 | 1 | [[Auranofin (drug)]] 5 µM 9.66× (z +10.6) | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -10.1) |
| [[H4 (line)]] | wt | 593 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.222× (z -11.3) |
| [[Hs 766T (line)]] | wt | 95.8 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 5.68× (z +10.7) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 3.81× (z +8.6) | — |
| [[hTERT-HPNE (line)]] | wt | 80.0 | 2 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 7.03× (z +10.0) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 5.80× (z +9.4) | — |
| [[NCI-H460 (line)]] | wt | 451 | 0 | 2 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.163× (z -15.0) |
| [[SHP-77 (line)]] | alt | 87.0 | 1 (1 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 4.96× (z +9.7) ⚠ toxic; transcription drop | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -16.1) |
| [[SW 900 (line)]] | alt | 139 | 1 | 1 | [[Auranofin (drug)]] 5 µM 4.30× (z +8.9) | [[Homoharringtonine (drug)]] 5 µM 0.277× (z -11.1) |
| [[BT-474 (line)]] | alt | 55.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -16.6) |
| [[MIA PaCa-2 (line)]] | alt | 75.4 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.28× (z +8.5) | — |
| [[NCI-H1573 (line)]] | alt | 416 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.142× (z -17.5) |
| [[NCI-H23 (line)]] | alt | 80.3 | 1 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 3.62× (z +8.7) ⚠ toxic | — |
| [[SK-MEL-2 (line)]] | alt | 87.3 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.315× (z -9.7) |
| [[A-427 (line)]] | wt | 287 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 46.1 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 32.2 n.m. | — | — | — | — |
| [[C32 (line)]] | wt | 36.3 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 129 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 213 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 212 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 52.1 n.m. | — | — | — | — |
| [[Panc 03.27 (line)]] | alt | 44.1 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 34.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 161 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 98.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 7476), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[HSPA9]] | +0.73 | +0.67 / +0.76 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[IARS1]] | +0.72 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[NMRAL2P]] | +0.70 | +0.64 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[ME1]] | +0.69 | +0.59 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 455 |
| [[YARS1]] | +0.69 | +0.64 / +0.70 | both halves | 7e-06 |  |
| [[TARS1]] | +0.69 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[TXNRD1]] | +0.69 | +0.71 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 664 |
| [[PSAT1]] | +0.68 | +0.70 / +0.68 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 449 |
| [[SLC6A9]] | +0.68 | +0.69 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM |
| [[GCLM]] | +0.68 | +0.66 / +0.66 | both halves | 7e-06 | pathway: HALLMARK_HEME_METABOLISM; STRING 689 |
| [[AARS1]] | +0.68 | +0.64 / +0.71 | both halves | 7e-06 |  |
| [[PIR]] | +0.67 | +0.67 / +0.65 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NBPF14]] | -0.48 | -0.44 / -0.51 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AKR1B10]] | B | AKR1B10 activity raises SLC7A11's level | lines that do not express AKR1B10 (41) vs lines expressing it (9) | 2.79× lower at baseline in the lines without AKR1B10 | 0.014 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: FGFR2, GABRP, MUC17 |
| [[CYP4F11]] | B | CYP4F11 activity raises SLC7A11's level | lines that do not express CYP4F11 (29) vs lines expressing it (21) | 2.17× lower at baseline in the lines without CYP4F11 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC01564, ENSG00000279806, TNS4 |
| [[NMRAL2P]] | B | NMRAL2P activity raises SLC7A11's level | lines that do not express NMRAL2P (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without NMRAL2P | 0.057 | ⚠ within organs, on part of the lines; also absent: NMRAL2P-1, SERPINE2, APOL1 |
| [[NMRAL2P-1]] | B | NMRAL2P-1 activity raises SLC7A11's level | lines that do not express NMRAL2P-1 (18) vs lines expressing it (32) | 1.76× lower at baseline in the lines without NMRAL2P-1 | 0.087 | ⚠ within organs, on part of the lines; also absent: NMRAL2P, SERPINE2, APOL1 |
| [[JDP2]] | B | JDP2 activity raises SLC7A11's level | lines that do not express JDP2 (12) vs lines expressing it (38) | 2.13× lower at baseline in the lines without JDP2 | 0.097 | ⚠ within organs, on part of the lines; also absent: JUP, LINC01836, SEL1L3; maybe low, not absent |

### Downstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TXNRD1]] | B | SLC7A11 activity raises TXNRD1's level | lines that do not express SLC7A11 (6) vs lines expressing it (44) | 1.93× lower at baseline in the lines without SLC7A11 | 0.064 | ⚠ within organs, on part of the lines; also absent: CD68; maybe low, not absent |
| [[NECAB2]] | B | SLC7A11 activity raises NECAB2's level | lines that do not express SLC7A11 (6) vs lines expressing it (44) | 1.46× lower at baseline in the lines without SLC7A11 | 0.094 | ⚠ within organs, on part of the lines; also absent: CD68; maybe low, not absent |

## Where it sits

- **Module**: [[Module 117]] — NRF2; 41 genes; every member is in the + arm (projection on the module's main direction 0.736). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-9.2, 48.2); signed map (51.4, -10.6). **Vector** length 158, 56.7% of its response variance represented; |z| ≥ 3 in 1,642 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *NRF2* (control, mean cos +0.55 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +13.1 | +16.8 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | +9.3 | +12.7 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +9.0 | +10.5 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +8.3 | +7.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +5.8 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +7.7 | +6.1 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.5 | +7.3 |
|  | [[Ponatinib (drug)]] 5 µM |  | +6.5 | +5.8 |
| fall | [[Harringtonine (drug)]] 5 µM |  | -5.6 | -10.0 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -4.4 | -4.7 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | -4.0 | -17.7 |
|  | [[Belinostat (drug)]] 5 µM |  | -3.4 | -10.3 |
|  | [[Selinexor (drug)]] 0.5 µM |  | -3.1 | -3.7 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | -2.8 | -2.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.8 | -0.7 |
|  | [[Dexamethasone (drug)]] 0.5 µM |  | -2.7 | -1.9 |
|  | [[Daidzin (drug)]] 5 µM |  | -2.5 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | solute carrier family 7 member 11 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 4q28.3 — chr4:138,164,097-138,242,349 (-) |
| Ensembl biotype | protein_coding |
| Also known as | xCT |
| Gene groups (HGNC) | Solute carrier family 7 |
| Hallmark sets | HEME_METABOLISM, P53_PATHWAY, MTORC1_SIGNALING |
| Reactome | 13 pathways, smallest: NFE2L2 regulating anti-oxidant/detoxification enzymes; Basigin interactions; Amino acid transport across the plasma membrane |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9UPY5](https://www.uniprot.org/uniprotkb/Q9UPY5) (Cystine/glutamate transporter):

> Heterodimer with SLC3A2, that functions as an antiporter by mediating the exchange of extracellular anionic L-cystine and intracellular L-glutamate across the cellular plasma membrane. Provides L-cystine for the maintenance of the redox balance between extracellular L-cystine and L-cysteine and for the maintenance of the intracellular levels of glutathione that is essential for cells protection from oxidative stress (By similarity). The transport is sodium-independent, electroneutral with a …

**Summary**, from NCBI Gene [23657](https://www.ncbi.nlm.nih.gov/gene/23657):

> This gene encodes a member of a heteromeric, sodium-independent, anionic amino acid transport system that is highly specific for cysteine and glutamate. In this system, designated Xc(-), the anionic form of cysteine is transported in exchange for glutamate. This protein has been identified as the predominant mediator of Kaposi sarcoma-associated herpesvirus fusion and entry permissiveness into cells. Also, increased expression of this gene in primary gliomas (compared to normal brain tissue) …

**Accessions** — [HGNC:11059](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:11059) · Entrez [23657](https://www.ncbi.nlm.nih.gov/gene/23657) · UniProt [Q9UPY5](https://www.uniprot.org/uniprotkb/Q9UPY5) · Ensembl [ENSG00000151012](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000151012)

## Data

Gene col 7476: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 7476); `tables/drug_effects.parquet` (53 rows, flagged included); `relations/gene_relations.parquet` (col_a == 7476, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 7476]; `tensor/DDL_lfc|DDL_z.npy` [7476]; `embed/gene_vectors.npy` [7476]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 7476 or target_col == 7476). Every well: [[SLC7A11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC7A11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
