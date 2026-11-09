---
symbol: "GREB1"
type: "gene"
col: 12155
ensembl_id: "ENSG00000196208"
name: "growth regulating estrogen receptor binding 1"
location: "2p25.1"
module: 75
arm: "+"
pooled_cpm: 4.81
n_lines_expressing: 44
n_dd_up: 34
n_dd_down: 3
n_dd_up_clean: 24
n_dd_down_clean: 2
in_vector_space: true
direction_upstream: 3
direction_downstream: 4
tags: ["gene", "module/075"]
generated_by: "tahoemap"
---

# GREB1

*growth regulating estrogen receptor binding 1* — 2p25.1

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 34 drug-doses (10 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 6.46× (z +32.8, q 0e+00, up in 32 of 34 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (1 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.617× (z -6.0, q 1e-06, down in 16 of 37 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0610×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H23 0.0602×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.108×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0648×).
> Its strongest partners by |cos| (97 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 3 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GALNTL6]] (+0.70, fdr 7e-06), [[ARL14EP-DT]] (+0.68, fdr 7e-06), [[LINC02006]] (+0.67, fdr 7e-06); moves opposite to [[STUB1]] (-0.57, fdr 0.002, ⚠ not reproduced).
> It is in [[Module 075]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 4 go from it, the strongest it → [[PSMD14-DT]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 34 in all, 10 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 34 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 10 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12155.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **6.46×** | +32.8 | 0e+00 | 32/34 (PANC-1, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~3% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **5.74×** | +21.7 | 0e+00 | 17/20 (SW480, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **4.94×** | +19.1 | 0e+00 | 4/5 (HOP62, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **4.56×** | +17.5 | 0e+00 | 5/8 (PANC-1, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.09×** | +13.0 | 1e-36 | 17/33 (NCI-H460, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.85×** | +10.8 | 4e-25 | 19/41 (HOP62, A498, …) | all doses, stronger at high dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~25% of this change | **1.82×** | +10.5 | 6e-24 | 17/39 (A549, HOP62, …) | inconsistent across doses | low cells (technical?) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **2.19×** | +9.4 | 4e-19 | 15/30 (A498, HEC-1-A, …) | top dose only | cell-cycle shift (explains ~10% here) |
| [[Auranofin (drug)]] 5 µM |  | **1.91×** | +8.1 | 5e-14 | 14/35 (MIA PaCa-2, NCI-H23, …) | top dose only |  |
| [[Tucidinostat (drug)]] 5 µM |  | **1.55×** | +7.7 | 8e-13 | 15/40 (KATO III, SNU-423, …) | all doses, stronger at high dose |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.81×** | +7.1 | 5e-11 | 17/34 (A498, HEC-1-A, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | **1.83×** | +7.0 | 1e-10 | 15/38 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~18% here) |
| [[Panobinostat (drug)]] 5 µM |  | **1.74×** | +6.9 | 2e-10 | 10/40 (PANC-1, SW1417, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.63×** | +5.7 | 6e-07 | 6/35 (KATO III, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.60×** | +5.4 | 2e-06 | 6/30 (LoVo, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **1.48×** | +4.8 | 4e-05 | 8/36 (H4, LoVo, …) | all doses, stronger at high dose |  |
| [[Triamcinolone (drug)]] 5 µM |  | **1.31×** | +4.7 | 7e-05 | 7/40 (BT-474, SHP-77, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **1.24×** | +3.8 | 0.004 | 7/40 (A549, A-172, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.33×** | +3.6 | 0.010 | 3/38 (CHP-212, HT-29, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12155.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 6 here, 2 with an alert ⚠; the 4 shown; `tables/drug_line_top.parquet`), these lower it: [[Digitoxin (drug)]] 0.5 µM in 1 line (NCI-H460 0.0610×); [[Pitavastatin (Calcium) (drug)]] 5 µM in 1 line (NCI-H23 0.0602×); [[Niclosamide (olamine) (drug)]] 5 µM in 1 line (A-427 0.108×; ⚠ toxic; cell-cycle shift, explains ~0% of this change); [[Vinblastine (sulfate) (drug)]] 0.5 µM in 1 line (NCI-H460 0.0648×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.617×** | -6.0 | 1e-06 | 16/37 (NCI-H460, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~16% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~44% of this change | **0.738×** | -3.8 | 0.044 | 13/40 (C-33 A, SW480, …) | inconsistent across doses | composition shift |
| [[Peretinoin (drug)]] 5 µM |  | **0.741×** | -3.6 | 0.065 | 8/37 (SW 900, CFPAC-1, …) | top dose only |  |
| [[Abemaciclib (drug)]] 5 µM |  | 0.608× | -3.2 | 0.13 | 3/35 (SW 900, hTERT-HPNE, …) | top dose only | noisy plate (z scaled) |
| [[Pitavastatin (Calcium) (drug)]] 5 µM |  | 0.763× | -3.2 | 0.13 | 8/33 (NCI-H23, NCI-H1792, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Mebendazole (drug)]] 5 µM |  | 0.765× | -3.2 | 0.13 | 4/39 (LOX-IMVI, hTERT-HPNE, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~36% of this change | 0.780× | -3.1 | 0.17 | 6/40 (SNU-423, NCI-H460, …) | inconsistent across doses |  |
| [[Daptomycin (drug)]] 5 µM | ⚠ unreliable plate only | 0.785× | -3.0 | 0.19 | 6/39 (H4, HepG2/C3A, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.21 per unit of S-phase module lfc, -0.42 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12155. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 3.48 | 1 | 2 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.56× (z +9.0) | [[Digitoxin (drug)]] 0.5 µM 0.0610× (z -11.7) |
| [[A-427 (line)]] | wt | 13.6 | 0 | 2 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.108× (z -10.8) ⚠ toxic; cell-cycle shift, explains ~0% of this change · without an alert: [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.134× (z -9.8) |
| [[SW480 (line)]] | alt | 3.44 | 2 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 18.9× (z +12.6) ⚠ toxic; transcription drop · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.95× (z +9.7) | — |
| [[HEC-1-A (line)]] | alt | 3.25 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 25.8× (z +11.1) ⚠ toxic; transcription drop | — |
| [[KATO III (line)]] | alt | 2.96 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 8.93× (z +9.1) | — |
| [[LOX-IMVI (line)]] | wt | 2.74 | 0 | 1 (1 ⚠) | — | [[Daptomycin (drug)]] 0.5 µM 0.0625× (z -8.6) ⚠ unreliable plate only |
| [[NCI-H1573 (line)]] | alt | 2.12 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 14.3× (z +10.2) | — |
| [[NCI-H2030 (line)]] | alt | 3.13 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 7.21× (z +9.1) | — |
| [[NCI-H23 (line)]] | alt | 8.10 | 0 | 1 | — | [[Pitavastatin (Calcium) (drug)]] 5 µM 0.0602× (z -11.7) |
| [[PANC-1 (line)]] | alt | 1.76 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 10.5× (z +10.8) | — |
| [[A-172 (line)]] | wt | 2.85 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.95 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 5.45 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 2.42 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 0.789 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 55.5 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.75 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 1.41 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.1 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 9.62 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 1.73 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 22.3 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 3.32 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 0.880 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.44 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 1.48 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 4.51 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 1.08 n.m. | — | — | — | — |
| [[LoVo (line)]] | wt | 1.58 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 1.49 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.34 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.13 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 5.32 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 1.07 n.m. | — | — | — | — |
| [[NCI-H596 (line)]] | alt | 8.19 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 6.76 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 0.890 n.m. | — | — | — | — |
| [[RKO (line)]] | wt | 2.57 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.70 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 4.05 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 2.10 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.68 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 4.03 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 2.64 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 2.16 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 1.32 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.66 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12155), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 2 of them with an alert (⚠; 2 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GALNTL6]] | +0.70 | +0.61 / +0.66 | both halves | 7e-06 |  |
| [[ARL14EP-DT]] | +0.68 | +0.63 / +0.63 | both halves | 7e-06 |  |
| [[LINC02006]] | +0.67 | +0.61 / +0.59 | both halves | 7e-06 |  |
| [[EYS]] | +0.67 | +0.55 / +0.55 | both halves | 1e-05 |  |
| [[C2orf88]] | +0.66 | +0.45 / +0.54 | both halves | 3e-05 |  |
| [[ZNF423]] | +0.65 | +0.55 / +0.68 | both halves | 1e-05 |  |
| [[ACTA2]] | +0.65 | +0.61 / +0.40 | both halves | 5e-05 |  |
| [[LHFPL3]] | +0.65 | +0.51 / +0.48 | both halves | 2e-05 |  |
| [[EFCAB5]] | +0.64 | +0.59 / +0.45 | both halves | 3e-05 |  |
| [[CCDC26]] | +0.64 | +0.48 / +0.58 | both halves | 2e-05 |  |
| [[THSD7B]] | +0.64 | +0.54 / +0.58 | both halves | 1e-05 |  |
| [[MYO16]] | +0.64 | +0.60 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 1 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[STUB1]] | -0.57 | -0.42 / -0.13 | ⚠ not reproduced | 0.002 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers GREB1's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 7.3% of all compounds | 0.010 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[PURPL]] | B | PURPL activity raises GREB1's level | lines that do not express PURPL (25) vs lines expressing it (25) | 1.77× lower at baseline in the lines without PURPL | 0.046 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: MIR99AHG, ENSG00000286385, RPS4Y1 |
| [[ABCA12]] | B | ABCA12 activity raises GREB1's level | lines that do not express ABCA12 (10) vs lines expressing it (40) | 1.07× lower at baseline in the lines without ABCA12 | 0.069 | ⚠ within organs, on part of the lines; also absent: ENSG00000226640, ZPLD1, ANKRD7; maybe low, not absent |

### Downstream of this gene

*4 arrows, 4 of them with an alert ⚠; grade A 0, B 4, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[PSMD14-DT]] | B | GREB1 activity raises PSMD14-DT's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 1.28× lower at baseline in the lines without GREB1 | 0.024 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |
| [[TYMSOS]] | B | GREB1 activity raises TYMSOS's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 2.10× lower at baseline in the lines without GREB1 | 0.032 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |
| [[PPP1R9A-AS1]] | B | GREB1 activity raises PPP1R9A-AS1's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 1.24× lower at baseline in the lines without GREB1 | 0.036 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |
| [[C2orf49-DT]] | B | GREB1 activity raises C2orf49-DT's level | lines that do not express GREB1 (6) vs lines expressing it (44) | 1.41× lower at baseline in the lines without GREB1 | 0.088 | ⚠ within organs, on part of the lines; also absent: PRKN, SLC17A7, ENSG00000232855; maybe low, not absent |

## Where it sits

- **Module**: [[Module 075]]; 60 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (18.8, 27.4); signed map (36.5, -1.3). **Vector** length 58.6, 9.22% of its response variance represented; |z| ≥ 3 in 913 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +9.1 | +32.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +8.0 | +19.1 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +7.9 | +21.7 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +7.5 | +17.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 0.5 µM |  | +4.8 | +7.0 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +4.4 | +10.8 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.3 | +8.1 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.2 | +7.7 |
|  | [[Amsacrine (drug)]] 5 µM |  | +1.8 | +3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.5 | +4.8 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -3.0 | -1.2 |
|  | [[Belinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.3 | -2.2 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.0 | +2.7 |
|  | [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.6 | -2.4 |
|  | [[Digitoxin (drug)]] 0.5 µM |  | -1.6 | -6.0 |
|  | [[Artesunate (drug)]] 0.5 µM |  | -1.5 | -0.9 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.5 | -0.5 |
|  | [[Mebendazole (drug)]] 5 µM |  | -1.2 | -3.2 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.2 | +0.1 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.1 | +0.3 |

## What is on record

|  |  |
|---|---|
| Name | growth regulating estrogen receptor binding 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 2p25.1 — chr2:11,482,341-11,642,788 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0575 |
| Hallmark sets | ESTROGEN_RESPONSE_EARLY |
| Reactome | 3 pathways, smallest: Estrogen-dependent gene expression; ESR-mediated signaling; Signaling by Nuclear Receptors |
| Matched by | ensembl_id |

**Function**, from UniProt [Q4ZG55](https://www.uniprot.org/uniprotkb/Q4ZG55) (Protein GREB1):

> May play a role in estrogen-stimulated cell proliferation. Acts as a regulator of hormone-dependent cancer growth in breast and prostate cancers.

**Summary**, from NCBI Gene [9687](https://www.ncbi.nlm.nih.gov/gene/9687):

> This gene is an estrogen-responsive gene that is an early response gene in the estrogen receptor-regulated pathway. It is thought to play an important role in hormone-responsive tissues and cancer. Three alternatively spliced transcript variants encoding distinct isoforms have been found for this gene. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:24885](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24885) · Entrez [9687](https://www.ncbi.nlm.nih.gov/gene/9687) · UniProt [Q4ZG55](https://www.uniprot.org/uniprotkb/Q4ZG55) · Ensembl [ENSG00000196208](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000196208)

## Data

Gene col 12155: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12155); `tables/drug_effects.parquet` (42 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12155, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12155]; `tensor/DDL_lfc|DDL_z.npy` [12155]; `embed/gene_vectors.npy` [12155]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12155 or target_col == 12155). Every well: [[GREB1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GREB1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
