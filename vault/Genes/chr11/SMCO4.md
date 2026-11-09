---
symbol: "SMCO4"
type: "gene"
col: 9222
ensembl_id: "ENSG00000166002"
name: "single-pass membrane protein with coiled-coil domains 4"
location: "11q21"
module: 49
arm: "+"
pooled_cpm: 14.23
n_lines_expressing: 48
n_dd_up: 4
n_dd_down: 23
n_dd_up_clean: 4
n_dd_down_clean: 17
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/049"]
generated_by: "tahoemap"
---

# SMCO4

*single-pass membrane protein with coiled-coil domains 4* — 11q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 4 drug-doses (none with an alert); the strongest is [[Tucidinostat (drug)]] 5 µM: 1.38× (z +7.5, q 3e-11, up in 23 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 23 drug-doses (6 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 0.399× (z -7.9, q 1e-12, down in 25 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[TMEM243]] (+0.63, fdr 1e-05), [[PDXDC1]] (+0.58, fdr 1e-05), [[PDIA5]] (+0.57, fdr 1e-05); moves opposite to [[SUMF1]] (-0.50, fdr 3e-05), [[DNAJC8]] (-0.46, fdr 4e-05), [[LYRM2]] (-0.46, fdr 6e-05).
> It is in [[Module 049]], a single-armed module (XBP1(S) activates chaperone genes).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[SLC1A1]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 5 in all, 1 with an alert ⚠. 4 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 9222.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **1.38×** | +7.5 | 3e-11 | 23/45 (PANC-1, SW480, …) | all doses, stronger at high dose |  |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.49×** | +6.6 | 1e-08 | 23/44 (NCI-H2347, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.34×** | +4.8 | 3e-04 | 15/45 (PANC-1, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Brivudine (drug)]] 5 µM |  | **1.63×** | +4.2 | 0.004 | 8/45 (PANC-1, SW480, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | 1.18× | +3.8 | 0.016 | 16/45 (NCI-H460, SW480, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 6 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 23 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 9222.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **0.399×** | -7.9 | 1e-12 | 25/45 (LS 180, H4, …) | rises with dose | plate-row cell shift; cell-cycle shift (explains ~7% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.634×** | -7.5 | 2e-11 | 28/43 (KATO III, LS 180, …) | two highest doses |  |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.694×** | -6.0 | 3e-07 | 22/44 (HS-578T, A498, …) | all doses, flat |  |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~26% of this change | **0.701×** | -5.9 | 7e-07 | 24/45 (LS 180, KATO III, …) | all doses, stronger at high dose | composition shift |
| [[Selinexor (drug)]] 5 µM |  | **0.789×** | -5.5 | 4e-06 | 22/46 (A-172, HS-578T, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.718×** | -5.5 | 5e-06 | 18/45 (LS 180, HEC-1-A, …) | two highest doses | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **0.794×** | -5.4 | 6e-06 | 24/43 (HS-578T, A498, …) | all doses, flat | composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.726×** | -5.3 | 9e-06 | 21/42 (HS-578T, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~22% of this change | **0.752×** | -4.7 | 2e-04 | 14/44 (KATO III, SW 900, …) | all doses, stronger at high dose |  |
| [[Auranofin (drug)]] 5 µM |  | **0.762×** | -4.5 | 4e-04 | 19/44 (KATO III, LS 180, …) | rises with dose |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.769×** | -4.3 | 8e-04 | 18/44 (HS-578T, A498, …) | all doses, flat | cell-cycle shift (explains ~14% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.833×** | -4.3 | 9e-04 | 22/45 (A498, H4, …) | rises with dose |  |
| [[Belumosudil (drug)]] 5 µM |  | **0.777×** | -4.0 | 0.003 | 15/44 (NCI-H2030, NCI-H23, …) | top dose only |  |
| [[EX229 (drug)]] 5 µM |  | **0.639×** | -3.9 | 0.004 | 7/42 (A-172, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Belzutifan (drug)]] 5 µM |  | **0.645×** | -3.8 | 0.006 | 12/43 (SNU-423, HCT15, …) | top dose only | noisy plate (z scaled) |
| [[Thymol (drug)]] 5 µM |  | 0.855× | -3.7 | 0.009 | 13/45 (LoVo, J82, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.818×** | -3.3 | 0.026 | 7/44 (HOP62, LoVo, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.820×** | -3.3 | 0.028 | 8/45 (HT-29, LoVo, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 9222. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HS-578T (line)]] | alt | 25.2 | 0 | 5 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.221× (z -15.3) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.237× (z -10.4) |
| [[A498 (line)]] | wt | 14.9 | 0 | 3 (2 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.319× (z -12.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.311× (z -9.0) |
| [[HT-29 (line)]] | alt | 19.6 | 0 | 3 (3 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.223× (z -9.3) ⚠ toxic; cell-cycle shift, explains ~4% of this change |
| [[LS 180 (line)]] | wt | 40.3 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.107× (z -17.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change · without an alert: [[Ixazomib citrate (drug)]] 5 µM 0.291× (z -10.3) |
| [[Hs 766T (line)]] | wt | 9.33 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.190× (z -10.4) ⚠ cell-cycle shift, explains ~45% of this change · without an alert: [[Lidocaine (hydrochloride) (drug)]] 0.05 µM 0.140× (z -8.7) |
| [[HepG2_C3A (line)]] | wt | 21.9 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.177× (z -8.5) |
| [[HOP62 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.334× (z -8.6) ⚠ cell-cycle shift, explains ~45% of this change |
| [[hTERT-HPNE (line)]] | wt | 10.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0916× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[KATO III (line)]] | alt | 27.7 | 0 | 1 | — | [[Ixazomib citrate (drug)]] 0.5 µM 0.305× (z -9.7) |
| [[NCI-H460 (line)]] | wt | 5.14 | 0 | 1 | — | [[Cysteamine (hydrochloride) (drug)]] 0.5 µM 0.176× (z -8.9) |
| [[RPMI-7951 (line)]] | alt | 9.80 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0765× (z -10.2) |
| [[SW 900 (line)]] | alt | 24.0 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0965× (z -15.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[A-172 (line)]] | wt | 4.68 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 15.4 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 9.36 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 4.06 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 5.97 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 1.16 n.m. | — | — | — | — |
| [[CFPAC-1 (line)]] | alt | 5.31 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 2.47 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 18.4 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 20.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 28.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 9.33 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 4.86 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 7.17 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 11.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 7.21 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 4.27 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 7.54 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.45 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 20.8 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 23.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 5.42 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 23.6 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 11.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 15.0 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 19.9 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 17.3 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 12.8 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 9222), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*93 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TMEM243]] | +0.63 | +0.72 / +0.52 | both halves | 1e-05 |  |
| [[PDXDC1]] | +0.58 | +0.58 / +0.51 | both halves | 1e-05 |  |
| [[PDIA5]] | +0.57 | +0.58 / +0.54 | both halves | 1e-05 |  |
| [[MCEE]] | +0.57 | +0.61 / +0.51 | both halves | 1e-05 |  |
| [[SSR3]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[SLC1A1]] | +0.57 | +0.57 / +0.51 | both halves | 1e-05 |  |
| [[KDELR3]] | +0.56 | +0.60 / +0.45 | both halves | 3e-05 |  |
| [[PDXDC2P]] | +0.56 | +0.58 / +0.49 | both halves | 1e-05 |  |
| [[SEC24D]] | +0.55 | +0.53 / +0.50 | both halves | 1e-05 |  |
| [[ARL1]] | +0.55 | +0.54 / +0.42 | both halves | 4e-05 |  |
| [[NFXL1]] | +0.55 | +0.61 / +0.48 | both halves | 2e-05 |  |
| [[GORASP2]] | +0.54 | +0.51 / +0.48 | both halves | 2e-05 |  |

## Genes that move opposite

*7 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SUMF1]] | -0.50 | -0.48 / -0.46 | both halves | 3e-05 |  |
| [[DNAJC8]] | -0.46 | -0.46 / -0.41 | both halves | 4e-05 |  |
| [[LYRM2]] | -0.46 | -0.49 / -0.38 | both halves | 6e-05 |  |
| [[GPATCH3]] | -0.46 | -0.40 / -0.45 | both halves | 5e-05 |  |
| [[ZFYVE26]] | -0.45 | -0.35 / -0.49 | both halves | 1e-04 |  |
| [[CCDC191]] | -0.44 | -0.44 / -0.42 | both halves | 4e-05 |  |
| [[ZMAT2]] | -0.43 | -0.44 / -0.38 | both halves | 6e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[SLC1A1]] | B | SLC1A1 activity strengthens SMCO4's drug response | lines that do not express SLC1A1 (10) vs lines expressing it (36) | the lines without SLC1A1 respond 0.55× as strongly (z diff +1.22); strongest at Homoharringtonine 5 µM: 1.15x vs 0.62x (z diff +4.8) | 0.041 | ⚠ within organs, on part of the lines; also absent: UST, HLA-F; maybe low, not absent; target measured in part of the lines; both ways; artifact flags |
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity lowers SMCO4's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 raise it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 0.8% of all compounds | 0.044 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 049]] — XBP1(S) activates chaperone genes; 93 genes; every member is in the + arm (projection on the module's main direction 0.541). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.12; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (14.4, -33.9); signed map (-52.3, 10.0). **Vector** length 82.9, 15.6% of its response variance represented; |z| ≥ 3 in 978 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Tucidinostat (drug)]] 5 µM |  | +5.7 | +7.5 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +5.2 | +6.6 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change | +3.9 | +0.6 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~0% of this change | +3.6 | +3.8 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift | +3.3 | +1.8 |
|  | [[Brivudine (drug)]] 5 µM |  | +2.1 | +4.2 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | +1.9 | +2.0 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.9 | +2.7 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | +1.8 | +2.2 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -3.3 | -6.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.6 | -7.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.5 | -2.3 |
|  | [[Selinexor (drug)]] 5 µM |  | -2.4 | -5.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.4 | -4.3 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -2.0 | -2.1 |
|  | [[Thymol (drug)]] 5 µM |  | -1.8 | -3.7 |

## What is on record

|  |  |
|---|---|
| Name | single-pass membrane protein with coiled-coil domains 4 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q21 — chr11:93,478,472-93,543,391 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FN5; previously C11orf75 |
| Matched by | ensembl_id |

UniProt [Q9NRQ5](https://www.uniprot.org/uniprotkb/Q9NRQ5) carries no function annotation.

**Summary**, from NCBI Gene [56935](https://www.ncbi.nlm.nih.gov/gene/56935):

> Predicted to be located in membrane. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:24810](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:24810) · Entrez [56935](https://www.ncbi.nlm.nih.gov/gene/56935) · UniProt [Q9NRQ5](https://www.uniprot.org/uniprotkb/Q9NRQ5) · Ensembl [ENSG00000166002](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000166002)

## Data

Gene col 9222: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 9222); `tables/drug_effects.parquet` (31 rows, flagged included); `relations/gene_relations.parquet` (col_a == 9222, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 9222]; `tensor/DDL_lfc|DDL_z.npy` [9222]; `embed/gene_vectors.npy` [9222]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 9222 or target_col == 9222). Every well: [[SMCO4 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SMCO4.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
