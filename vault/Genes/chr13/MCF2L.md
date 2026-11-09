---
symbol: "MCF2L"
type: "gene"
col: 4721
ensembl_id: "ENSG00000126217"
name: "MCF.2 cell line derived transforming sequence like"
location: "13q34"
module: 55
arm: "+"
pooled_cpm: 25.39
n_lines_expressing: 36
n_dd_up: 9
n_dd_down: 40
n_dd_up_clean: 9
n_dd_down_clean: 28
in_vector_space: true
direction_upstream: 21
direction_downstream: 37
tags: ["gene", "module/055"]
generated_by: "tahoemap"
---

# MCF2L

*MCF.2 cell line derived transforming sequence like* — 13q34

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (none with an alert); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +13.1, q 1e-36, up in 30 of 33 measured lines).
> Pooled over the cell lines (median), lowered significantly by 40 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.433× (z -16.5, q 0e+00, down in 30 of 34 measured lines) ⚠ cell-cycle shift, explains ~38% of this change. The strongest without an alert is [[Homoharringtonine (drug)]] 0.5 µM: 0.360× (z -14.2, q 2e-43, down in 27 of 31 measured lines).
> Its strongest partners by |cos| (98 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGAP8]] (+0.60, fdr 2e-05), [[LINC01814]] (+0.60, fdr 1e-05), [[ATP2C2]] (+0.59, fdr 3e-05); moves opposite to [[ZNF407-AS1]] (-0.50, fdr 2e-04), [[MFF-DT]] (-0.50, fdr 1e-04), [[CLIP1]] (-0.50, fdr 1e-04).
> It is in [[Module 055]], a single-armed module (Regulation of FZD by ubiquitination).
> Probable direction (from the cell lines, not proof of direct regulation): 21 arrows point to it, the strongest [[TJP3]] → it (grade B ⚠); 37 go from it, the strongest it → [[ATP11A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, none with an alert. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4721.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +13.1 | 1e-36 | 30/33 (AsPC-1, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.31×** | +11.7 | 4e-29 | 31/33 (AsPC-1, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | **1.43×** | +7.1 | 3e-10 | 18/34 (SW1417, NCI-H2347, …) | rises with dose |  |
| [[Belinostat (drug)]] 5 µM |  | **1.53×** | +5.9 | 4e-07 | 17/33 (AsPC-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.42×** | +5.0 | 8e-05 | 14/33 (AsPC-1, HepG2/C3A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.68×** | +3.8 | 0.013 | 13/34 (AsPC-1, LoVo, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | 1.19× | +3.4 | 0.045 | 8/34 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Entecavir (monohydrate) (drug)]] 5 µM |  | **1.29×** | +3.4 | 0.045 | 8/33 (CFPAC-1, COLO 205, …) | top dose only | plate-row cell shift; position effect removed |
| [[Lactate (calcium) (drug)]] 0.5 µM |  | **1.26×** | +3.3 | 0.062 | 6/32 (SW 900, RKO, …) | inconsistent across doses |  |
| [[Sivelestat (sodium tetrahydrate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.062 | 7/33 (COLO 205, HT-29, …) | top dose only | plate-row cell shift |
| [[Cepharanthine (drug)]] 5 µM |  | 1.17× | +3.2 | 0.069 | 8/34 (HCT15, LS 180, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 40 in all, 12 with an alert ⚠; shown: the 15 strongest and the 6 next strongest without an alert. 40 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4721.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.433×** | -16.5 | 0e+00 | 30/34 (HEC-1-A, NCI-H2030, …) | all doses, stronger at high dose | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.360×** | -14.2 | 2e-43 | 27/31 (CFPAC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.371×** | -13.3 | 4e-38 | 29/33 (SW480, LoVo, …) | rises with dose | composition shift |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.386×** | -13.3 | 4e-38 | 26/33 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here); composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.441×** | -11.4 | 4e-28 | 27/32 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.470×** | -10.5 | 6e-24 | 28/32 (RKO, NCI-H2030, …) | all doses, stronger at high dose | cell-cycle shift (explains ~16% here) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.463×** | -10.3 | 5e-23 | 24/32 (SW 900, LoVo, …) | top dose only | cell-cycle shift (explains ~14% here) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.488×** | -10.0 | 1e-21 | 26/33 (A-427, A-172, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.493×** | -9.8 | 5e-21 | 26/32 (HT-29, H4, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.574×** | -7.7 | 6e-13 | 21/33 (SW480, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.687×** | -7.4 | 7e-12 | 21/33 (NCI-H2030, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.582×** | -7.3 | 2e-11 | 13/23 (A-172, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~19% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **0.616×** | -6.7 | 6e-10 | 18/30 (NCI-H1573, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.623×** | -6.6 | 2e-09 | 21/33 (SW480, HepG2/C3A, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.646×** | -6.1 | 5e-08 | 18/32 (A-172, MIA PaCa-2, …) | all doses, stronger at high dose |  |
| [[TAK-901 (drug)]] 5 µM |  | **0.492×** | -5.2 | 8e-06 | 18/33 (HEC-1-A, A-427, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~22% here); composition shift; noisy plate (z scaled) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.771×** | -5.1 | 1e-05 | 14/33 (SW480, HT-29, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.692×** | -4.8 | 4e-05 | 18/32 (SW480, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.749×** | -3.9 | 0.003 | 17/32 (A-427, HT-29, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | **0.752×** | -3.8 | 0.003 | 11/34 (SW480, MIA PaCa-2, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.597×** | -3.8 | 0.004 | 9/32 (MIA PaCa-2, SW480, …) | rises with dose | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.12 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4721. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 90.8 | 0 | 14 (7 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.181× (z -16.6) |
| [[HEC-1-A (line)]] | alt | 43.4 | 0 | 9 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.238× (z -17.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.261× (z -11.3) |
| [[HT-29 (line)]] | alt | 53.4 | 0 | 7 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.140× (z -11.7) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.191× (z -10.2) |
| [[MIA PaCa-2 (line)]] | alt | 16.1 | 0 | 7 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0951× (z -12.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.173× (z -9.7) |
| [[A-172 (line)]] | wt | 40.8 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.199× (z -16.1) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.241× (z -10.0) |
| [[A-427 (line)]] | wt | 37.7 | 0 | 6 (2 ⚠) | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.0628× (z -17.4) |
| [[LoVo (line)]] | wt | 29.3 | 0 | 6 (4 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.201× (z -13.5) ⚠ cell-cycle shift, explains ~26% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.219× (z -13.3) |
| [[NCI-H1573 (line)]] | alt | 47.8 | 0 | 6 (4 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -11.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.180× (z -11.1) |
| [[NCI-H2030 (line)]] | alt | 36.5 | 0 | 6 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.180× (z -17.0) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.348× (z -10.4) |
| [[COLO 205 (line)]] | alt | 97.1 | 0 | 4 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.207× (z -14.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.254× (z -8.9) |
| [[NCI-H23 (line)]] | alt | 38.3 | 0 | 4 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.176× (z -15.5) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.179× (z -10.8) |
| [[C32 (line)]] | wt | 35.3 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.285× (z -9.6) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.186× (z -9.1) |
| [[CFPAC-1 (line)]] | alt | 21.0 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.105× (z -13.3) |
| [[HCT15 (line)]] | alt | 42.3 | 0 | 3 (1 ⚠) | — | [[Thymol (drug)]] 0.5 µM 0.190× (z -9.6) |
| [[RKO (line)]] | wt | 19.3 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.172× (z -14.7) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.209× (z -9.2) |
| [[AN3 CA (line)]] | alt | 44.3 | 0 | 2 | — | [[Harringtonine (drug)]] 0.5 µM 0.109× (z -9.1) |
| [[AsPC-1 (line)]] | alt | 7.33 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 10.5× (z +9.9) | — |
| [[HepG2_C3A (line)]] | wt | 35.4 | 0 | 2 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.146× (z -10.0) ⚠ toxic · without an alert: [[Ixazomib citrate (drug)]] 0.5 µM 0.178× (z -9.3) |
| [[SW 900 (line)]] | alt | 14.0 | 0 | 2 (2 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0587× (z -12.3) ⚠ toxic |
| [[SW48 (line)]] | wt | 33.5 | 0 | 2 | — | [[TAK-901 (drug)]] 0.05 µM 0.110× (z -10.9) |
| [[H4 (line)]] | wt | 29.4 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.0909× (z -13.6) ⚠ cell-cycle shift, explains ~38% of this change |
| [[NCI-H2347 (line)]] | alt | 12.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 4.02× (z +8.7) | — |
| [[SW1417 (line)]] | alt | 9.16 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.141× (z -8.6) |
| [[A498 (line)]] | wt | 3.44 n.m. | — | — | — | — |
| [[A549 (line)]] | wt | 5.66 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 56.6 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 24.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 32.2 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.07 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 3.08 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 2.32 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.28 n.m. | — | — | — | — |
| [[J82 (line)]] | alt | 2.64 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 49.3 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 4.48 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 36.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.48 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 33.6 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 6.21 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 32.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.8 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 3.56 n.m. | — | — | — | — |
| [[RPMI-7951 (line)]] | alt | 5.87 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 78.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.97 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.94 n.m. | — | — | — | — |
| [[SNU-423 (line)]] | alt | 2.89 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.14 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4721), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*86 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGAP8]] | +0.60 | +0.47 / +0.50 | both halves | 2e-05 | same gene group; pathway: RHOA GTPase cycle |
| [[LINC01814]] | +0.60 | +0.56 / +0.58 | both halves | 1e-05 |  |
| [[ATP2C2]] | +0.59 | +0.56 / +0.46 | both halves | 3e-05 |  |
| [[ACOT11]] | +0.57 | +0.53 / +0.53 | both halves | 1e-05 |  |
| [[NKD1]] | +0.56 | +0.51 / +0.51 | both halves | 1e-05 |  |
| [[LINC00659]] | +0.56 | +0.53 / +0.49 | both halves | 1e-05 |  |
| [[MROH7]] | +0.56 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[AZGP1]] | +0.56 | +0.53 / +0.47 | both halves | 2e-05 |  |
| [[ADGRG5]] | +0.55 | +0.46 / +0.56 | both halves | 2e-05 |  |
| [[LINC00299]] | +0.54 | +0.52 / +0.55 | both halves | 1e-05 |  |
| [[SPIRE2]] | +0.54 | +0.32 / +0.50 | both halves | 2e-04 |  |
| [[ENTPD2]] | +0.54 | +0.51 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*14 of its nearest partners move opposite, 2 of them with an alert (⚠; 2 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407-AS1]] | -0.50 | -0.47 / -0.32 | both halves | 2e-04 |  |
| [[MFF-DT]] | -0.50 | -0.45 / -0.34 | both halves | 1e-04 |  |
| [[CLIP1]] | -0.50 | -0.46 / -0.35 | both halves | 1e-04 |  |
| [[TSTD3]] | -0.49 | -0.43 / -0.29 | both halves | 2e-04 |  |
| [[ANXA2R-OT1]] | -0.48 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[RNPC3-DT]] | -0.48 | -0.47 / -0.16 | ⚠ not reproduced | 0.001 |  |
| [[UBXN2A]] | -0.48 | -0.50 / -0.26 | both halves | 4e-04 |  |
| [[ATE1OSP]] | -0.48 | -0.44 / -0.26 | both halves | 4e-04 |  |
| [[RNF115]] | -0.48 | -0.40 / -0.33 | both halves | 1e-04 |  |
| [[ZNF181]] | -0.47 | -0.45 / -0.30 | both halves | 2e-04 |  |
| [[NRIP1]] | -0.47 | -0.33 / -0.37 | both halves | 1e-04 |  |
| [[ZNF626]] | -0.46 | -0.49 / -0.08 | ⚠ not reproduced | 0.003 |  |
| [[NAIF1]] | -0.46 | -0.37 / -0.26 | both halves | 4e-04 |  |
| [[ZBED5]] | -0.46 | -0.41 / -0.25 | both halves | 4e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*21 arrows, 21 of them with an alert ⚠; grade A 0, B 17, C 4. Shown: the 12 strongest; 9 more arrows (9 of them with an alert ⚠) not shown.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TJP3]] | B | TJP3 activity raises MCF2L's level | lines that do not express TJP3 (29) vs lines expressing it (21) | 2.95× lower at baseline in the lines without TJP3 | 0.012 | ⚠ within organs, on part of the lines; also absent: KDF1, EPCAM, CDH1 |
| [[FAM83F]] | B | FAM83F activity raises MCF2L's level | lines that do not express FAM83F (32) vs lines expressing it (18) | 3.18× lower at baseline in the lines without FAM83F | 0.012 | ⚠ within organs, on part of the lines; also absent: SLC5A1, TRIM15, TMEM45B |
| [[GPR35]] | B | GPR35 activity raises MCF2L's level | lines that do not express GPR35 (29) vs lines expressing it (21) | 3.44× lower at baseline in the lines without GPR35 | 0.034 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: EPS8L3, CDH1, TNNT2; maybe low, not absent |
| [[ENPP5]] | B | ENPP5 activity raises MCF2L's level | lines that do not express ENPP5 (27) vs lines expressing it (23) | 2.52× lower at baseline in the lines without ENPP5 | 0.048 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: TMEM125, ESRP1, ENSG00000243004 |
| [[ZDHHC11B]] | B | ZDHHC11B activity raises MCF2L's level | lines that do not express ZDHHC11B (5) vs lines expressing it (45) | 4.99× lower at baseline in the lines without ZDHHC11B | 0.051 | ⚠ within organs, on part of the lines; also absent: CTSV, RTN4R, ATP11A; maybe low, not absent |
| [[LINC01814]] | B | LINC01814 activity raises MCF2L's level | lines that do not express LINC01814 (30) vs lines expressing it (20) | 3.22× lower at baseline in the lines without LINC01814 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LINC00299, TMEM45B, EPS8L3 |
| [[AXIN2]] | B | AXIN2 activity raises MCF2L's level | lines that do not express AXIN2 (32) vs lines expressing it (18) | 3.54× lower at baseline in the lines without AXIN2 | 0.056 | ⚠ within organs, on part of the lines; co-occurs with CDKN2A; also absent: LGR5, LINC02253, LINC02964 |
| [[STXBP6]] | B | STXBP6 activity raises MCF2L's level | lines that do not express STXBP6 (22) vs lines expressing it (28) | 1.86× lower at baseline in the lines without STXBP6 | 0.057 | ⚠ within organs, on part of the lines; also absent: LINC00992, POU3F3, LINC01748 |
| [[NXPH4]] | B | NXPH4 activity strengthens MCF2L's drug response | lines that do not express NXPH4 (9) vs lines expressing it (25) | the lines without NXPH4 respond 0.74× as strongly (z diff +1.76); strongest at Harringtonine 5 µM: 0.53x vs 0.29x (z diff +3.6) | 0.060 | ⚠ within organs, on part of the lines; also absent: LINC01234; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[SLC52A3]] | B | SLC52A3 activity raises MCF2L's level | lines that do not express SLC52A3 (26) vs lines expressing it (24) | 2.40× lower at baseline in the lines without SLC52A3 | 0.060 | ⚠ within organs, on part of the lines; also absent: SPINT2, ENSG00000267748, CLDN7 |
| [[RAPGEF5]] | B | RAPGEF5 activity raises MCF2L's level | lines that do not express RAPGEF5 (17) vs lines expressing it (33) | 2.21× lower at baseline in the lines without RAPGEF5 | 0.071 | ⚠ within organs, on part of the lines; also absent: HSH2D, HOOK1, SAMD12; maybe low, not absent |
| [[AZGP1]] | B | AZGP1 activity raises MCF2L's level | lines that do not express AZGP1 (35) vs lines expressing it (15) | 2.15× lower at baseline in the lines without AZGP1 | 0.084 | ⚠ within organs, on part of the lines; also absent: GJB1, PROM1, LYZ |

### Downstream of this gene

*37 arrows, 37 of them with an alert ⚠; grade A 0, B 34, C 3. Shown: the 12 strongest; 25 more arrows (25 of them with an alert ⚠) not shown.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ATP11A]] | B | MCF2L activity raises ATP11A's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without MCF2L | 0.003 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[TJP3]] | B | MCF2L activity raises TJP3's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 3.59× lower at baseline in the lines without MCF2L | 0.007 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[LMTK3]] | B | MCF2L activity raises LMTK3's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.34× lower at baseline in the lines without MCF2L | 0.013 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[CHKA]] | B | MCF2L activity raises CHKA's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.51× lower at baseline in the lines without MCF2L | 0.015 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[AZGP1]] | B | MCF2L activity raises AZGP1's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.59× lower at baseline in the lines without MCF2L | 0.021 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[TMEM63C]] | B | MCF2L activity raises TMEM63C's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.02× lower at baseline in the lines without MCF2L | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[SPIRE2]] | B | MCF2L activity raises SPIRE2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.77× lower at baseline in the lines without MCF2L | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[SLC29A2]] | B | MCF2L activity raises SLC29A2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.71× lower at baseline in the lines without MCF2L | 0.022 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[PKP2]] | B | MCF2L activity raises PKP2's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.79× lower at baseline in the lines without MCF2L | 0.023 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[RAPGEF5]] | B | MCF2L activity raises RAPGEF5's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 3.00× lower at baseline in the lines without MCF2L | 0.028 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[MMP15]] | B | MCF2L activity raises MMP15's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 1.98× lower at baseline in the lines without MCF2L | 0.029 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |
| [[MLXIPL]] | B | MCF2L activity raises MLXIPL's level | lines that do not express MCF2L (14) vs lines expressing it (36) | 2.55× lower at baseline in the lines without MCF2L | 0.042 | ⚠ within organs, on part of the lines; also absent: B4GALNT3, CGN, HSD11B2 |

## Where it sits

- **Module**: [[Module 055]] — Regulation of FZD by ubiquitination; 87 genes; every member is in the + arm (projection on the module's main direction 0.473). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.31; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (20.7, 46.6); signed map (61.0, 11.1). **Vector** length 87.2, 20.9% of its response variance represented; |z| ≥ 3 in 958 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 5 µM |  | +3.7 | +13.1 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | +3.0 | +11.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +2.9 | +7.1 |
|  | [[Belinostat (drug)]] 5 µM |  | +2.5 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +2.3 | -6.7 |
|  | [[PF-06260933 (drug)]] 5 µM |  | +1.9 | +1.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.6 | +0.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +1.2 | +2.0 |
|  | [[crizotinib (drug)]] 5 µM |  | +1.1 | +0.1 |
| fall | [[Homoharringtonine (drug)]] 0.5 µM |  | -4.2 | -14.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -3.5 | -3.1 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | -3.0 | -13.3 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -2.5 | -10.0 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -2.4 | -3.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | -2.3 | -3.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | +1.1 |
|  | [[Trametinib (drug)]] 0.05 µM |  | -2.0 | +0.5 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -1.9 | +0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 5 µM |  | -1.7 | -1.0 |

## What is on record

|  |  |
|---|---|
| Name | MCF.2 cell line derived transforming sequence like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 13q34 — chr13:112,894,378-113,099,742 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0362, DBS, OST, ARHGEF14 |
| Gene groups (HGNC) | Pleckstrin homology domain containing; Dbl family Rho GEFs; Spectrin repeat containing; CRAL-TRIO lipid binding domain containing; SH3 domain containing |
| Reactome | 16 pathways, smallest: NRAGE signals death through JNK; G alpha (12/13) signalling events; RHOB GTPase cycle |
| Matched by | ensembl_id |

**Function**, from UniProt [O15068](https://www.uniprot.org/uniprotkb/O15068) (Guanine nucleotide exchange factor DBS):

> Guanine nucleotide exchange factor that catalyzes guanine nucleotide exchange on RHOA and CDC42, and thereby contributes to the regulation of RHOA and CDC42 signaling pathways (By similarity). Seems to lack activity with RAC1. Becomes activated and highly tumorigenic by truncation of the N-terminus (By similarity). Isoform 5 activates CDC42.; [Isoform 3]: Does not catalyze guanine nucleotide exchange on CDC42.

**Summary**, from NCBI Gene [23263](https://www.ncbi.nlm.nih.gov/gene/23263):

> This gene encodes a guanine nucleotide exchange factor that interacts specifically with the GTP-bound Rac1 and plays a role in the Rho/Rac signaling pathways. A variant in this gene was associated with osteoarthritis. Alternative splicing results in multiple transcript variants. [provided by RefSeq, Mar 2016]

**Accessions** — [HGNC:14576](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:14576) · Entrez [23263](https://www.ncbi.nlm.nih.gov/gene/23263) · UniProt [O15068](https://www.uniprot.org/uniprotkb/O15068) · Ensembl [ENSG00000126217](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000126217)

## Data

Gene col 4721: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4721); `tables/drug_effects.parquet` (51 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4721, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4721]; `tensor/DDL_lfc|DDL_z.npy` [4721]; `embed/gene_vectors.npy` [4721]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4721 or target_col == 4721). Every well: [[MCF2L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MCF2L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
