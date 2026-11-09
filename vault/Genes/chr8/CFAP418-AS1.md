---
symbol: "CFAP418-AS1"
type: "gene"
col: 14840
ensembl_id: "ENSG00000253773"
name: "CFAP418 antisense RNA 1"
location: "8q22.1"
module: 26
arm: "+"
pooled_cpm: 11.85
n_lines_expressing: 50
n_dd_up: 38
n_dd_down: 20
n_dd_up_clean: 34
n_dd_down_clean: 11
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/026"]
generated_by: "tahoemap"
---

# CFAP418-AS1

*CFAP418 antisense RNA 1* — 8q22.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 38 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 8.72× (z +30.4, q 0e+00, up in 44 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 20 drug-doses (9 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.478× (z -7.3, q 1e-10, down in 33 of 47 measured lines).
> Its strongest partners by |cos| (95 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 5 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PKN2-AS1]] (+0.86, fdr 7e-06), [[MAD2L1-DT]] (+0.83, fdr 1e-05), [[ZRANB2-DT]] (+0.83, fdr 7e-06).
> It sits in the **+** arm of [[Module 026]].
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[LINC02641]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 4 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 38 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 14840.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **8.72×** | +30.4 | 0e+00 | 44/45 (LoVo, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.31×** | +11.4 | 1e-27 | 35/44 (SW480, HOP62, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.19×** | +11.0 | 1e-25 | 39/48 (NCI-H2347, A-172, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.02×** | +9.8 | 1e-20 | 33/45 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.57×** | +9.0 | 3e-17 | 36/47 (LS 180, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **2.22×** | +7.9 | 3e-13 | 37/47 (NCI-H460, BT-474, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Cobimetinib (drug)]] 5 µM |  | **2.05×** | +6.8 | 7e-10 | 29/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **1.82×** | +6.0 | 2e-07 | 26/47 (RKO, HOP62, …) | top dose only |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | **1.77×** | +5.5 | 2e-06 | 23/46 (SW480, C32, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.4 | 4e-06 | 16/35 (HEC-1-A, AsPC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.5 µM |  | **1.49×** | +4.9 | 5e-05 | 20/47 (SW480, NCI-H23, …) | all doses, flat | noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +4.7 | 1e-04 | 19/44 (A-172, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Binimetinib (drug)]] 0.5 µM |  | **1.45×** | +4.6 | 2e-04 | 18/47 (SW480, SW48, …) | all doses, flat | noisy plate (z scaled) |
| [[Ponatinib (drug)]] 5 µM |  | **1.58×** | +4.5 | 2e-04 | 21/47 (RKO, LS 180, …) | rises with dose |  |
| [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | **1.61×** | +4.5 | 2e-04 | 18/46 (SW480, NCI-H1573, …) | all doses, stronger at high dose |  |
| [[Trametinib (drug)]] 5 µM |  | **1.55×** | +4.5 | 2e-04 | 19/48 (SW480, NCI-H23, …) | all doses, flat | cell-cycle shift (explains ~21% here); noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 20 in all, 9 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 20 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 9 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 14840.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.478×** | -7.3 | 1e-10 | 33/47 (SW48, C32, …) | two highest doses | cell-cycle shift (explains ~19% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.554×** | -5.9 | 1e-06 | 23/44 (AsPC-1, COLO 205, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.570×** | -5.6 | 4e-06 | 24/47 (NCI-H661, LOX-IMVI, …) | all doses, stronger at high dose | cell-cycle shift (explains ~24% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.679×** | -5.4 | 7e-06 | 23/48 (SW480, NCI-H1573, …) | rises with dose |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.597×** | -5.1 | 3e-05 | 22/46 (C32, HS-578T, …) | two highest doses |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.595×** | -5.0 | 4e-05 | 22/47 (KATO III, C32, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~39% of this change | **0.614×** | -4.8 | 9e-05 | 22/48 (A-427, C32, …) | all doses, stronger at high dose | composition shift |
| [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | **0.614×** | -4.8 | 9e-05 | 18/46 (SHP-77, A-172, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.609×** | -4.7 | 1e-04 | 17/39 (HS-578T, SW480, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.634×** | -4.5 | 3e-04 | 16/47 (RKO, J82, …) | inconsistent across doses |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.649×** | -4.3 | 9e-04 | 21/47 (SW48, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Peretinoin (drug)]] 5 µM |  | **0.665×** | -3.9 | 0.005 | 13/47 (SW1417, NCI-H23, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.691×** | -3.7 | 0.011 | 20/46 (HS-578T, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.696×** | -3.6 | 0.012 | 15/47 (C32, H4, …) | two highest doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.699×** | -3.6 | 0.014 | 15/47 (C32, A-427, …) | all doses, flat |  |
| [[S-Adenosyl-L-methionine (disulfate tosylate) (drug)]] 5 µM |  | **0.787×** | -3.4 | 0.024 | 10/48 (MIA PaCa-2, J82, …) | all doses, flat |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.712×** | -3.2 | 0.043 | 12/46 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.29 per unit of S-phase module lfc, -0.19 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 14840. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[C32 (line)]] | wt | 59.1 | 1 | 6 (4 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.91× (z +8.8) | [[Dinaciclib (drug)]] 5 µM 0.0578× (z -12.6) ⚠ toxic; transcription drop · without an alert: [[Ponatinib (drug)]] 5 µM 0.115× (z -9.9) |
| [[A-172 (line)]] | wt | 10.6 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.2× (z +18.5) | — |
| [[A-427 (line)]] | wt | 20.2 | 0 | 3 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.132× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HCT15 (line)]] | alt | 19.2 | 2 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.46× (z +10.5) | [[Niclosamide (olamine) (drug)]] 5 µM 0.0656× (z -9.6) ⚠ toxic; cell-cycle shift, explains ~41% of this change |
| [[HOP62 (line)]] | alt | 7.29 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +14.2) | — |
| [[LoVo (line)]] | wt | 7.25 | 3 (1 ⚠) | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +16.5) | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 2 (1 ⚠) | 1 (1 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.90× (z +10.6) ⚠ position not correctable · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.53× (z +8.5) | [[Digitoxin (drug)]] 5 µM 0.158× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 4.46 | 3 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 17.7× (z +14.7) ⚠ cell-cycle shift, explains ~81% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.2) | — |
| [[RKO (line)]] | wt | 11.5 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.5× (z +15.0) | — |
| [[BT-474 (line)]] | alt | 12.1 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.0× (z +12.0) | — |
| [[HS-578T (line)]] | alt | 46.5 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.45× (z +10.6) | [[Digitoxin (drug)]] 5 µM 0.114× (z -10.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HT-29 (line)]] | alt | 5.78 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.3× (z +12.5) | — |
| [[hTERT-HPNE (line)]] | wt | 6.04 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 32.9× (z +15.0) | — |
| [[J82 (line)]] | alt | 4.98 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +13.4) | — |
| [[LOX-IMVI (line)]] | wt | 10.8 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.98× (z +12.0) | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.114× (z -9.0) |
| [[NCI-H460 (line)]] | wt | 5.05 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.2× (z +15.5) | — |
| [[SW 900 (line)]] | alt | 10.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.9× (z +12.6) | — |
| [[SW480 (line)]] | alt | 14.5 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 5.04× (z +12.2) | — |
| [[A498 (line)]] | wt | 14.8 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.7× (z +14.1) | — |
| [[A549 (line)]] | wt | 6.78 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.74× (z +10.8) | — |
| [[AsPC-1 (line)]] | alt | 4.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.5× (z +13.5) | — |
| [[CFPAC-1 (line)]] | alt | 3.16 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 20.4× (z +12.9) | — |
| [[COLO 205 (line)]] | alt | 6.61 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +12.2) | — |
| [[HEC-1-A (line)]] | alt | 8.26 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 6.99× (z +12.2) | — |
| [[HepG2_C3A (line)]] | wt | 5.39 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 23.6× (z +11.9) | — |
| [[Hs 766T (line)]] | wt | 7.22 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.49× (z +10.6) | — |
| [[KATO III (line)]] | alt | 10.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.12× (z +11.9) | — |
| [[LS 180 (line)]] | wt | 9.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +13.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 4.27 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.52× (z +9.6) | — |
| [[NCI-H1792 (line)]] | alt | 4.11 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 16.7× (z +12.3) | — |
| [[NCI-H661 (line)]] | alt | 55.9 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 0.5 µM 0.0397× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 3.85 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 13.1× (z +10.8) | — |
| [[PANC-1 (line)]] | alt | 17.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +9.8) | — |
| [[RPMI-7951 (line)]] | alt | 6.84 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.2× (z +10.4) | — |
| [[SHP-77 (line)]] | alt | 5.86 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 15.9× (z +12.9) | — |
| [[SNU-423 (line)]] | alt | 5.48 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.48× (z +10.9) | — |
| [[SW1417 (line)]] | alt | 8.55 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 9.06× (z +12.5) | — |
| [[SW48 (line)]] | wt | 26.8 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.0472× (z -10.3) |
| [[AN3 CA (line)]] | alt | 8.93 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.29 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 20.0 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 13.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.2 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 29.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 14840), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 5 of them with an alert (⚠; 5 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PKN2-AS1]] | +0.86 | +0.83 / +0.71 | both halves | 7e-06 | same gene group |
| [[MAD2L1-DT]] | +0.83 | +0.83 / +0.55 | both halves | 1e-05 |  |
| [[ZRANB2-DT]] | +0.83 | +0.77 / +0.72 | both halves | 7e-06 |  |
| [[PCNX4-DT]] | +0.80 | +0.79 / +0.56 | both halves | 1e-05 |  |
| [[TMEM202-AS1]] | +0.78 | +0.76 / +0.48 | both halves | 2e-05 | same gene group |
| [[EIF1B-AS1]] | +0.78 | +0.76 / +0.55 | both halves | 1e-05 |  |
| [[AHI1-DT]] | +0.77 | +0.78 / +0.45 | both halves | 3e-05 |  |
| [[SOX2-OT]] | +0.77 | +0.77 / +0.62 | both halves | 7e-06 |  |
| [[TAFA2]] | +0.76 | +0.73 / +0.52 | both halves | 1e-05 |  |
| [[CCDC30]] | +0.76 | +0.76 / +0.45 | both halves | 3e-05 |  |
| [[DPH6-DT]] | +0.75 | +0.75 / +0.50 | both halves | 1e-05 |  |
| [[MMADHC-DT]] | +0.75 | +0.70 / +0.43 | both halves | 3e-05 |  |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[LINC02641]] | B | LINC02641 activity raises CFAP418-AS1's level | lines that do not express LINC02641 (14) vs lines expressing it (36) | 1.68× lower at baseline in the lines without LINC02641 | 0.047 | ⚠ within organs, on part of the lines; also absent: PSD2, LINC02940, ENSG00000250101; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers CFAP418-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 6.7% of all compounds | 0.059 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[FLJ12825]] | B | FLJ12825 activity raises CFAP418-AS1's level | lines that do not express FLJ12825 (15) vs lines expressing it (35) | 1.91× lower at baseline in the lines without FLJ12825 | 0.073 | ⚠ within organs, on part of the lines; also absent: HOXC10, HOXC6, HOXC8; maybe low, not absent |
| [[SYT9-AS1]] | B | SYT9-AS1 activity raises CFAP418-AS1's level | lines that do not express SYT9-AS1 (8) vs lines expressing it (42) | 1.58× lower at baseline in the lines without SYT9-AS1 | 0.091 | ⚠ within organs, on part of the lines; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 026]]; 163 genes; this gene is in the **+** arm (projection on the module's main direction 0.808). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.40).
- **Nodal map** (x, y) = (8.5, 16.4); signed map (29.1, -9.4). **Vector** length 102, 25.3% of its response variance represented; |z| ≥ 3 in 1,157 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +10.3 | +30.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +7.1 | +11.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +6.9 | +11.0 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.9 | +9.8 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +9.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.2 | +6.0 |
|  | [[Cobimetinib (drug)]] 5 µM |  | +4.0 | +6.8 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | +3.3 | +4.5 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.3 | +1.6 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -6.6 | -3.6 |
|  | [[Belinostat (drug)]] 0.5 µM |  | -6.4 | -5.9 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -5.2 | -0.9 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -4.7 | -5.0 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -4.6 | -0.4 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.8 | -5.4 |
|  | [[Brivudine (drug)]] 5 µM |  | -2.8 | +0.1 |
|  | [[Belinostat (drug)]] 0.05 µM |  | -2.2 | -0.7 |
|  | [[Peretinoin (drug)]] 5 µM |  | -2.1 | -3.9 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -2.0 | -4.8 |

## What is on record

|  |  |
|---|---|
| Name | CFAP418 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 8q22.1 — chr8:95,204,456-95,811,254 (+) |
| Ensembl biotype | lncRNA |
| Also known as | tospeak; previously C8orf37-AS1 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

**Summary**, from NCBI Gene [100616530](https://www.ncbi.nlm.nih.gov/gene/100616530):

> Predicted to enable triplet codon-amino acid adaptor activity. Predicted to be involved in translation. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:50444](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:50444) · Entrez [100616530](https://www.ncbi.nlm.nih.gov/gene/100616530) · Ensembl [ENSG00000253773](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000253773)

## Data

Gene col 14840: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 14840); `tables/drug_effects.parquet` (58 rows, flagged included); `relations/gene_relations.parquet` (col_a == 14840, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 14840]; `tensor/DDL_lfc|DDL_z.npy` [14840]; `embed/gene_vectors.npy` [14840]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 14840 or target_col == 14840). Every well: [[CFAP418-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CFAP418-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
