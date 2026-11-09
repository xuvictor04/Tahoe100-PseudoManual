---
symbol: "SLC38A4-AS1"
type: "gene"
col: 15028
ensembl_id: "ENSG00000257261"
name: "SLC38A4 antisense RNA 1"
location: "12q13.11"
module: 10
arm: "+"
pooled_cpm: 175.81
n_lines_expressing: 49
n_dd_up: 0
n_dd_down: 38
n_dd_up_clean: 0
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/010"]
generated_by: "tahoemap"
---

# SLC38A4-AS1

*SLC38A4 antisense RNA 1* — 12q13.11

## At a glance

> [!summary] In this data
> No drug-dose raises it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 1.69×, HOP62 1.58×; ⚠ position not correctable); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 2.63×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 2.06×; ⚠ cell-cycle shift, explains ~97% of this change); [[Auranofin (drug)]] 5 µM in 1 line (AN3 CA 6.75×); [[Binimetinib (drug)]] 0.05 µM in 1 line (SW480 2.12×).
> Pooled over the cell lines (median), lowered significantly by 38 drug-doses (21 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 5 µM: 0.215× (z -14.8, q 0e+00, down in 46 of 47 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change. The strongest without an alert is [[Ixazomib citrate (drug)]] 5 µM: 0.297× (z -11.7, q 2e-29, down in 47 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LEKR1]] (+0.71, fdr 7e-06), [[SGO1-AS1]] (+0.70, fdr 7e-06), [[TMEM232]] (+0.66, fdr 1e-05); moves opposite to [[PRR5]] (-0.62, fdr 4e-05), [[ZNRF1]] (-0.58, fdr 3e-05), [[PDPR2P]] (-0.57, fdr 4e-05).
> It sits in the **+** arm of [[Module 010]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[AGA-DT]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, none with an alert. 0 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 15028.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 5 shown; `tables/drug_line_top.parquet`), these raise it: [[Adagrasib (drug)]] 0.05 µM in 2 lines (NCI-H23 1.69×, HOP62 1.58×; ⚠ position not correctable); [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM in 1 line (SNU-1 2.63×); [[Homoharringtonine (drug)]] 5 µM in 1 line (A-427 2.06×; ⚠ cell-cycle shift, explains ~97% of this change); [[Auranofin (drug)]] 5 µM in 1 line (AN3 CA 6.75×); [[Binimetinib (drug)]] 0.05 µM in 1 line (SW480 2.12×).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Cobimetinib (drug)]] 5 µM |  | 1.45× | +3.4 | 0.22 | 28/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Cobimetinib (drug)]] 0.5 µM |  | 1.46× | +3.3 | 0.22 | 27/46 (SW480, NCI-H23, …) | rises with dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | 1.27× | +3.3 | 0.22 | 22/47 (SNU-1, AsPC-1, …) | top dose only |  |
| [[Demeclocycline (drug)]] 5 µM |  | 1.25× | +3.1 | 0.23 | 27/47 (H4, BT-474, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | 1.38× | +3.1 | 0.23 | 27/47 (NCI-H23, KATO III, …) | two highest doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 38 in all, 21 with an alert ⚠; shown: the 15 strongest and the 11 next strongest without an alert. 38 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 21 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 15028.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | **0.215×** | -14.8 | 0e+00 | 46/47 (LS 180, NCI-H1573, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.243×** | -13.7 | 5e-40 | 45/47 (COLO 205, SW480, …) | all doses, stronger at high dose | composition shift |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.297×** | -11.7 | 2e-29 | 47/47 (HCT15, PANC-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.295×** | -11.3 | 1e-27 | 43/46 (COLO 205, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~27% of this change | **0.336×** | -10.5 | 8e-24 | 44/47 (SW480, LoVo, …) | rises with dose |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **0.367×** | -9.7 | 4e-20 | 46/47 (H4, SW480, …) | all doses, stronger at high dose |  |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.370×** | -9.6 | 6e-20 | 44/47 (COLO 205, LoVo, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~35% of this change | **0.372×** | -9.6 | 9e-20 | 44/47 (LoVo, NCI-H1573, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.379×** | -9.4 | 5e-19 | 45/47 (KATO III, LoVo, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | **0.391×** | -8.7 | 2e-16 | 38/47 (NCI-H1792, A549, …) | rises with dose | composition shift |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **0.406×** | -8.7 | 2e-16 | 42/47 (LoVo, COLO 205, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~31% of this change | **0.392×** | -8.7 | 2e-16 | 38/46 (LoVo, COLO 205, …) | rises with dose |  |
| [[PH-797804 (drug)]] 5 µM |  | **0.185×** | -8.5 | 6e-16 | 42/47 (COLO 205, Panc 03.27, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[TAK-901 (drug)]] 5 µM |  | **0.189×** | -8.4 | 2e-15 | 46/48 (HT-29, KATO III, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~17% here); composition shift; noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **0.446×** | -7.8 | 3e-13 | 43/47 (HT-29, NCI-H1792, …) | inconsistent across doses |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.440×** | -7.5 | 3e-12 | 46/47 (HT-29, HepG2/C3A, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **0.528×** | -5.5 | 1e-06 | 37/47 (MIA PaCa-2, COLO 205, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Abemaciclib (drug)]] 5 µM |  | **0.412×** | -4.5 | 2e-04 | 39/47 (HT-29, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **0.469×** | -3.8 | 0.003 | 31/47 (MIA PaCa-2, NCI-H460, …) | top dose only | noisy plate (z scaled) |
| [[Mebendazole (drug)]] 5 µM |  | **0.663×** | -3.8 | 0.003 | 32/47 (NCI-H23, NCI-H460, …) | rises with dose |  |
| [[EX229 (drug)]] 5 µM |  | **0.489×** | -3.6 | 0.006 | 30/47 (BT-474, HT-29, …) | all doses, stronger at high dose | noisy plate (z scaled) |
| [[Abemaciclib (drug)]] 0.5 µM |  | **0.599×** | -3.5 | 0.008 | 34/47 (NCI-H460, SNU-1, …) | rises with dose | noisy plate (z scaled) |
| [[Pasireotide (acetate) (drug)]] 5 µM |  | **0.773×** | -3.5 | 0.008 | 36/48 (SW 1271, Panc 03.27, …) | rises with dose | position effect removed |
| [[Vilanterol (drug)]] 5 µM |  | **0.774×** | -3.5 | 0.008 | 30/48 (C32, SNU-423, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **0.787×** | -3.3 | 0.018 | 27/48 (CFPAC-1, NCI-H23, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.5 µM |  | **0.637×** | -3.1 | 0.031 | 31/48 (LoVo, HCT15, …) | all doses, flat | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.54 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 15028. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[KATO III (line)]] | alt | 220 | 0 | 17 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.101× (z -19.1) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.174× (z -14.6) |
| [[NCI-H1573 (line)]] | alt | 361 | 0 | 16 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0702× (z -20.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -12.5) |
| [[COLO 205 (line)]] | alt | 386 | 0 | 15 (12 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.102× (z -20.5) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0298× (z -16.5) |
| [[LOX-IMVI (line)]] | wt | 202 | 0 | 15 (12 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.119× (z -14.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.230× (z -9.1) |
| [[HT-29 (line)]] | alt | 295 | 0 | 14 (10 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.195× (z -18.7) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.185× (z -13.7) |
| [[LS 180 (line)]] | wt | 210 | 0 | 14 (10 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0526× (z -22.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.206× (z -11.8) |
| [[LoVo (line)]] | wt | 179 | 0 | 13 (11 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.118× (z -18.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.204× (z -14.0) |
| [[SW480 (line)]] | alt | 148 | 2 | 11 (8 ⚠) | [[Binimetinib (drug)]] 0.05 µM 2.12× (z +8.6) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.105× (z -20.3) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.287× (z -11.2) |
| [[A549 (line)]] | wt | 199 | 0 | 12 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.106× (z -19.6) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.104× (z -14.0) |
| [[HEC-1-A (line)]] | alt | 420 | 0 | 12 (8 ⚠) | — | [[Panobinostat (drug)]] 0.5 µM 0.215× (z -13.3) ⚠ cell-cycle shift, explains ~35% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.292× (z -10.7) |
| [[HCT15 (line)]] | alt | 208 | 0 | 11 (8 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.0832× (z -16.5) |
| [[HepG2_C3A (line)]] | wt | 302 | 0 | 11 (8 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.107× (z -15.6) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.137× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 176 | 0 | 10 (10 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.118× (z -14.4) ⚠ cell-cycle shift, explains ~38% of this change |
| [[H4 (line)]] | wt | 115 | 0 | 9 (8 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.165× (z -15.3) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.124× (z -12.5) |
| [[NCI-H23 (line)]] | alt | 190 | 1 (1 ⚠) | 8 (7 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.69× (z +14.2) ⚠ position not correctable | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.125× (z -16.2) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Peretinoin (drug)]] 0.5 µM 0.284× (z -8.7) |
| [[CFPAC-1 (line)]] | alt | 164 | 0 | 8 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.216× (z -16.4) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.274× (z -9.8) |
| [[Panc 03.27 (line)]] | alt | 212 | 0 | 8 (6 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.150× (z -13.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[PH-797804 (drug)]] 5 µM 0.0428× (z -12.0) |
| [[PANC-1 (line)]] | alt | 110 | 0 | 7 (5 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.132× (z -16.8) ⚠ cell-cycle shift, explains ~28% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.162× (z -15.1) |
| [[SW 900 (line)]] | alt | 215 | 0 | 7 (7 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0790× (z -15.5) ⚠ toxic |
| [[A498 (line)]] | wt | 147 | 0 | 6 (5 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.171× (z -14.6) ⚠ cell-cycle shift, explains ~97% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.173× (z -10.2) |
| [[BT-474 (line)]] | alt | 205 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.135× (z -16.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.209× (z -12.3) |
| [[RKO (line)]] | wt | 115 | 0 | 6 (5 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.197× (z -11.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.302× (z -8.7) |
| [[RPMI-7951 (line)]] | alt | 77.0 | 0 | 6 (5 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.150× (z -11.4) ⚠ cell-cycle shift, explains ~38% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.237× (z -9.0) |
| [[SK-MEL-2 (line)]] | alt | 112 | 0 | 6 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.226× (z -11.2) ⚠ cell-cycle shift, explains ~40% of this change |
| [[SNU-1 (line)]] | wt | 132 | 1 | 5 (4 ⚠) | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 2.63× (z +10.0) | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.255× (z -10.0) ⚠ unreliable plate only · without an alert: [[PH-797804 (drug)]] 5 µM 0.0919× (z -9.1) |
| [[SW1417 (line)]] | alt | 112 | 0 | 6 (6 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.213× (z -15.8) ⚠ cell-cycle shift, explains ~97% of this change |
| [[A-427 (line)]] | wt | 396 | 1 (1 ⚠) | 4 (3 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.06× (z +9.4) ⚠ cell-cycle shift, explains ~97% of this change | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.233× (z -12.7) ⚠ cell-cycle shift, would explain all of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.365× (z -9.1) |
| [[HOP62 (line)]] | alt | 143 | 1 (1 ⚠) | 4 (4 ⚠) | [[Adagrasib (drug)]] 0.05 µM 1.58× (z +9.0) ⚠ position not correctable | [[Digitoxin (drug)]] 5 µM 0.146× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[MIA PaCa-2 (line)]] | alt | 378 | 0 | 5 (4 ⚠) | — | [[c-Kit-IN-1 (drug)]] 0.05 µM 0.208× (z -10.5) ⚠ unreliable plate only · without an alert: [[Topotecan (hydrochloride) (drug)]] 0.5 µM 0.215× (z -9.1) |
| [[NCI-H460 (line)]] | wt | 117 | 0 | 5 (4 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.147× (z -13.3) |
| [[A-172 (line)]] | wt | 152 | 0 | 4 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.220× (z -10.0) |
| [[SW 1271 (line)]] | alt | 466 | 0 | 4 (4 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.0880× (z -12.4) ⚠ cell-cycle shift, explains ~28% of this change |
| [[J82 (line)]] | alt | 77.8 | 0 | 3 (2 ⚠) | — | [[Ixazomib citrate (drug)]] 5 µM 0.232× (z -10.2) |
| [[SNU-423 (line)]] | alt | 186 | 0 | 3 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.199× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.226× (z -10.2) |
| [[CHP-212 (line)]] | wt | 168 | 0 | 2 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.138× (z -10.7) ⚠ cell-cycle shift, explains ~28% of this change |
| [[AN3 CA (line)]] | alt | 138 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.75× (z +9.0) | — |
| [[Hs 766T (line)]] | wt | 78.0 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 5 µM 0.198× (z -10.4) |
| [[HS-578T (line)]] | alt | 64.7 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.239× (z -8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[hTERT-HPNE (line)]] | wt | 95.8 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.201× (z -9.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2030 (line)]] | alt | 150 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.196× (z -10.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change |
| [[NCI-H2347 (line)]] | alt | 141 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.373× (z -9.8) ⚠ cell-cycle shift, explains ~97% of this change |
| [[NCI-H596 (line)]] | alt | 158 | 0 | 1 | — | [[Atazanavir (sulfate) (drug)]] 5 µM 0.0705× (z -12.4) |
| [[SW48 (line)]] | wt | 80.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 0.5 µM 0.172× (z -8.9) ⚠ cell-cycle shift, explains ~27% of this change |
| [[AsPC-1 (line)]] | alt | 71.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 90.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 76.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 138 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 177 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 42.9 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 85.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 15028), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*87 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LEKR1]] | +0.71 | +0.68 / +0.63 | both halves | 7e-06 |  |
| [[SGO1-AS1]] | +0.70 | +0.70 / +0.63 | both halves | 7e-06 | same gene group |
| [[TMEM232]] | +0.66 | +0.66 / +0.57 | both halves | 1e-05 |  |
| [[UFL1-AS1]] | +0.66 | +0.66 / +0.53 | both halves | 1e-05 | same gene group |
| [[PDCL3P4]] | +0.66 | +0.65 / +0.59 | both halves | 7e-06 |  |
| [[PKN2-AS1]] | +0.65 | +0.67 / +0.64 | both halves | 7e-06 | same gene group |
| [[ZRANB2-DT]] | +0.65 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[FSIP2-AS1]] | +0.65 | +0.64 / +0.56 | both halves | 1e-05 | same gene group |
| [[AK9]] | +0.63 | +0.64 / +0.48 | both halves | 2e-05 |  |
| [[EIF1B-AS1]] | +0.63 | +0.64 / +0.46 | both halves | 3e-05 |  |
| [[DAB1]] | +0.63 | +0.56 / +0.52 | both halves | 1e-05 |  |
| [[LINC01252]] | +0.63 | +0.53 / +0.62 | both halves | 1e-05 |  |

## Genes that move opposite

*13 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PRR5]] | -0.62 | -0.71 / -0.42 | both halves | 4e-05 |  |
| [[ZNRF1]] | -0.58 | -0.56 / -0.45 | both halves | 3e-05 |  |
| [[PDPR2P]] | -0.57 | -0.57 / -0.41 | both halves | 4e-05 |  |
| [[TAF5L]] | -0.57 | -0.62 / -0.41 | both halves | 4e-05 |  |
| [[GFOD2]] | -0.56 | -0.48 / -0.48 | both halves | 2e-05 |  |
| [[NBPF3]] | -0.56 | -0.59 / -0.39 | both halves | 5e-05 |  |
| [[LCMT1]] | -0.55 | -0.54 / -0.39 | both halves | 6e-05 |  |
| [[IQCB1]] | -0.55 | -0.54 / -0.46 | both halves | 2e-05 |  |
| [[HERC2P9]] | -0.54 | -0.50 / -0.46 | both halves | 2e-05 |  |
| [[TOMM5]] | -0.54 | -0.55 / -0.39 | both halves | 5e-05 |  |
| [[PI4KAP2]] | -0.54 | -0.39 / -0.52 | both halves | 6e-05 |  |
| [[TPST2]] | -0.53 | -0.61 / -0.28 | both halves | 3e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[AGA-DT]] | B | AGA-DT activity raises SLC38A4-AS1's level | lines that do not express AGA-DT (6) vs lines expressing it (44) | 1.97× lower at baseline in the lines without AGA-DT | 0.079 | ⚠ within organs, on part of the lines; also absent: RUNDC3A-AS1, UTRN, TMEM144; maybe low, not absent |
| [[SLCO1B1]] | B | SLCO1B1 activity raises SLC38A4-AS1's level | lines that do not express SLCO1B1 (28) vs lines expressing it (22) | 1.41× lower at baseline in the lines without SLCO1B1 | 0.088 | ⚠ within organs, on part of the lines; also absent: ENSG00000257062, SLCO1B3, SLCO1B3-SLCO1B7 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 010]]; 217 genes; this gene is in the **+** arm (projection on the module's main direction 0.615). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.32).
- **Nodal map** (x, y) = (9.4, 15.3); signed map (28.1, -10.5). **Vector** length 87.0, 37.8% of its response variance represented; |z| ≥ 3 in 1,802 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Auranofin (drug)]] 5 µM |  | +8.5 | +1.2 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~97% of this change | +6.0 | -5.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | +5.7 | -2.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +3.3 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | +4.3 | -8.7 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +3.2 | +1.3 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +2.1 | +1.9 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.9 | +1.4 |
| fall | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -7.2 | -11.3 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | -6.7 | -5.5 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -4.3 | -9.6 |
|  | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~41% of this change | -4.3 | -8.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -4.2 | -11.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | -2.8 | -3.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -2.8 | -2.5 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.4 | -2.3 |
|  | [[EX229 (drug)]] 5 µM |  | -2.2 | -3.6 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.1 | -8.5 |

## What is on record

|  |  |
|---|---|
| Name | SLC38A4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 12q13.11 — chr12:46,383,433-46,876,784 (+) |
| Ensembl biotype | lncRNA |
| Also known as | lncPCED1b |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:56178](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:56178) · Entrez [100288798](https://www.ncbi.nlm.nih.gov/gene/100288798) · Ensembl [ENSG00000257261](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000257261)

## Data

Gene col 15028: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 15028); `tables/drug_effects.parquet` (43 rows, flagged included); `relations/gene_relations.parquet` (col_a == 15028, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 15028]; `tensor/DDL_lfc|DDL_z.npy` [15028]; `embed/gene_vectors.npy` [15028]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 15028 or target_col == 15028). Every well: [[SLC38A4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SLC38A4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
