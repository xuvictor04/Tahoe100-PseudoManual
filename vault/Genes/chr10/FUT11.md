---
symbol: "FUT11"
type: "gene"
col: 12313
ensembl_id: "ENSG00000196968"
name: "protein O-fucosyltransferase 4"
location: "10q22.2"
module: 144
arm: "+"
pooled_cpm: 123.53
n_lines_expressing: 50
n_dd_up: 0
n_dd_down: 34
n_dd_up_clean: 0
n_dd_down_clean: 22
in_vector_space: true
direction_upstream: 4
direction_downstream: 0
tags: ["gene", "module/144"]
generated_by: "tahoemap"
---

# FUT11

*protein O-fucosyltransferase 4* — 10q22.2

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 2.60×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.137× (z -34.0, q 0e+00, down in 48 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EFCAB3P1]] (+0.77, fdr 7e-06), [[FAM162A]] (+0.76, fdr 7e-06), [[C4orf47]] (+0.75, fdr 7e-06); moves opposite to [[SGPL1]] (-0.67, fdr 3e-05), [[SLC25A24]] (-0.65, fdr 1e-05), [[GNG12]] (-0.62, fdr 4e-04).
> It is in [[Module 144]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 4 arrows point to it, the strongest [[NR2F2-AS1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12313.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Topotecan (hydrochloride) (drug)]] 5 µM in 1 line (NCI-H2030 2.60×; ⚠ toxic; cell-cycle shift, explains ~0% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Sapanisertib (drug)]] 0.5 µM |  | 1.50× | +3.5 | 0.24 | 33/48 (LoVo, C-33 A, …) | inconsistent across doses | plate-row cell shift; noisy plate (z scaled) |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 0.5 µM |  | 1.31× | +3.3 | 0.24 | 31/48 (NCI-H23, PANC-1, …) | inconsistent across doses |  |
| [[PF-06260933 (drug)]] 5 µM |  | 1.66× | +3.2 | 0.24 | 28/48 (CFPAC-1, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Entrectinib (drug)]] 5 µM |  | 1.29× | +3.1 | 0.24 | 24/48 (AsPC-1, NCI-H2030, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 12 with an alert ⚠; shown: the 15 strongest and the 7 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12313.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **0.137×** | -34.0 | 0e+00 | 48/48 (C32, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 5 µM |  | **0.185×** | -20.4 | 0e+00 | 47/48 (KATO III, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.201×** | -18.6 | 0e+00 | 48/48 (NCI-H460, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.260×** | -16.3 | 0e+00 | 47/48 (C32, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.271×** | -15.8 | 0e+00 | 47/48 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.276×** | -15.5 | 0e+00 | 48/48 (hTERT-HPNE, HT-29, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.355×** | -12.0 | 2e-31 | 44/47 (C-33 A, NCI-H1573, …) | top dose only | cell-cycle shift (explains ~1% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.369×** | -11.6 | 4e-29 | 40/44 (RPMI-7951, Hs 766T, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.413×** | -10.7 | 9e-25 | 44/49 (Hs 766T, HCT15, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here); composition shift |
| [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **0.510×** | -8.1 | 3e-14 | 42/48 (HOP62, LOX-IMVI, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.515×** | -8.0 | 6e-14 | 45/48 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.669×** | -6.8 | 4e-10 | 36/49 (CHP-212, SNU-423, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.486×** | -6.6 | 1e-09 | 40/48 (SNU-423, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~13% here); noisy plate (z scaled) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~29% of this change | **0.684×** | -6.5 | 4e-09 | 37/48 (SNU-423, NCI-H1573, …) | rises with dose | low cells (technical?) |
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.398×** | -5.8 | 2e-07 | 35/45 (SNU-423, LOX-IMVI, …) | inconsistent across doses | cell-cycle shift (explains ~17% here); noisy plate (z scaled) |
| [[Brivudine (drug)]] 5 µM |  | **0.402×** | -5.8 | 3e-07 | 46/49 (SK-MEL-2, RPMI-7951, …) | top dose only | plate-row cell shift; noisy plate (z scaled); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **0.729×** | -5.4 | 3e-06 | 39/48 (LoVo, HT-29, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.735×** | -5.2 | 5e-06 | 38/48 (HOP62, A-172, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.640×** | -5.2 | 7e-06 | 37/48 (NCI-H1573, C-33 A, …) | top dose only |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.448×** | -5.1 | 1e-05 | 41/48 (Hs 766T, RKO, …) | inconsistent across doses | plate-row cell shift; composition shift; noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.663×** | -4.9 | 2e-05 | 38/48 (HOP62, C32, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **0.688×** | -4.5 | 2e-04 | 38/48 (hTERT-HPNE, SW 900, …) | rises with dose | cell-cycle shift (explains ~13% here) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.45 per unit of S-phase module lfc, +0.43 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12313. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SNU-423 (line)]] | alt | 203 | 0 | 13 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.148× (z -25.5) |
| [[NCI-H460 (line)]] | wt | 150 | 0 | 12 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0922× (z -31.5) |
| [[HT-29 (line)]] | alt | 138 | 0 | 11 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0776× (z -29.6) |
| [[A-172 (line)]] | wt | 144 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0854× (z -31.2) |
| [[C-33 A (line)]] | alt | 181 | 0 | 10 (3 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0296× (z -27.6) ⚠ toxic · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.154× (z -21.5) |
| [[C32 (line)]] | wt | 161 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0745× (z -32.4) |
| [[HOP62 (line)]] | alt | 231 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.112× (z -28.4) |
| [[Hs 766T (line)]] | wt | 154 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0886× (z -29.6) |
| [[LoVo (line)]] | wt | 98.2 | 0 | 10 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -22.0) |
| [[NCI-H1573 (line)]] | alt | 203 | 0 | 10 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0955× (z -23.7) |
| [[RPMI-7951 (line)]] | alt | 199 | 0 | 10 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0960× (z -31.2) |
| [[HCT15 (line)]] | alt | 264 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0917× (z -26.8) |
| [[hTERT-HPNE (line)]] | wt | 164 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -25.5) |
| [[KATO III (line)]] | alt | 88.3 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0981× (z -26.7) |
| [[LOX-IMVI (line)]] | wt | 115 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0966× (z -29.5) |
| [[SW 900 (line)]] | alt | 180 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0793× (z -31.3) |
| [[SW480 (line)]] | alt | 136 | 0 | 9 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.191× (z -20.3) |
| [[CHP-212 (line)]] | wt | 239 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0797× (z -22.8) |
| [[H4 (line)]] | wt | 209 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0916× (z -24.4) |
| [[HEC-1-A (line)]] | alt | 98.5 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.129× (z -25.3) |
| [[J82 (line)]] | alt | 95.1 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.211× (z -20.8) |
| [[NCI-H2347 (line)]] | alt | 77.3 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.117× (z -28.8) |
| [[Panc 03.27 (line)]] | alt | 111 | 0 | 8 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.151× (z -22.9) |
| [[SK-MEL-2 (line)]] | alt | 133 | 0 | 8 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.166× (z -22.1) |
| [[A549 (line)]] | wt | 98.4 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.134× (z -26.2) |
| [[CFPAC-1 (line)]] | alt | 191 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.232× (z -19.5) |
| [[LS 180 (line)]] | wt | 76.5 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.126× (z -21.7) |
| [[MIA PaCa-2 (line)]] | alt | 175 | 0 | 7 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0907× (z -29.0) |
| [[PANC-1 (line)]] | alt | 139 | 0 | 7 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.121× (z -32.2) |
| [[AsPC-1 (line)]] | alt | 75.5 | 0 | 6 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.146× (z -21.5) |
| [[COLO 205 (line)]] | alt | 102 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.127× (z -21.5) |
| [[HS-578T (line)]] | alt | 104 | 0 | 6 | — | [[Homoharringtonine (drug)]] 5 µM 0.163× (z -23.2) |
| [[NCI-H1792 (line)]] | alt | 128 | 0 | 6 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.162× (z -23.0) |
| [[HepG2_C3A (line)]] | wt | 102 | 0 | 5 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.185× (z -16.4) |
| [[NCI-H23 (line)]] | alt | 76.5 | 0 | 5 | — | [[Homoharringtonine (drug)]] 5 µM 0.249× (z -16.7) |
| [[BT-474 (line)]] | alt | 65.3 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.0961× (z -21.4) |
| [[NCI-H2030 (line)]] | alt | 71.5 | 1 (1 ⚠) | 3 | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.60× (z +8.7) ⚠ toxic; cell-cycle shift, explains ~0% of this change | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -22.2) |
| [[RKO (line)]] | wt | 60.8 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.156× (z -20.0) |
| [[SNU-1 (line)]] | wt | 88.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.170× (z -17.8) |
| [[SW48 (line)]] | wt | 99.3 | 0 | 4 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.200× (z -16.9) |
| [[A-427 (line)]] | wt | 62.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0539× (z -22.9) |
| [[A498 (line)]] | wt | 46.9 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.409× (z -11.1) |
| [[SHP-77 (line)]] | alt | 40.8 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.338× (z -9.3) |
| [[SW 1088 (line)]] | alt | 145 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0891× (z -10.4) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.217× (z -9.3) |
| [[SW 1271 (line)]] | alt | 138 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.0534× (z -18.3) |
| [[SW1417 (line)]] | alt | 58.2 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.193× (z -17.0) |
| [[AN3 CA (line)]] | alt | 112 | 0 | 1 | — | [[Harringtonine (drug)]] 5 µM 0.0793× (z -13.6) |
| [[NCI-H661 (line)]] | alt | 59.7 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.164× (z -9.4) |
| [[NCI-H2122 (line)]] | alt | 201 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12313), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*89 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EFCAB3P1]] | +0.77 | +0.75 / +0.72 | both halves | 7e-06 |  |
| [[FAM162A]] | +0.76 | +0.78 / +0.77 | both halves | 7e-06 |  |
| [[C4orf47]] | +0.75 | +0.69 / +0.79 | both halves | 7e-06 |  |
| [[HILPDA]] | +0.74 | +0.80 / +0.69 | both halves | 7e-06 |  |
| [[ENO2]] | +0.71 | +0.71 / +0.73 | both halves | 7e-06 |  |
| [[WDR45B]] | +0.71 | +0.71 / +0.69 | both halves | 7e-06 |  |
| [[SAP30]] | +0.71 | +0.68 / +0.65 | both halves | 7e-06 |  |
| [[SEC61G]] | +0.71 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[PRKRIP1]] | +0.71 | +0.76 / +0.66 | both halves | 7e-06 |  |
| [[C4orf3]] | +0.69 | +0.74 / +0.68 | both halves | 7e-06 |  |
| [[POM121C]] | +0.69 | +0.77 / +0.63 | both halves | 7e-06 |  |
| [[VKORC1]] | +0.69 | +0.70 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*11 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SGPL1]] | -0.67 | -0.43 / -0.69 | both halves | 3e-05 |  |
| [[SLC25A24]] | -0.65 | -0.55 / -0.57 | both halves | 1e-05 |  |
| [[GNG12]] | -0.62 | -0.26 / -0.67 | both halves | 4e-04 |  |
| [[XRN2]] | -0.59 | -0.54 / -0.63 | both halves | 1e-05 |  |
| [[EWSR1]] | -0.57 | -0.54 / -0.59 | both halves | 1e-05 |  |
| [[OCRL]] | -0.57 | -0.50 / -0.60 | both halves | 1e-05 |  |
| [[DARS2]] | -0.56 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[GMFB]] | -0.56 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[DHX9]] | -0.56 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[API5]] | -0.56 | -0.38 / -0.66 | both halves | 7e-05 |  |
| [[ELAC2]] | -0.55 | -0.50 / -0.60 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 2, C 2.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[NR2F2-AS1]] | B | NR2F2-AS1 activity raises FUT11's level | lines that do not express NR2F2-AS1 (8) vs lines expressing it (42) | 1.80× lower at baseline in the lines without NR2F2-AS1 | 0.008 | ⚠ within organs, on part of the lines; also absent: TMEFF1, RIMKLB, LHFPL6 |
| [[KDM2B-DT]] | B | KDM2B-DT activity raises FUT11's level | lines that do not express KDM2B-DT (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without KDM2B-DT | 0.082 | ⚠ within organs, on part of the lines; also absent: KATNAL2, TMEM170B, LHFPL6; maybe low, not absent |
| [[C4orf47]] | C | C4orf47 activity raises FUT11's level | lines that do not express C4orf47 (3) vs lines expressing it (47) | 2.16× lower at baseline in the lines without C4orf47 | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; co-absent genes; also absent: ENSG00000286162, CLEC2D, MPP4; its own permutation p |
| [[EFCAB3P1]] | C | EFCAB3P1 activity raises FUT11's level | lines that do not express EFCAB3P1 (3) vs lines expressing it (47) | 1.52× lower at baseline in the lines without EFCAB3P1 | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: FRZB, ENSG00000273184, CLEC2D; maybe low, not absent; its own permutation p |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 144]]; 32 genes; every member is in the + arm (projection on the module's main direction 0.785). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.30; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.2, -18.1); signed map (-33.5, 26.1). **Vector** length 129, 54.6% of its response variance represented; |z| ≥ 3 in 1,344 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | +5.2 | +0.2 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.9 | +0.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift | +4.5 | -0.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +4.4 | -0.2 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +4.1 | +2.6 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +3.7 | -0.3 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.5 | +1.9 |
| fall | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -12.9 | -11.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -12.6 | -10.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | -9.7 | -2.6 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -9.6 | -12.0 |
|  | [[Belumosudil (drug)]] 5 µM |  | -6.3 | -5.2 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -4.7 | -4.9 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.3 | -2.1 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.0 | -0.8 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -2.9 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | protein O-fucosyltransferase 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q22.2 — chr10:73,772,276-73,780,251 (+) |
| Ensembl biotype | protein_coding |
| Also known as | MGC33202; previously FUT11 |
| Gene groups (HGNC) | Fucosyltransferases |
| Reactome | 1 pathways, smallest: O-linked glycosylation |
| Matched by | ensembl_id |

