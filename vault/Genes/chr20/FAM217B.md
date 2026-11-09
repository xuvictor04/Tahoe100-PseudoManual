---
symbol: "FAM217B"
type: "gene"
col: 12159
ensembl_id: "ENSG00000196227"
name: "family with sequence similarity 217 member B"
location: "20q13.33"
module: 64
arm: "+"
pooled_cpm: 23.09
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 26
n_dd_up_clean: 11
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/064"]
generated_by: "tahoemap"
---

# FAM217B

*family with sequence similarity 217 member B* — 20q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Topotecan (hydrochloride) (drug)]] 5 µM: 1.86× (z +8.7, q 1e-15, up in 37 of 44 measured lines) ⚠ toxic. The strongest without an alert is [[Ponatinib (drug)]] 5 µM: 1.74× (z +8.1, q 2e-13, up in 38 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 26 drug-doses (7 with an alert ⚠); the strongest is [[Ouabain (Octahydrate) (drug)]] 5 µM: 0.294× (z -17.9, q 0e+00, down in 44 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SPR]] (+0.69, fdr 7e-06), [[CDC40]] (+0.65, fdr 7e-06), [[PPP1R3D]] (+0.62, fdr 7e-06, ⚠ same locus), [[EFCAB7]] (+0.60, fdr 7e-06); moves opposite to [[CFL1]] (-0.51, fdr 2e-05), [[SLC35F5]] (-0.50, fdr 4e-05), [[AGRN]] (-0.50, fdr 3e-05).
> It sits in the **+** arm of [[Module 064]] (proteasome).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[F3]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12159.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.86×** | +8.7 | 1e-15 | 37/44 (HEC-1-A, HT-29, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +8.1 | 2e-13 | 38/48 (HOP62, CFPAC-1, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.59×** | +6.8 | 2e-09 | 32/47 (CFPAC-1, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.36×** | +6.3 | 4e-08 | 28/48 (RKO, A-172, …) | top dose only | low cells (technical?) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.45×** | +5.4 | 6e-06 | 26/47 (HT-29, NCI-H1792, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.44×** | +5.1 | 4e-05 | 23/48 (LoVo, HOP62, …) | inconsistent across doses | cell-cycle shift (explains ~21% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **1.39×** | +4.8 | 1e-04 | 20/47 (HOP62, COLO 205, …) | two highest doses |  |
| [[Radotinib (drug)]] 5 µM |  | **1.24×** | +4.5 | 5e-04 | 22/48 (NCI-H1792, RPMI-7951, …) | top dose only |  |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.32×** | +4.0 | 0.003 | 22/47 (HOP62, LS 180, …) | two highest doses | cell-cycle shift (explains ~11% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +4.0 | 0.004 | 16/43 (AsPC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 5 µM |  | **1.32×** | +3.9 | 0.006 | 16/48 (NCI-H23, LOX-IMVI, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM |  | **1.62×** | +3.7 | 0.010 | 14/45 (NCI-H23, A-427, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.28×** | +3.7 | 0.011 | 15/48 (CFPAC-1, PANC-1, …) | top dose only |  |
| [[Cabozantinib (S-malate) (drug)]] 5 µM |  | **1.26×** | +3.3 | 0.035 | 8/47 (AsPC-1, PANC-1, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 28 in all, 8 with an alert ⚠; shown: the 15 strongest and the 5 next strongest without an alert. 26 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12159.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.294×** | -17.9 | 0e+00 | 44/48 (SW480, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~9% here); composition shift; position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.336×** | -15.9 | 0e+00 | 41/47 (HT-29, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.406×** | -13.2 | 3e-37 | 42/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **0.538×** | -12.8 | 2e-35 | 34/47 (NCI-H23, HT-29, …) | rises with dose | cell-cycle shift (explains ~18% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.423×** | -12.6 | 3e-34 | 39/47 (SW480, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.550×** | -8.7 | 2e-16 | 31/47 (A498, A-427, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.699×** | -7.4 | 1e-11 | 28/47 (SNU-1, HepG2/C3A, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.587×** | -7.2 | 5e-11 | 25/38 (HEC-1-A, Panc 03.27, …) | inconsistent across doses | cell-cycle shift (explains ~16% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.393×** | -7.1 | 6e-11 | 33/48 (SK-MEL-2, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~9% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 5 µM |  | **0.612×** | -6.9 | 3e-10 | 30/47 (NCI-H1573, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~21% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.417×** | -6.7 | 1e-09 | 30/46 (LOX-IMVI, C-33 A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.646×** | -6.1 | 4e-08 | 28/44 (MIA PaCa-2, RPMI-7951, …) | rises with dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.661×** | -6.1 | 6e-08 | 26/47 (LS 180, SNU-1, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | **0.680×** | -5.6 | 7e-07 | 27/47 (A-172, SK-MEL-2, …) | rises with dose |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.690×** | -5.4 | 2e-06 | 23/47 (HT-29, SW1417, …) | inconsistent across doses |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **0.701×** | -5.0 | 2e-05 | 21/48 (A-172, C-33 A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.715×** | -4.9 | 3e-05 | 25/47 (SW1417, LS 180, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.727×** | -4.5 | 2e-04 | 25/47 (C32, AsPC-1, …) | top dose only | cell-cycle shift (explains ~8% here) |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.823×** | -4.0 | 0.002 | 19/48 (MIA PaCa-2, SW480, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 0.835× | -3.7 | 0.005 | 18/48 (Hs 766T, MIA PaCa-2, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.17 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12159. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 22.8 | 0 | 12 (4 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.0856× (z -20.0) |
| [[PANC-1 (line)]] | alt | 22.4 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.151× (z -16.0) |
| [[SW480 (line)]] | alt | 31.8 | 0 | 7 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.147× (z -18.7) |
| [[NCI-H1573 (line)]] | alt | 20.9 | 0 | 6 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0947× (z -15.1) |
| [[SW1417 (line)]] | alt | 52.2 | 0 | 6 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.141× (z -17.4) ⚠ toxic; transcription drop · without an alert: [[Ouabain (Octahydrate) (drug)]] 5 µM 0.242× (z -12.6) |
| [[HT-29 (line)]] | alt | 34.3 | 0 | 5 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -19.0) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 5 µM 0.292× (z -15.2) |
| [[KATO III (line)]] | alt | 20.5 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0775× (z -15.4) |
| [[SW 900 (line)]] | alt | 20.4 | 0 | 4 | — | [[Homoharringtonine (drug)]] 5 µM 0.212× (z -12.7) |
| [[COLO 205 (line)]] | alt | 26.4 | 0 | 3 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.120× (z -12.0) |
| [[HepG2_C3A (line)]] | wt | 20.2 | 0 | 3 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.135× (z -12.7) |
| [[NCI-H23 (line)]] | alt | 51.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.268× (z -16.3) |
| [[SNU-1 (line)]] | wt | 38.8 | 0 | 3 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0710× (z -15.1) |
| [[A-427 (line)]] | wt | 46.2 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.131× (z -19.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.235× (z -13.8) |
| [[A498 (line)]] | wt | 18.5 | 0 | 2 | — | [[Homoharringtonine (drug)]] 5 µM 0.267× (z -14.5) |
| [[HEC-1-A (line)]] | alt | 27.0 | 1 (1 ⚠) | 1 (1 ⚠) | [[Topotecan (hydrochloride) (drug)]] 5 µM 2.97× (z +9.4) ⚠ toxic | [[Dinaciclib (drug)]] 0.05 µM 0.0729× (z -21.8) ⚠ toxic; transcription drop |
| [[Hs 766T (line)]] | wt | 47.4 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.215× (z -12.4) |
| [[LS 180 (line)]] | wt | 26.9 | 0 | 2 (1 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.313× (z -9.1) |
| [[Panc 03.27 (line)]] | alt | 29.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.122× (z -14.3) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 8.83 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.170× (z -8.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.8 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.323× (z -8.8) |
| [[AsPC-1 (line)]] | alt | 13.4 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.129× (z -9.2) |
| [[C-33 A (line)]] | alt | 53.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.290× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change |
| [[C32 (line)]] | wt | 11.1 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0877× (z -10.0) |
| [[H4 (line)]] | wt | 12.2 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 0.5 µM 0.0528× (z -11.1) |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.176× (z -8.7) |
| [[HOP62 (line)]] | alt | 10.6 | 0 | 1 | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.182× (z -9.4) |
| [[LoVo (line)]] | wt | 12.0 | 0 | 1 | — | [[Homoharringtonine (drug)]] 5 µM 0.340× (z -9.9) |
| [[LOX-IMVI (line)]] | wt | 16.6 | 0 | 1 | — | [[Digitoxin (drug)]] 0.5 µM 0.167× (z -9.9) |
| [[MIA PaCa-2 (line)]] | alt | 17.9 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.145× (z -11.2) ⚠ toxic |
| [[NCI-H2030 (line)]] | alt | 31.6 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.115× (z -14.8) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 23.6 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.118× (z -12.1) |
| [[RPMI-7951 (line)]] | alt | 24.5 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.192× (z -8.9) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.171× (z -9.2) ⚠ toxic; transcription drop |
| [[SK-MEL-2 (line)]] | alt | 23.3 | 0 | 1 | — | [[TAK-901 (drug)]] 5 µM 0.0599× (z -8.8) |
| [[SNU-423 (line)]] | alt | 23.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.248× (z -8.8) ⚠ toxic; transcription drop |
| [[SW 1271 (line)]] | alt | 56.1 | 0 | 1 | — | [[Pioglitazone (drug)]] 0.5 µM 0.0921× (z -8.6) |
| [[SW48 (line)]] | wt | 25.4 | 0 | 1 | — | [[Irinotecan (hydrochloride) (drug)]] 0.05 µM 0.0464× (z -14.2) |
| [[AN3 CA (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 9.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 13.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 9.65 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 57.5 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 15.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12159), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 3 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SPR]] | +0.69 | +0.77 / +0.60 | both halves | 7e-06 |  |
| [[CDC40]] | +0.65 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[PPP1R3D]] | +0.62 | +0.65 / +0.60 | both halves | 7e-06 | STRING 546; ⚠ same locus (0.0 kb: neighbours can correlate without regulation) |
| [[EFCAB7]] | +0.60 | +0.63 / +0.62 | both halves | 7e-06 |  |
| [[ZFP64]] | +0.60 | +0.42 / +0.60 | both halves | 4e-05 |  |
| [[GNPDA2]] | +0.59 | +0.65 / +0.48 | both halves | 2e-05 |  |
| [[BRF2]] | +0.59 | +0.59 / +0.54 | both halves | 1e-05 |  |
| [[TXNL1]] | +0.59 | +0.55 / +0.50 | both halves | 1e-05 |  |
| [[CASP6]] | +0.58 | +0.68 / +0.53 | both halves | 1e-05 |  |
| [[PIGB]] | +0.58 | +0.56 / +0.50 | both halves | 1e-05 |  |
| [[FAM241B]] | +0.58 | +0.55 / +0.60 | both halves | 1e-05 |  |
| [[CCDC43]] | +0.58 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[HIBCH]] | +0.57 | +0.62 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CFL1]] | -0.51 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[SLC35F5]] | -0.50 | -0.42 / -0.50 | both halves | 4e-05 |  |
| [[AGRN]] | -0.50 | -0.46 / -0.48 | both halves | 3e-05 |  |
| [[CD59]] | -0.49 | -0.46 / -0.51 | both halves | 3e-05 |  |
| [[GRK4]] | -0.47 | -0.27 / -0.40 | both halves | 3e-04 |  |
| [[DRAP1]] | -0.47 | -0.52 / -0.38 | both halves | 6e-05 |  |
| [[ARPC2]] | -0.46 | -0.42 / -0.51 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[F3]] | B | F3 activity lowers FAM217B's level | lines that do not express F3 (24) vs lines expressing it (26) | 1.48× higher at baseline in the lines without F3 | 0.075 | ⚠ within organs, on part of the lines; also absent: TLR2, KRT7, EDNRA |
| [[PIR]] | B | PIR activity raises FAM217B's level | lines that do not express PIR (10) vs lines expressing it (40) | 1.33× lower at baseline in the lines without PIR | 0.078 | ⚠ within organs, on part of the lines; also absent: VEGFD, ELMO1; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 064]] — proteasome; 77 genes; this gene is in the **+** arm (projection on the module's main direction 0.551). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.26).
- **Nodal map** (x, y) = (-19.1, -6.6); signed map (-26.4, -20.4). **Vector** length 98.0, 25.4% of its response variance represented; |z| ≥ 3 in 1,069 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +7.1 | +5.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +6.8 | +4.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +6.7 | +8.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +6.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +6.0 | +6.8 |
|  | [[Ponatinib (drug)]] 5 µM |  | +5.0 | +8.1 |
|  | [[Radotinib (drug)]] 5 µM |  | +3.8 | +4.5 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +3.0 | +0.3 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.3 | +3.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -7.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -7.0 | -7.2 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, would explain all of this change | -6.8 | -1.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~78% of this change | -6.7 | -2.6 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -5.9 | -5.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -3.4 | -3.7 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | -2.6 | -1.9 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -1.8 | -4.0 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -2.4 |
|  | [[vincristine (drug)]] 0.5 µM |  | -1.6 | +0.1 |

## What is on record

|  |  |
|---|---|
| Name | family with sequence similarity 217 member B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 20q13.33 — chr20:59,933,764-59,948,680 (+) |
| Ensembl biotype | protein_coding |
| Also known as | dJ551D2.5; previously C20orf177 |
| Matched by | ensembl_id |

UniProt [Q9NTX9](https://www.uniprot.org/uniprotkb/Q9NTX9) carries no function annotation.

**Summary**, from NCBI Gene [63939](https://www.ncbi.nlm.nih.gov/gene/63939):

> Located in nucleoplasm. [provided by Alliance of Genome Resources, Jun 2026]

**Accessions** — [HGNC:16170](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16170) · Entrez [63939](https://www.ncbi.nlm.nih.gov/gene/63939) · UniProt [Q9NTX9](https://www.uniprot.org/uniprotkb/Q9NTX9) · Ensembl [ENSG00000196227](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196227)

## Data

Gene col 12159: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12159); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12159, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12159]; `tensor/DDL_lfc|DDL_z.npy` [12159]; `embed/gene_vectors.npy` [12159]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12159 or target_col == 12159). Every well: [[FAM217B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/FAM217B.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
