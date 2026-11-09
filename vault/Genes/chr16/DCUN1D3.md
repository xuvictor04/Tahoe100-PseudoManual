---
symbol: "DCUN1D3"
type: "gene"
col: 11988
ensembl_id: "ENSG00000188215"
name: "defective in cullin neddylation 1 domain containing 3"
location: "16p12.3"
module: 109
arm: "+"
pooled_cpm: 72.7
n_lines_expressing: 50
n_dd_up: 2
n_dd_down: 37
n_dd_up_clean: 2
n_dd_down_clean: 26
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/109"]
generated_by: "tahoemap"
---

# DCUN1D3

*defective in cullin neddylation 1 domain containing 3* — 16p12.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 2 drug-doses (none with an alert); the strongest is [[TAK-901 (drug)]] 5 µM: 6.24× (z +11.0, q 3e-25, up in 48 of 49 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 15 lines (MIA PaCa-2 41.6×, NCI-H460 12.1×, SNU-1 36.5×, LOX-IMVI 12.8×, …).
> Pooled over the cell lines (median), lowered significantly by 37 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.295× (z -13.4, q 3e-38, down in 40 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.530× (z -10.3, q 2e-22, down in 39 of 49 measured lines).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GP6-AS1]] (+0.65, fdr 1e-05), [[TXN2]] (+0.61, fdr 1e-05), [[RGL1]] (+0.59, fdr 3e-05); moves opposite to [[FBXW4]] (-0.62, fdr 7e-05), [[DNAI4]] (-0.61, fdr 1e-05), [[DPH6-DT]] (-0.59, fdr 3e-05).
> It is in [[Module 109]], a single-armed module (immediate early).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 2 in all, none with an alert. 2 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 11988.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, none with an alert; `tables/drug_line_top.parquet`), these raise it: [[TAK-901 (drug)]] 5 µM in 15 lines (MIA PaCa-2 41.6×, NCI-H460 12.1×, SNU-1 36.5×, LOX-IMVI 12.8×, …).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **6.24×** | +11.0 | 3e-25 | 48/49 (MIA PaCa-2, NCI-H460, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **2.24×** | +4.8 | 4e-04 | 30/48 (LOX-IMVI, SNU-1, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 39 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 37 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 11988.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.295×** | -13.4 | 3e-38 | 40/42 (hTERT-HPNE, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.325×** | -12.9 | 2e-35 | 46/49 (A498, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.530×** | -10.3 | 2e-22 | 39/49 (A498, SW1417, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.522×** | -7.4 | 2e-11 | 34/48 (Panc 03.27, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.505×** | -7.2 | 5e-11 | 35/45 (KATO III, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.535×** | -6.9 | 6e-10 | 37/48 (SW48, hTERT-HPNE, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.538×** | -6.8 | 7e-10 | 38/50 (SNU-423, A-172, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.547×** | -6.6 | 2e-09 | 36/47 (RPMI-7951, H4, …) | top dose only | cell-cycle shift (explains ~11% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.626×** | -5.4 | 5e-06 | 32/48 (SW1417, SW48, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.639×** | -5.1 | 2e-05 | 33/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Belumosudil (drug)]] 5 µM |  | **0.630×** | -5.1 | 2e-05 | 30/48 (NCI-H1792, J82, …) | top dose only |  |
| [[Auranofin (drug)]] 5 µM |  | **0.659×** | -4.8 | 8e-05 | 33/48 (SW480, SW48, …) | top dose only |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~62% of this change | **0.748×** | -4.7 | 1e-04 | 23/48 (SW1417, COLO 205, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.748×** | -4.7 | 1e-04 | 28/48 (A549, NCI-H2030, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~34% of this change | **0.657×** | -4.6 | 1e-04 | 30/48 (COLO 205, SW1417, …) | rises with dose | composition shift |
| [[XRK3F2 (drug)]] 0.5 µM |  | **0.581×** | -4.4 | 3e-04 | 35/47 (H4, RKO, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **0.679×** | -4.4 | 3e-04 | 34/48 (SNU-423, KATO III, …) | rises with dose |  |
| [[Radotinib (drug)]] 5 µM |  | **0.762×** | -4.4 | 3e-04 | 27/48 (RKO, RPMI-7951, …) | top dose only |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.777×** | -4.1 | 0.001 | 30/48 (A-172, NCI-H2030, …) | top dose only |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | **0.702×** | -4.0 | 0.001 | 36/49 (SW480, Hs 766T, …) | all doses, flat |  |
| [[Trametinib (drug)]] 0.5 µM |  | **0.763×** | -3.7 | 0.006 | 24/48 (RKO, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[vincristine (drug)]] 0.5 µM |  | **0.640×** | -3.6 | 0.006 | 26/48 (SW 1088, SW48, …) | inconsistent across doses | low cells (technical?); noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.04 per unit of S-phase module lfc, -0.27 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 11988. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW1417 (line)]] | alt | 145 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -13.2) ⚠ cell-cycle shift, explains ~62% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.308× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 75.8 | 1 | 5 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 11.6× (z +9.3) | [[Dinaciclib (drug)]] 5 µM 0.0295× (z -24.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.388× (z -9.7) |
| [[A-172 (line)]] | wt | 66.4 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.174× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.344× (z -8.6) |
| [[A-427 (line)]] | wt | 44.0 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +10.0) | [[Dinaciclib (drug)]] 5 µM 0.231× (z -11.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.280× (z -10.5) |
| [[A498 (line)]] | wt | 156 | 1 | 4 (3 ⚠) | [[TAK-901 (drug)]] 5 µM 6.08× (z +9.5) | [[Dinaciclib (drug)]] 5 µM 0.121× (z -20.3) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.339× (z -15.3) |
| [[A549 (line)]] | wt | 93.7 | 1 | 4 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.07× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.166× (z -13.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.446× (z -9.2) |
| [[SW480 (line)]] | alt | 114 | 0 | 5 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.249× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.412× (z -10.8) |
| [[CFPAC-1 (line)]] | alt | 85.9 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.170× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.365× (z -9.0) |
| [[Hs 766T (line)]] | wt | 130 | 1 | 3 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 9.44× (z +8.8) | [[Dinaciclib (drug)]] 0.5 µM 0.121× (z -15.7) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.389× (z -9.9) |
| [[RPMI-7951 (line)]] | alt | 68.4 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.189× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.391× (z -9.8) |
| [[SW48 (line)]] | wt | 125 | 0 | 4 (1 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.136× (z -13.2) |
| [[COLO 205 (line)]] | alt | 61.5 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.117× (z -13.9) ⚠ toxic; transcription drop |
| [[KATO III (line)]] | alt | 53.7 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0583× (z -19.4) ⚠ toxic; transcription drop |
| [[NCI-H2347 (line)]] | alt | 47.4 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.147× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -12.9) |
| [[Panc 03.27 (line)]] | alt | 57.4 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.187× (z -11.5) |
| [[PANC-1 (line)]] | alt | 72.3 | 1 | 2 (2 ⚠) | [[TAK-901 (drug)]] 5 µM 11.1× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.6) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 152 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.423× (z -10.8) |
| [[H4 (line)]] | wt | 68.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0547× (z -16.9) ⚠ toxic; transcription drop |
| [[HepG2_C3A (line)]] | wt | 78.3 | 0 | 2 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.389× (z -9.0) ⚠ cell-cycle shift, explains ~62% of this change |
| [[HS-578T (line)]] | alt | 59.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.250× (z -10.8) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.431× (z -9.2) |
| [[HT-29 (line)]] | alt | 64.6 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.169× (z -12.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 51.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 13.4× (z +9.8) | [[Dinaciclib (drug)]] 5 µM 0.274× (z -9.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 47.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.8× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.308× (z -9.1) ⚠ toxic; transcription drop |
| [[LS 180 (line)]] | wt | 40.8 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.4× (z +8.7) | [[Dinaciclib (drug)]] 5 µM 0.241× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 140 | 0 | 2 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.328× (z -10.9) |
| [[NCI-H1792 (line)]] | alt | 77.4 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.163× (z -10.4) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 77.7 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 8.57× (z +8.9) | [[Dinaciclib (drug)]] 5 µM 0.214× (z -11.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 70.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 12.4× (z +10.0) | [[Dinaciclib (drug)]] 0.5 µM 0.132× (z -15.4) ⚠ toxic; transcription drop |
| [[SNU-423 (line)]] | alt | 59.4 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0936× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.225× (z -8.5) |
| [[SW 1088 (line)]] | alt | 87.8 | 0 | 2 (1 ⚠) | — | [[Estrone sulfate (potassium) (drug)]] 0.05 µM 0.0793× (z -9.5) |
| [[AN3 CA (line)]] | alt | 63.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.138× (z -9.7) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 73.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.117× (z -13.8) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 47.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0932× (z -13.5) ⚠ toxic; transcription drop |
| [[HEC-1-A (line)]] | alt | 36.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.345× (z -8.7) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 41.6× (z +13.5) | — |
| [[NCI-H460 (line)]] | wt | 38.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.1× (z +11.4) | — |
| [[SK-MEL-2 (line)]] | alt | 34.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.5× (z +9.1) | — |
| [[SNU-1 (line)]] | wt | 56.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 36.5× (z +10.9) | — |
| [[SW 900 (line)]] | alt | 84.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.217× (z -11.7) ⚠ toxic; transcription drop |
| [[BT-474 (line)]] | alt | 33.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 54.6 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 61.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 43.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 78.3 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 60.9 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 40.0 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 56.1 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 55.1 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 11988), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*72 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GP6-AS1]] | +0.65 | +0.64 / +0.54 | both halves | 1e-05 |  |
| [[TXN2]] | +0.61 | +0.59 / +0.56 | both halves | 1e-05 |  |
| [[RGL1]] | +0.59 | +0.46 / +0.48 | both halves | 3e-05 |  |
| [[NECTIN2]] | +0.58 | +0.61 / +0.50 | both halves | 1e-05 |  |
| [[SYS1-DBNDD2]] | +0.58 | +0.55 / +0.57 | both halves | 1e-05 |  |
| [[EGR2]] | +0.58 | +0.40 / +0.63 | both halves | 5e-05 |  |
| [[ATG101]] | +0.57 | +0.61 / +0.39 | both halves | 6e-05 |  |
| [[NCKAP5L]] | +0.56 | +0.43 / +0.52 | both halves | 3e-05 |  |
| [[EGR3]] | +0.56 | +0.42 / +0.63 | both halves | 4e-05 |  |
| [[DIABLO]] | +0.56 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[MAPKAPK2]] | +0.56 | +0.58 / +0.48 | both halves | 2e-05 |  |
| [[ABCA7]] | +0.55 | +0.48 / +0.41 | both halves | 4e-05 |  |

## Genes that move opposite

*28 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXW4]] | -0.62 | -0.62 / -0.38 | both halves | 7e-05 | pathway: Neddylation; STRING 499 |
| [[DNAI4]] | -0.61 | -0.57 / -0.50 | both halves | 1e-05 |  |
| [[DPH6-DT]] | -0.59 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[UBXN2A]] | -0.57 | -0.59 / -0.37 | both halves | 8e-05 |  |
| [[STAT5B]] | -0.56 | -0.53 / -0.43 | both halves | 3e-05 |  |
| [[RNF146]] | -0.55 | -0.59 / -0.34 | both halves | 1e-04 |  |
| [[ENTPD3-AS1]] | -0.54 | -0.50 / -0.37 | both halves | 8e-05 |  |
| [[CASS4]] | -0.52 | -0.48 / -0.37 | both halves | 9e-05 |  |
| [[SLC26A7]] | -0.52 | -0.51 / -0.27 | both halves | 3e-04 |  |
| [[ZFR]] | -0.51 | -0.42 / -0.45 | both halves | 4e-05 |  |
| [[CLCN7]] | -0.51 | -0.56 / -0.37 | both halves | 8e-05 |  |
| [[HEXIM2-AS1]] | -0.50 | -0.49 / -0.27 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity raises DCUN1D3's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.6% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 109]] — immediate early; 43 genes; every member is in the + arm (projection on the module's main direction 0.573). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.5, -26.4); signed map (3.5, 27.3). **Vector** length 114, 37.0% of its response variance represented; |z| ≥ 3 in 1,280 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +8.2 | +11.0 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.3 | +0.3 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.8 | +1.0 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +4.5 | +0.9 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | +4.3 | +0.9 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.8 | +4.8 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.4 | +1.2 |
|  | [[Brivudine (drug)]] 5 µM |  | +1.9 | +0.1 |
|  | [[Cytarabine (drug)]] 0.05 µM |  | +1.9 | +1.7 |
|  | [[TAK-733 (drug)]] 0.05 µM |  | +1.7 | +2.2 |
| fall | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -7.1 | -6.9 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -7.4 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.8 | -6.8 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -5.7 | -3.4 |
|  | [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | -5.3 | -5.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | -5.2 | -4.4 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -4.2 | -3.0 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.5 µM |  | -4.0 | -4.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.8 | -5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.5 | -2.9 |

## What is on record

|  |  |
|---|---|
| Name | defective in cullin neddylation 1 domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 16p12.3 — chr16:20,854,925-20,900,358 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MGC48972, FLJ41725, DKFZp686O0290, SCCRO3 |
| Reactome | 1 pathways, smallest: Neddylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q8IWE4](https://www.uniprot.org/uniprotkb/Q8IWE4) (DCN1-like protein 3):

> Contributes to the neddylation of all cullins by transferring NEDD8 from N-terminally acetylated NEDD8-conjugating E2s enzyme to different cullin C-terminal domain-RBX complexes and may play a role in the cell cycle progression by regulating the SCF ubiquitin E3 ligase complex, after UV damage. At the cell membrane, can promote and as well inhibit cullins neddylation.

**Summary**, from NCBI Gene [123879](https://www.ncbi.nlm.nih.gov/gene/123879):

> Enables cullin family protein binding activity. Involved in several processes, including negative regulation of G1/S transition of mitotic cell cycle; regulation of protein neddylation; and response to UV-C. Located in several cellular components, including cytosol; nucleoplasm; and perinuclear region of cytoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:28734](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:28734) · Entrez [123879](https://www.ncbi.nlm.nih.gov/gene/123879) · UniProt [Q8IWE4](https://www.uniprot.org/uniprotkb/Q8IWE4) · Ensembl [ENSG00000188215](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188215)

## Data

Gene col 11988: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 11988); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 11988, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 11988]; `tensor/DDL_lfc|DDL_z.npy` [11988]; `embed/gene_vectors.npy` [11988]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 11988 or target_col == 11988). Every well: [[DCUN1D3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DCUN1D3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