**Function**, from UniProt [Q495W5](https://www.uniprot.org/uniprotkb/Q495W5) (GDP-fucose protein O-fucosyltransferase 4):

> Protein O-fucosyltransferase that specifically catalyzes O-fucosylation of serine or threonine residues in EMI domains of target proteins, such as MMRN1, MMRN2 and EMID1. Attaches fucose through an O-glycosidic linkage. O-fucosylation of EMI domain-containing proteins may be required for facilitating protein folding and secretion. Also shows minor alpha-(1,3)-fucosyltransferase activity toward activity toward biantennary N-glycan acceptors. However, this was tested with a library of synthetic …

**Summary**, from NCBI Gene [170384](https://www.ncbi.nlm.nih.gov/gene/170384):

> Enables peptide-O-fucosyltransferase activity. Involved in N-glycan processing and positive regulation of protein secretion. Is active in endoplasmic reticulum. Implicated in stomach cancer. Biomarker of stomach cancer. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:19233](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:19233) · Entrez [170384](https://www.ncbi.nlm.nih.gov/gene/170384) · UniProt [Q495W5](https://www.uniprot.org/uniprotkb/Q495W5) · Ensembl [ENSG00000196968](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196968)

## Data

Gene col 12313: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12313); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12313, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12313]; `tensor/DDL_lfc|DDL_z.npy` [12313]; `embed/gene_vectors.npy` [12313]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12313 or target_col == 12313). Every well: [[FUT11 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FUT11.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
