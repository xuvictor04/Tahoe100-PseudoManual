---
symbol: "GOLPH3L"
type: "gene"
col: 6748
ensembl_id: "ENSG00000143457"
name: "golgi phosphoprotein 3 like"
location: "1q21.3"
module: 41
arm: "+"
pooled_cpm: 90.18
n_lines_expressing: 49
n_dd_up: 4
n_dd_down: 34
n_dd_up_clean: 3
n_dd_down_clean: 20
in_vector_space: true
direction_upstream: 6
direction_downstream: 0
tags: ["gene", "module/041"]
generated_by: "tahoemap"
---

# GOLPH3L

*golgi phosphoprotein 3 like* — 1q21.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (1 with an alert ⚠); the strongest is [[Terfenadine (drug)]] 5 µM: 1.22× (z +4.5, q 0.003, up in 24 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 34 drug-doses (14 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.546× (z -14.0, q 1e-41, down in 42 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[EAF2]] (+0.73, fdr 7e-06), [[SEC22A]] (+0.73, fdr 7e-06), [[ACBD3]] (+0.73, fdr 7e-06); moves opposite to [[TULP4]] (-0.66, fdr 7e-06), [[PRRC2B]] (-0.66, fdr 7e-06), [[PSME3]] (-0.65, fdr 7e-06).
> It sits in the **+** arm of [[Module 041]] (Intra-Golgi and retrograde Golgi-to-ER traffic).
> Probable direction (from the cell lines, not proof of direct regulation): 6 arrows point to it, the strongest [[AGR2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 2 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6748.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Terfenadine (drug)]] 5 µM |  | **1.22×** | +4.5 | 0.003 | 24/47 (A-172, MIA PaCa-2, …) | top dose only |  |
| [[Retinoic acid (drug)]] 5 µM |  | 1.20× | +4.1 | 0.012 | 24/48 (HCT15, Panc 03.27, …) | rises with dose |  |
| [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | **1.24×** | +3.7 | 0.037 | 17/47 (A-172, J82, …) | inconsistent across doses |  |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~68% of this change | **1.22×** | +3.5 | 0.070 | 18/47 (NCI-H23, A-427, …) | inconsistent across doses |  |
| [[Verteporfin (drug)]] 5 µM |  | **1.23×** | +3.4 | 0.070 | 16/48 (J82, hTERT-HPNE, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | 1.21× | +3.3 | 0.10 | 17/47 (A-427, AsPC-1, …) | rises with dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.19× | +3.1 | 0.15 | 21/47 (A-427, NCI-H460, …) | rises with dose |  |
| [[Ipatasertib (drug)]] 0.5 µM |  | 1.31× | +3.1 | 0.15 | 12/47 (NCI-H1792, LOX-IMVI, …) | inconsistent across doses | low cells (technical?); plate-row cell shift; noisy plate (z scaled) |
| [[Tucidinostat (drug)]] 0.05 µM |  | 1.19× | +3.0 | 0.16 | 13/47 (NCI-H2347, CFPAC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 47 in all, 18 with an alert ⚠; shown: the 15 strongest and the 10 next strongest without an alert. 34 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6748.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.546×** | -14.0 | 1e-41 | 42/48 (A498, NCI-H2347, …) | top dose only | cell-cycle shift (explains ~12% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change | **0.474×** | -13.0 | 4e-36 | 39/48 (CFPAC-1, SW 900, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.462×** | -12.9 | 5e-36 | 34/41 (KATO III, NCI-H1573, …) | all doses, flat | composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.453×** | -12.8 | 4e-35 | 32/43 (CFPAC-1, A549, …) | all doses, flat | cell-cycle shift (explains ~24% here); composition shift |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.512×** | -11.7 | 2e-29 | 46/47 (NCI-H1792, HT-29, …) | inconsistent across doses |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.570×** | -9.4 | 5e-19 | 38/47 (H4, A-172, …) | top dose only | cell-cycle shift (explains ~23% here) |
| [[Auranofin (drug)]] 5 µM |  | **0.583×** | -9.4 | 5e-19 | 37/47 (SW480, AsPC-1, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.584×** | -9.4 | 5e-19 | 37/47 (NCI-H460, AsPC-1, …) | rises with dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | **0.604×** | -8.8 | 1e-16 | 34/47 (NCI-H460, AsPC-1, …) | all doses, stronger at high dose |  |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -8.4 | 2e-15 | 37/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~25% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.626×** | -7.9 | 2e-13 | 32/49 (LS 180, A-172, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~27% of this change | **0.639×** | -7.5 | 3e-12 | 31/46 (NCI-H1573, NCI-H1792, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.657×** | -7.3 | 1e-11 | 38/47 (NCI-H460, SW480, …) | rises with dose |  |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.743×** | -6.8 | 4e-10 | 27/46 (CFPAC-1, AsPC-1, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.756×** | -6.4 | 4e-09 | 32/47 (COLO 205, A498, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.759×** | -4.8 | 5e-05 | 30/47 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.761×** | -4.8 | 6e-05 | 28/48 (HEC-1-A, KATO III, …) | inconsistent across doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **0.605×** | -4.6 | 1e-04 | 24/47 (Hs 766T, AsPC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Belumosudil (drug)]] 5 µM |  | **0.781×** | -4.1 | 1e-03 | 24/47 (PANC-1, A549, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.790×** | -4.1 | 1e-03 | 26/47 (HEC-1-A, LS 180, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.790×** | -4.1 | 1e-03 | 27/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[c-Kit-IN-1 (drug)]] 5 µM |  | **0.638×** | -4.1 | 1e-03 | 23/47 (A498, CFPAC-1, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Busulfan (drug)]] 5 µM |  | 0.836× | -4.0 | 0.001 | 19/48 (H4, MIA PaCa-2, …) | inconsistent across doses |  |
| [[Larotrectinib (drug)]] 0.05 µM |  | **0.794×** | -4.0 | 0.001 | 25/48 (LS 180, HEC-1-A, …) | inconsistent across doses |  |
| [[TAK-733 (drug)]] 5 µM |  | **0.655×** | -3.9 | 0.002 | 20/47 (Hs 766T, A498, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.33 per unit of S-phase module lfc, -0.07 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6748. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 68.8 | 0 | 12 (9 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.267× (z -14.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.304× (z -13.2) |
| [[CFPAC-1 (line)]] | alt | 192 | 0 | 10 (9 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.290× (z -18.5) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.379× (z -14.5) |
| [[NCI-H2347 (line)]] | alt | 133 | 0 | 8 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.371× (z -15.7) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.400× (z -14.6) |
| [[A498 (line)]] | wt | 133 | 0 | 7 (5 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.326× (z -17.1) |
| [[AsPC-1 (line)]] | alt | 79.9 | 0 | 7 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.231× (z -17.1) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.306× (z -10.3) |
| [[A549 (line)]] | wt | 90.5 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.220× (z -16.5) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.469× (z -11.9) |
| [[H4 (line)]] | wt | 106 | 0 | 6 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.197× (z -14.2) |
| [[Panc 03.27 (line)]] | alt | 109 | 0 | 6 (6 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.272× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW480 (line)]] | alt | 81.4 | 0 | 6 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.313× (z -11.9) ⚠ toxic; transcription drop · without an alert: [[Auranofin (drug)]] 5 µM 0.348× (z -11.7) |
| [[A-172 (line)]] | wt | 75.6 | 0 | 5 (2 ⚠) | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.303× (z -11.1) |
| [[HT-29 (line)]] | alt | 150 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.203× (z -15.0) ⚠ unreliable plate only · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.369× (z -12.3) |
| [[LS 180 (line)]] | wt | 130 | 0 | 5 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.225× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.372× (z -11.9) |
| [[SNU-423 (line)]] | alt | 59.6 | 0 | 5 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.408× (z -9.8) |
| [[SW 900 (line)]] | alt | 131 | 0 | 5 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.215× (z -16.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[KATO III (line)]] | alt | 142 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.129× (z -16.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 104 | 0 | 4 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.179× (z -15.8) ⚠ unreliable plate only |
| [[SW1417 (line)]] | alt | 84.7 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.222× (z -14.9) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.461× (z -11.0) |
| [[A-427 (line)]] | wt | 47.6 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.211× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.382× (z -8.6) |
| [[COLO 205 (line)]] | alt | 210 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.364× (z -12.4) |
| [[Hs 766T (line)]] | wt | 155 | 0 | 3 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.203× (z -14.6) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.371× (z -9.1) |
| [[LoVo (line)]] | wt | 113 | 0 | 3 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.407× (z -13.1) |
| [[NCI-H1573 (line)]] | alt | 134 | 0 | 3 (3 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -16.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[HCT15 (line)]] | alt | 122 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.256× (z -10.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[HEC-1-A (line)]] | alt | 94.7 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.304× (z -11.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[MIA PaCa-2 (line)]] | alt | 72.9 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.187× (z -14.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change · without an alert: [[Auranofin (drug)]] 5 µM 0.336× (z -9.6) |
| [[NCI-H23 (line)]] | alt | 91.7 | 0 | 2 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.360× (z -9.8) ⚠ unreliable plate only · without an alert: [[Auranofin (drug)]] 5 µM 0.411× (z -8.5) |
| [[SNU-1 (line)]] | wt | 42.0 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.233× (z -9.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.318× (z -8.8) |
| [[C32 (line)]] | wt | 38.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.286× (z -8.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[CHP-212 (line)]] | wt | 95.7 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.231× (z -10.4) |
| [[HOP62 (line)]] | alt | 61.8 | 0 | 1 | — | [[Auranofin (drug)]] 5 µM 0.341× (z -9.5) |
| [[hTERT-HPNE (line)]] | wt | 48.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.153× (z -9.7) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 91.8 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.563× (z -9.3) |
| [[PANC-1 (line)]] | alt | 64.5 | 0 | 1 (1 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.380× (z -11.0) ⚠ unreliable plate only |
| [[RPMI-7951 (line)]] | alt | 83.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.259× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SK-MEL-2 (line)]] | alt | 49.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.109× (z -16.5) ⚠ toxic; transcription drop; cell-cycle shift, explains ~38% of this change |
| [[SW48 (line)]] | wt | 57.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.115× (z -12.7) ⚠ toxic; transcription drop |
| [[AN3 CA (line)]] | alt | 25.9 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 21.5 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 50.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 38.1 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 58.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 31.9 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 109 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 84.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 38.7 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 51.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 81.3 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 93.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 58.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6748), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EAF2]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[SEC22A]] | +0.73 | +0.69 / +0.68 | both halves | 7e-06 |  |
| [[ACBD3]] | +0.73 | +0.75 / +0.65 | both halves | 7e-06 |  |
| [[TBC1D23]] | +0.73 | +0.75 / +0.63 | both halves | 7e-06 |  |
| [[CIR1]] | +0.71 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[AFTPH]] | +0.71 | +0.66 / +0.69 | both halves | 7e-06 |  |
| [[FBXO16]] | +0.70 | +0.58 / +0.65 | both halves | 7e-06 |  |
| [[ZNHIT3]] | +0.69 | +0.61 / +0.65 | both halves | 7e-06 |  |
| [[SRP54]] | +0.68 | +0.76 / +0.57 | both halves | 9e-06 |  |
| [[MRPL43]] | +0.68 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[SSR2]] | +0.68 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[TMF1]] | +0.68 | +0.71 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP4]] | -0.66 | -0.60 / -0.59 | both halves | 7e-06 |  |
| [[PRRC2B]] | -0.66 | -0.64 / -0.61 | both halves | 7e-06 |  |
| [[PSME3]] | -0.65 | -0.61 / -0.63 | both halves | 7e-06 |  |
| [[SEPTIN11]] | -0.64 | -0.58 / -0.60 | both halves | 7e-06 |  |
| [[NUP188]] | -0.63 | -0.61 / -0.62 | both halves | 7e-06 |  |
| [[MAPRE1]] | -0.62 | -0.55 / -0.59 | both halves | 1e-05 |  |
| [[KPNA4]] | -0.62 | -0.58 / -0.66 | both halves | 8e-06 |  |
| [[HNRNPAB]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[EIF4G1]] | -0.61 | -0.53 / -0.64 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 5, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGR2]] | B | AGR2 activity raises GOLPH3L's level | lines that do not express AGR2 (32) vs lines expressing it (18) | 1.70× lower at baseline in the lines without AGR2 | 0.008 | ⚠ within organs, on part of the lines; also absent: FXYD3, SERPINB5, PRKCH-AS1 |
| [[MPZL3]] | B | MPZL3 activity raises GOLPH3L's level | lines that do not express MPZL3 (25) vs lines expressing it (25) | 1.67× lower at baseline in the lines without MPZL3 | 0.030 | ⚠ within organs, on part of the lines; also absent: RNF39, MYO5B, CDH1 |
| [[ICA1]] | B | ICA1 activity raises GOLPH3L's level | lines that do not express ICA1 (20) vs lines expressing it (30) | 1.66× lower at baseline in the lines without ICA1 | 0.042 | ⚠ within organs, on part of the lines; also absent: SLC27A2, ENSG00000229970, ENSG00000288656 |
| [[TOP2A]] | B | TOP2A activity raises GOLPH3L's level | compounds that target TOP2A: 4 of 5 lower it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 7.8% of all compounds | 0.071 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[MCTP2]] | B | MCTP2 activity raises GOLPH3L's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.58× lower at baseline in the lines without MCTP2 | 0.075 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[ACBD3]] | C | ACBD3's natural level strengthens GOLPH3L's drug response | ACBD3's natural level across 48 lines (lineage-adjusted; a glimpse) | r +0.62, reverse +0.17; direction not clear | 0.098 | ⚠ tissue can mimic it; precision caveat; direction unclear |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 041]] — Intra-Golgi and retrograde Golgi-to-ER traffic; 111 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.31).
- **Nodal map** (x, y) = (10.4, -35.4); signed map (-49.3, 13.4). **Vector** length 149, 52.0% of its response variance represented; |z| ≥ 3 in 1,287 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Intra-Golgi and retrograde Golgi-to-ER traffic* (reactome, mean cos +0.51 to 12); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.51 to 8); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.51 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.4 | +2.4 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +5.1 | +3.1 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | +4.6 | +1.6 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +4.6 | +3.7 |
|  | [[Terfenadine (drug)]] 5 µM |  | +4.3 | +4.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +3.8 | +2.4 |
|  | [[Ponatinib (drug)]] 5 µM |  | +3.6 | +3.3 |
|  | [[GSK1059615 (drug)]] 0.5 µM |  | +3.6 | +2.3 |
| fall | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | -8.0 | -11.7 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.7 | -14.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -6.0 | -12.8 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -5.7 | -8.4 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.4 | -9.4 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.2 | -6.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | -4.9 | -4.1 |
|  | [[Auranofin (drug)]] 5 µM |  | -4.8 | -9.4 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | -4.6 | -4.1 |
|  | [[EX229 (drug)]] 5 µM |  | -4.3 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | golgi phosphoprotein 3 like |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q21.3 — chr1:150,646,230-150,697,154 (-) |
| Ensembl biotype | protein_coding |
| Also known as | GPP34R |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9H4A5](https://www.uniprot.org/uniprotkb/Q9H4A5) (Golgi phosphoprotein 3-like):

> Phosphatidylinositol-4-phosphate-binding protein that may antagonize the action of GOLPH3 which is required for the process of vesicle budding at the Golgi and anterograde transport to the plasma membrane.

**Summary**, from NCBI Gene [55204](https://www.ncbi.nlm.nih.gov/gene/55204):

> The Golgi complex plays a key role in the sorting and modification of proteins exported from the endoplasmic reticulum. The protein encoded by this gene is localized at the Golgi stack and may have a regulatory role in Golgi trafficking. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24882](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24882) · Entrez [55204](https://www.ncbi.nlm.nih.gov/gene/55204) · UniProt [Q9H4A5](https://www.uniprot.org/uniprotkb/Q9H4A5) · Ensembl [ENSG00000143457](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000143457)

## Data

Gene col 6748: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6748); `tables/drug_effects.parquet` (56 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6748, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6748]; `tensor/DDL_lfc|DDL_z.npy` [6748]; `embed/gene_vectors.npy` [6748]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6748 or target_col == 6748). Every well: [[GOLPH3L — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOLPH3L.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
