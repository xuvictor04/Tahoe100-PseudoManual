---
symbol: "AP3B2"
type: "gene"
col: 2393
ensembl_id: "ENSG00000103723"
name: "adaptor related protein complex 3 subunit beta 2"
location: "15q25.2"
module: 165
arm: "+"
pooled_cpm: 8.0
n_lines_expressing: 35
n_dd_up: 43
n_dd_down: 0
n_dd_up_clean: 31
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 3
direction_downstream: 5
tags: ["gene", "module/165"]
generated_by: "tahoemap"
---

# AP3B2

*adaptor related protein complex 3 subunit beta 2* — 15q25.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 43 drug-doses (12 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 18.4× (z +44.9, q 0e+00, up in 26 of 27 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0578×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0756×); [[Hesperidin (drug)]] 5 µM in 1 line (J82 0.0779×).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC35F1]] (+0.67, fdr 7e-06), [[DLGAP2]] (+0.65, fdr 7e-06), [[ANGPT2]] (+0.64, fdr 3e-05); moves opposite to [[ZFP14]] (-0.63, fdr 3e-05), [[RHOT1]] (-0.59, fdr 2e-05), [[EHMT2]] (-0.54, fdr 2e-04).
> It is in [[Module 165]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); 5 go from it, the strongest it → [[MTUS2]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 43 in all, 12 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 43 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 12 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 2393.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **18.4×** | +44.9 | 0e+00 | 26/27 (NCI-H2030, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **9.89×** | +35.3 | 0e+00 | 26/28 (SW480, PANC-1, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **9.36×** | +24.4 | 0e+00 | 25/26 (NCI-H460, C32, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **6.34×** | +20.1 | 0e+00 | 31/32 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **5.33×** | +18.2 | 0e+00 | 28/30 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~20% here) |
| [[Harringtonine (drug)]] 5 µM |  | **5.54×** | +17.9 | 0e+00 | 23/29 (NCI-H2347, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Tucidinostat (drug)]] 5 µM |  | **2.59×** | +14.6 | 0e+00 | 27/29 (SK-MEL-2, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **3.82×** | +14.0 | 6e-43 | 24/26 (NCI-H460, SW480, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **3.29×** | +13.0 | 1e-36 | 28/32 (PANC-1, A549, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **3.37×** | +12.7 | 2e-35 | 12/19 (NCI-H460, J82, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Auranofin (drug)]] 5 µM |  | **3.11×** | +12.3 | 3e-33 | 21/30 (LoVo, C32, …) | top dose only |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **2.95×** | +11.8 | 2e-30 | 10/16 (SW480, RPMI-7951, …) | all doses, stronger at high dose | composition shift |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **2.14×** | +11.7 | 7e-30 | 21/31 (A-172, BT-474, …) | top dose only |  |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | **3.01×** | +11.5 | 4e-29 | 5/10 (SW480, HOP62, …) | all doses, stronger at high dose | composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **2.77×** | +11.1 | 4e-27 | 22/30 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **2.79×** | +10.8 | 2e-25 | 20/26 (NCI-H460, BT-474, …) | top dose only | cell-cycle shift (explains ~22% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **2.32×** | +9.1 | 2e-18 | 25/32 (PANC-1, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here) |
| [[Tucidinostat (drug)]] 0.5 µM |  | **2.29×** | +9.0 | 6e-18 | 22/29 (SK-MEL-2, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.56×** | +6.8 | 3e-10 | 15/31 (J82, NCI-H2347, …) | all doses, stronger at high dose | low cells (technical?); cell-cycle shift (explains ~12% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, 1 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 2393.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, none with an alert; the 3 shown; `tables/drug_line_top.parquet`), these lower it: [[Ferulic acid (drug)]] 0.5 µM in 1 line (NCI-H2347 0.0578×); [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM in 1 line (PANC-1 0.0756×); [[Hesperidin (drug)]] 5 µM in 1 line (J82 0.0779×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Radotinib (drug)]] 5 µM |  | 0.799× | -3.5 | 0.12 | 8/30 (SW1417, SK-MEL-2, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.5 µM |  | 0.730× | -3.4 | 0.12 | 6/31 (SHP-77, NCI-H1573, …) | inconsistent across doses | position effect removed |
| [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 5 µM |  | 0.724× | -3.4 | 0.12 | 8/29 (A-172, NCI-H460, …) | top dose only |  |
| [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | 0.565× | -3.3 | 0.15 | 7/24 (NCI-H23, SHP-77, …) | top dose only | noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.70 per unit of S-phase module lfc, -0.41 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 2393. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 2.70 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 42.6× (z +18.5) | — |
| [[A498 (line)]] | wt | 3.54 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +17.1) | [[Pimozide (drug)]] 0.05 µM 0.0989× (z -9.5) |
| [[NCI-H2347 (line)]] | alt | 3.94 | 4 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.5× (z +15.2) | [[Ferulic acid (drug)]] 0.5 µM 0.0578× (z -10.2) |
| [[PANC-1 (line)]] | alt | 2.31 | 4 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 22.5× (z +16.2) | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0756× (z -9.6) |
| [[J82 (line)]] | alt | 5.93 | 3 | 1 | [[Homoharringtonine (drug)]] 5 µM 20.9× (z +16.7) | [[Hesperidin (drug)]] 5 µM 0.0779× (z -9.6) |
| [[NCI-H1573 (line)]] | alt | 3.16 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 47.6× (z +18.6) | — |
| [[NCI-H2030 (line)]] | alt | 12.7 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.7× (z +19.8) | — |
| [[SW480 (line)]] | alt | 9.99 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 8.93× (z +17.6) | — |
| [[A549 (line)]] | wt | 3.00 | 3 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 43.3× (z +15.1) | — |
| [[C32 (line)]] | wt | 5.21 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 45.3× (z +15.7) | — |
| [[HOP62 (line)]] | alt | 4.00 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 57.1× (z +19.3) | — |
| [[LoVo (line)]] | wt | 2.06 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 54.8× (z +16.4) | — |
| [[SW 900 (line)]] | alt | 4.76 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.1× (z +14.3) | — |
| [[A-172 (line)]] | wt | 2.74 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 12.7× (z +10.8) | — |
| [[BT-474 (line)]] | alt | 5.43 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 24.4× (z +12.8) | — |
| [[CFPAC-1 (line)]] | alt | 3.40 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 42.0× (z +15.2) | — |
| [[HCT15 (line)]] | alt | 5.81 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 12.6× (z +9.0) | — |
| [[Panc 03.27 (line)]] | alt | 2.67 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.5× (z +12.3) | — |
| [[RPMI-7951 (line)]] | alt | 10.7 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 27.6× (z +16.4) | — |
| [[SK-MEL-2 (line)]] | alt | 7.84 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 21.1× (z +15.4) | — |
| [[SW1417 (line)]] | alt | 85.3 | 2 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.72× (z +12.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 2.95 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 11.9× (z +10.7) | — |
| [[NCI-H23 (line)]] | alt | 26.2 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +11.3) | — |
| [[A-427 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.80 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 1.14 n.m. | — | — | — | — |
| [[C-33 A (line)]] | alt | 9.99 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 1.28 n.m. | — | — | — | — |
| [[H4 (line)]] | wt | 1.77 n.m. | — | — | — | — |
| [[HEC-1-A (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 2.43 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 1.73 n.m. | — | — | — | — |
| [[HS-578T (line)]] | alt | 1.17 n.m. | — | — | — | — |
| [[HT-29 (line)]] | alt | 1.95 n.m. | — | — | — | — |
| [[hTERT-HPNE (line)]] | wt | 1.52 n.m. | — | — | — | — |
| [[KATO III (line)]] | alt | 0.914 n.m. | — | — | — | — |
| [[LOX-IMVI (line)]] | wt | 1.41 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 0.941 n.m. | — | — | — | — |
| [[NCI-H1792 (line)]] | alt | 1.34 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 8.80 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.95 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 0.981 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 100 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 3.06 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 1.41 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 3.76 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 4.68 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 1.21 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 2393), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*91 of its nearest partners move with it, 1 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC35F1]] | +0.67 | +0.73 / +0.63 | both halves | 7e-06 |  |
| [[DLGAP2]] | +0.65 | +0.70 / +0.58 | both halves | 7e-06 |  |
| [[ANGPT2]] | +0.64 | +0.72 / +0.44 | both halves | 3e-05 |  |
| [[ZNF341-AS1]] | +0.64 | +0.70 / +0.41 | both halves | 4e-05 |  |
| [[LETM2]] | +0.64 | +0.72 / +0.53 | both halves | 1e-05 |  |
| [[CACNA1E]] | +0.64 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[THSD7B]] | +0.63 | +0.69 / +0.50 | both halves | 1e-05 |  |
| [[GNG4]] | +0.63 | +0.52 / +0.62 | both halves | 1e-05 |  |
| [[MTUS2]] | +0.62 | +0.71 / +0.64 | both halves | 7e-06 |  |
| [[XKR4]] | +0.61 | +0.70 / +0.53 | both halves | 1e-05 |  |
| [[KBTBD12]] | +0.61 | +0.55 / +0.37 | both halves | 8e-05 |  |
| [[RELN]] | +0.60 | +0.56 / +0.51 | both halves | 1e-05 |  |

## Genes that move opposite

*9 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFP14]] | -0.63 | -0.55 / -0.46 | both halves | 3e-05 |  |
| [[RHOT1]] | -0.59 | -0.51 / -0.47 | both halves | 2e-05 |  |
| [[EHMT2]] | -0.54 | -0.49 / -0.30 | both halves | 2e-04 |  |
| [[ATRN]] | -0.54 | -0.52 / -0.41 | both halves | 4e-05 |  |
| [[IFT172]] | -0.53 | -0.40 / -0.38 | both halves | 6e-05 |  |
| [[DFFB]] | -0.53 | -0.47 / -0.48 | both halves | 2e-05 |  |
| [[MPHOSPH9]] | -0.53 | -0.49 / -0.39 | both halves | 6e-05 |  |
| [[ATP5F1C]] | -0.53 | -0.55 / -0.32 | both halves | 2e-04 |  |
| [[UBAC1]] | -0.53 | -0.56 / -0.40 | both halves | 5e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 2, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers AP3B2's level | compounds that target TOP2A: 5 of 5 raise it (Amsacrine, Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 100% of the class's compounds vs 8.4% of all compounds | 0.015 | ⚠ off-target possible; 5 compounds; artifact flags |
| [[RGS7]] | B | RGS7 activity raises AP3B2's level | lines that do not express RGS7 (25) vs lines expressing it (25) | 1.87× lower at baseline in the lines without RGS7 | 0.095 | ⚠ within organs, on part of the lines; also absent: KCNQ5, NRXN3, ENSG00000253553; maybe low, not absent |
| [[GNG4]] | C | GNG4 activity raises AP3B2's level | lines that do not express GNG4 (20) vs lines expressing it (30) | 2.14× lower at baseline in the lines without GNG4 | 0.067 | ⚠ within organs, on part of the lines; also absent: OLFM1, JPH3, LRRC4B; co-absent with the target |

### Downstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 5, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MTUS2]] | B | AP3B2 activity strengthens MTUS2's drug response | lines that do not express AP3B2 (15) vs lines expressing it (31) | the lines without AP3B2 respond 0.57× as strongly (z diff +2.39); strongest at Panobinostat 5 µM: 3.07x vs 7.90x (z diff +3.2) | 0.012 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent; target measured in part of the lines; artifact flags |
| [[TUT7]] | B | AP3B2 activity lowers TUT7's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.41× higher at baseline in the lines without AP3B2 | 0.013 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |
| [[USP11]] | B | AP3B2 activity raises USP11's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.56× lower at baseline in the lines without AP3B2 | 0.027 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |
| [[DISP3]] | B | AP3B2 activity raises DISP3's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.76× lower at baseline in the lines without AP3B2 | 0.041 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |
| [[LMNB1-DT]] | B | AP3B2 activity raises LMNB1-DT's level | lines that do not express AP3B2 (15) vs lines expressing it (35) | 1.39× lower at baseline in the lines without AP3B2 | 0.081 | ⚠ within organs, on part of the lines; also absent: MAPK8IP2, MED12L, HRK; maybe low, not absent |

## Where it sits

- **Module**: [[Module 165]]; 26 genes; every member is in the + arm (projection on the module's main direction 0.697). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (21.1, 32.5); signed map (29.8, 18.4). **Vector** length 66.6, 13.2% of its response variance represented; |z| ≥ 3 in 951 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +8.0 | +11.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +7.7 | +35.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~29% of this change | +7.6 | +11.8 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~26% of this change | +6.9 | +9.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +6.8 | +44.9 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +5.8 | +14.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +5.8 | +11.7 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.6 | +12.3 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +2.2 | +5.9 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +2.1 | +2.7 |
| fall | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | -2.2 | -2.6 |
|  | [[Radotinib (drug)]] 5 µM |  | -2.2 | -3.5 |
|  | [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | -1.7 | +1.9 |
|  | [[Lucanthone (drug)]] 0.05 µM |  | -1.6 | -1.0 |
|  | [[NG25 (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~49% of this change | -1.6 | -3.3 |
|  | [[Ipatasertib (drug)]] 5 µM |  | -1.4 | -2.2 |
|  | [[Erlotinib (drug)]] 0.05 µM |  | -1.3 | -1.6 |

## What is on record

|  |  |
|---|---|
| Name | adaptor related protein complex 3 subunit beta 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 15q25.2 — chr15:82,659,281-82,710,112 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NAPTB |
| Gene groups (HGNC) | Clathrin/coatomer adaptor, adaptin-like, N-terminal domain containing; Adaptor related protein complex 3 |
| Matched by | ensembl_id |

**Function**, from UniProt [Q13367](https://www.uniprot.org/uniprotkb/Q13367) (AP-3 complex subunit beta-2):

> Subunit of non-clathrin- and clathrin-associated adaptor protein complex 3 (AP-3) that plays a role in protein sorting in the late-Golgi/trans-Golgi network (TGN) and/or endosomes. The AP complexes mediate both the recruitment of clathrin to membranes and the recognition of sorting signals within the cytosolic tails of transmembrane cargo molecules. AP-3 appears to be involved in the sorting of a subset of transmembrane proteins targeted to lysosomes and lysosome-related organelles. In concert …

**Summary**, from NCBI Gene [8120](https://www.ncbi.nlm.nih.gov/gene/8120):

> Adaptor protein complex 3 (AP-3 complex) is a heterotrimeric protein complex involved in the formation of clathrin-coated synaptic vesicles. The protein encoded by this gene represents the beta subunit of the neuron-specific AP-3 complex and was first identified as the target antigen in human paraneoplastic neurologic disorders. The encoded subunit binds clathrin and is phosphorylated by a casein kinase-like protein, which mediates synaptic vesicle coat assembly. Defects in this gene are a …

**Accessions** — [HGNC:567](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:567) · Entrez [8120](https://www.ncbi.nlm.nih.gov/gene/8120) · UniProt [Q13367](https://www.uniprot.org/uniprotkb/Q13367) · Ensembl [ENSG00000103723](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000103723)

## Data

Gene col 2393: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 2393); `tables/drug_effects.parquet` (47 rows, flagged included); `relations/gene_relations.parquet` (col_a == 2393, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 2393]; `tensor/DDL_lfc|DDL_z.npy` [2393]; `embed/gene_vectors.npy` [2393]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 2393 or target_col == 2393). Every well: [[AP3B2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/AP3B2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
