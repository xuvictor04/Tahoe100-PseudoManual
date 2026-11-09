---
symbol: "PLEC"
type: "gene"
col: 10908
ensembl_id: "ENSG00000178209"
name: "plectin"
location: "8q24.3"
module: 78
arm: "+"
pooled_cpm: 237.05
n_lines_expressing: 47
n_dd_up: 12
n_dd_down: 9
n_dd_up_clean: 9
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 11
direction_downstream: 12
tags: ["gene", "module/078"]
generated_by: "tahoemap"
---

# PLEC

*plectin* — 8q24.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 12 drug-doses (3 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 1.89× (z +10.1, q 3e-21, up in 33 of 45 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Bortezomib (drug)]] 5 µM: 0.251× (z -8.1, q 2e-13, down in 40 of 42 measured lines) ⚠ toxic. The strongest without an alert is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.656× (z -6.7, q 4e-09, down in 32 of 46 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ARHGDIA]] (+0.79, fdr 7e-06), [[ITPR3]] (+0.71, fdr 7e-06), [[FLNA]] (+0.66, fdr 7e-06); moves opposite to [[WDR83OS]] (-0.56, fdr 1e-05, ⚠ WDR83OS in the vector space only through flagged drug-doses), [[TBK1]] (-0.55, fdr 2e-05), [[COA6]] (-0.55, fdr 1e-05), [[UBE4B]] (-0.53, fdr 1e-05).
> It is in [[Module 078]], a single-armed module (apical junction).
> Probable direction (from the cell lines, not proof of direct regulation): 11 arrows point to it, the strongest [[ITGA3]] → it (grade B ⚠); 12 go from it, the strongest it → [[FLNA]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 4 with an alert ⚠. 12 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 10908.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **1.89×** | +10.1 | 3e-21 | 33/45 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **1.82×** | +6.5 | 3e-08 | 32/45 (PANC-1, NCI-H1792, …) | rises with dose | cell-cycle shift (explains ~2% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.78×** | +6.2 | 9e-08 | 32/42 (SNU-423, NCI-H1792, …) | all doses, flat | cell-cycle shift (explains ~10% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.74×** | +5.8 | 1e-06 | 36/43 (SNU-423, RPMI-7951, …) | all doses, flat | cell-cycle shift (explains ~8% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.74×** | +5.3 | 1e-05 | 32/46 (NCI-H1792, SNU-423, …) | all doses, flat | cell-cycle shift (explains ~11% here); composition shift; position effect removed |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.59×** | +5.2 | 2e-05 | 28/45 (PANC-1, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.43×** | +4.0 | 0.005 | 26/45 (NCI-H1792, hTERT-HPNE, …) | two highest doses | cell-cycle shift (explains ~9% here); position effect removed |
| [[Belumosudil (drug)]] 5 µM |  | **1.45×** | +4.0 | 0.005 | 24/45 (NCI-H1792, LOX-IMVI, …) | top dose only |  |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.47×** | +3.7 | 0.011 | 27/45 (NCI-H460, A549, …) | rises with dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **1.37×** | +3.5 | 0.027 | 22/45 (NCI-H1792, RKO, …) | top dose only | cell-cycle shift (explains ~10% here); position effect removed |
| [[Sapanisertib (drug)]] 0.05 µM |  | **1.42×** | +3.4 | 0.029 | 30/45 (HEC-1-A, A498, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM |  | **1.32×** | +3.1 | 0.094 | 26/45 (NCI-H1792, Panc 03.27, …) | two highest doses | cell-cycle shift (explains ~12% here); position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | 1.32× | +3.0 | 0.11 | 25/45 (NCI-H1792, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 10908.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Bortezomib (drug)]] 5 µM | ⚠ toxic | **0.251×** | -8.1 | 2e-13 | 40/42 (HS-578T, HOP62, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here); noisy plate (z scaled); position effect removed |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.656×** | -6.7 | 4e-09 | 32/46 (HEC-1-A, KATO III, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.506×** | -6.7 | 4e-09 | 40/45 (HOP62, A-172, …) | all doses, stronger at high dose | cell-cycle shift (explains ~2% here); position effect removed |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.560×** | -6.5 | 1e-08 | 38/45 (HOP62, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.690×** | -4.0 | 0.007 | 29/44 (PANC-1, SW480, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.708×** | -3.8 | 0.013 | 37/46 (Panc 03.27, LS 180, …) | inconsistent across doses |  |
| [[NG25 (drug)]] 5 µM |  | **0.530×** | -3.7 | 0.015 | 30/44 (SK-MEL-2, RPMI-7951, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled); position effect removed |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.724×** | -3.6 | 0.018 | 21/45 (SK-MEL-2, HOP62, …) | rises with dose |  |
| [[Amsacrine (drug)]] 5 µM |  | **0.797×** | -3.6 | 0.018 | 26/45 (PANC-1, HOP62, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.913× | -3.6 | 0.018 | 4/47 (NCI-H1792, HOP62, …) | inconsistent across doses |  |
| [[Trimetrexate (drug)]] 5 µM |  | 0.827× | -3.0 | 0.12 | 22/46 (PANC-1, NCI-H23, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.08 per unit of S-phase module lfc, +0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 10908. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 326 | 0 | 13 (2 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.251× (z -13.4) |
| [[SK-MEL-2 (line)]] | alt | 234 | 0 | 12 (3 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.267× (z -13.9) |
| [[NCI-H1792 (line)]] | alt | 98.6 | 7 (3 ⚠) | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.99× (z +15.2) | [[Adagrasib (drug)]] 0.05 µM 0.639× (z -10.7) ⚠ position not correctable |
| [[HOP62 (line)]] | alt | 484 | 1 | 5 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.09× (z +8.6) | [[Ixazomib citrate (drug)]] 5 µM 0.196× (z -13.4) |
| [[A549 (line)]] | wt | 295 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +17.2) | — |
| [[H4 (line)]] | wt | 247 | 1 | 3 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.64× (z +10.9) | [[Ixazomib citrate (drug)]] 5 µM 0.247× (z -11.2) |
| [[MIA PaCa-2 (line)]] | alt | 144 | 0 | 4 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.101× (z -17.4) |
| [[PANC-1 (line)]] | alt | 214 | 3 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 4.85× (z +23.6) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.409× (z -9.0) ⚠ toxic |
| [[SNU-423 (line)]] | alt | 113 | 4 (3 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.59× (z +15.9) | — |
| [[A-172 (line)]] | wt | 227 | 0 | 3 | — | [[Ixazomib citrate (drug)]] 5 µM 0.255× (z -11.8) |
| [[AsPC-1 (line)]] | alt | 625 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.61× (z +14.4) | — |
| [[CFPAC-1 (line)]] | alt | 281 | 1 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 2.75× (z +10.7) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.402× (z -9.7) |
| [[HS-578T (line)]] | alt | 415 | 0 | 3 (1 ⚠) | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.410× (z -11.2) |
| [[Panc 03.27 (line)]] | alt | 229 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.50× (z +17.6) | — |
| [[RPMI-7951 (line)]] | alt | 217 | 2 (2 ⚠) | 1 | [[Dinaciclib (drug)]] 5 µM 3.31× (z +9.5) ⚠ toxic; transcription drop | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.330× (z -13.1) |
| [[SW 900 (line)]] | alt | 156 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.45× (z +17.9) | — |
| [[SW1417 (line)]] | alt | 265 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.81× (z +16.6) | — |
| [[A498 (line)]] | wt | 235 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.99× (z +12.8) | [[Ixazomib citrate (drug)]] 5 µM 0.330× (z -9.1) |
| [[HepG2_C3A (line)]] | wt | 199 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 2.88× (z +11.0) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.378× (z -10.4) |
| [[J82 (line)]] | alt | 205 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.57× (z +15.8) | — |
| [[LOX-IMVI (line)]] | wt | 233 | 1 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.03× (z +12.6) | [[Ixazomib citrate (drug)]] 5 µM 0.354× (z -8.5) |
| [[NCI-H1573 (line)]] | alt | 325 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 4.33× (z +10.4) | — |
| [[NCI-H460 (line)]] | wt | 89.3 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 3.51× (z +10.2) | — |
| [[AN3 CA (line)]] | alt | 61.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.59× (z +11.5) | — |
| [[HCT15 (line)]] | alt | 244 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.327× (z -12.0) |
| [[HEC-1-A (line)]] | alt | 297 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.300× (z -14.3) |
| [[KATO III (line)]] | alt | 301 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.268× (z -14.1) |
| [[LoVo (line)]] | wt | 151 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.441× (z -9.2) |
| [[NCI-H2030 (line)]] | alt | 155 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.39× (z +11.1) | — |
| [[A-427 (line)]] | wt | 82.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 208 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 72.5 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 159 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 89.3 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 48.2 n.m. | — | — | — | — |
| [[Hs 766T (line)]] | wt | 542 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 261 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 197 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 176 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 232 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 175 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 427 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 197 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 73.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 68.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 54.0 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 56.5 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 252 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 149 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 134 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 10908), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ARHGDIA]] | +0.79 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[ITPR3]] | +0.71 | +0.63 / +0.69 | both halves | 7e-06 |  |
| [[FLNA]] | +0.66 | +0.68 / +0.66 | both halves | 7e-06 | pathway: Cell junction organization; STRING 812 |
| [[INF2]] | +0.65 | +0.61 / +0.62 | both halves | 7e-06 |  |
| [[R3HDM4]] | +0.63 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[MYH9]] | +0.62 | +0.56 / +0.59 | both halves | 1e-05 | same gene group; STRING 572 |
| [[AGRN]] | +0.61 | +0.58 / +0.60 | both halves | 7e-06 | pathway: Extracellular matrix organization; STRING 494 |
| [[PTPRN2]] | +0.61 | +0.58 / +0.52 | both halves | 1e-05 | same gene group |
| [[ZYX]] | +0.61 | +0.62 / +0.61 | both halves | 7e-06 | same gene group |
| [[FAAP100]] | +0.61 | +0.56 / +0.54 | both halves | 1e-05 |  |
| [[STMN3]] | +0.61 | +0.60 / +0.52 | both halves | 1e-05 |  |
| [[C15orf39]] | +0.60 | +0.63 / +0.56 | both halves | 1e-05 |  |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[WDR83OS]] ⚠ | -0.56 | -0.50 / -0.57 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[TBK1]] | -0.55 | -0.49 / -0.48 | both halves | 2e-05 |  |
| [[COA6]] | -0.55 | -0.49 / -0.50 | both halves | 1e-05 |  |
| [[UBE4B]] | -0.53 | -0.50 / -0.54 | both halves | 1e-05 |  |
| [[ELMOD3]] | -0.53 | -0.53 / -0.46 | both halves | 3e-05 |  |
| [[HIGD2A]] | -0.53 | -0.38 / -0.52 | both halves | 7e-05 |  |
| [[SNX13]] | -0.52 | -0.57 / -0.39 | both halves | 5e-05 |  |
| [[PDSS2]] | -0.51 | -0.44 / -0.50 | both halves | 3e-05 |  |
| [[PCBD1]] | -0.50 | -0.33 / -0.53 | both halves | 1e-04 |  |
| [[ZNF148]] | -0.50 | -0.43 / -0.39 | both halves | 5e-05 |  |
| [[PSMB5]] | -0.49 | -0.36 / -0.47 | both halves | 9e-05 | pathway: Apoptosis |
| [[TENT2]] | -0.49 | -0.42 / -0.42 | both halves | 4e-05 |  |
| [[NDUFB4]] | -0.49 | -0.46 / -0.49 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*11 arrows, 11 of them with an alert ⚠; grade A 0, B 10, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ITGA3]] | B | ITGA3 activity raises PLEC's level | lines that do not express ITGA3 (10) vs lines expressing it (40) | 2.67× lower at baseline in the lines without ITGA3 | 0.010 | ⚠ within organs, on part of the lines; also absent: IL15, GBP2, CD82; maybe low, not absent |
| [[ELFN2]] | B | ELFN2 activity raises PLEC's level | lines that do not express ELFN2 (19) vs lines expressing it (31) | 2.03× lower at baseline in the lines without ELFN2 | 0.023 | ⚠ within organs, on part of the lines; also absent: IL31RA, LHX1, TMEM92 |
| [[ITGB4]] | B | ITGB4 activity raises PLEC's level | lines that do not express ITGB4 (25) vs lines expressing it (25) | 1.50× lower at baseline in the lines without ITGB4 | 0.049 | ⚠ within organs, on part of the lines; also absent: SCNN1A, AREG, GJB3 |
| [[CCND1]] | B | CCND1 activity raises PLEC's level | lines that do not express CCND1 (7) vs lines expressing it (43) | 2.46× lower at baseline in the lines without CCND1 | 0.055 | ⚠ within organs, on part of the lines; also absent: FSTL3, ADAMTSL5; maybe low, not absent |
| [[NIBAN2]] | B | NIBAN2 activity raises PLEC's level | lines that do not express NIBAN2 (5) vs lines expressing it (45) | 2.98× lower at baseline in the lines without NIBAN2 | 0.060 | ⚠ within organs, on part of the lines; co-absent genes; also absent: SMOX, SLC2A1, ENSG00000281883; maybe low, not absent; its own permutation p |
| [[PKP3]] | B | PKP3 activity raises PLEC's level | lines that do not express PKP3 (15) vs lines expressing it (35) | 1.72× lower at baseline in the lines without PKP3 | 0.069 | ⚠ within organs, on part of the lines; also absent: KRT18, PTK6, SFN; maybe low, not absent |
| [[SDC4]] | B | SDC4 activity raises PLEC's level | lines that do not express SDC4 (5) vs lines expressing it (45) | 3.11× lower at baseline in the lines without SDC4 | 0.090 | ⚠ within organs, on part of the lines; also absent: LAMB1, TGFBR2, PHLDA2 |
| [[TOR4A]] | B | TOR4A activity raises PLEC's level | lines that do not express TOR4A (14) vs lines expressing it (36) | 1.50× lower at baseline in the lines without TOR4A | 0.091 | ⚠ within organs, on part of the lines; also absent: PLEKHA6, CDCP1, C19orf33 |
| [[HDAC6]] | B | HDAC6 activity lowers PLEC's level | compounds that target HDAC6: 2 of 2 raise it (Belinostat, Panobinostat) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises PLEC's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |
| [[MAPK11]] | C | MAPK11 activity raises PLEC's level | lines that do not express MAPK11 (3) vs lines expressing it (47) | 2.82× lower at baseline in the lines without MAPK11 | 0.0995 | ⚠ few lines (3 vs 47); across organs; also absent: ADCY7, DBN1, LAMC1; maybe low, not absent; co-absent with the target |

### Downstream of this gene

*12 arrows, 12 of them with an alert ⚠; grade A 0, B 0, C 12.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FLNA]] | C | PLEC activity raises FLNA's level | lines that do not express PLEC (3) vs lines expressing it (47) | 4.31× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[ITPR3]] | C | PLEC activity raises ITPR3's level | lines that do not express PLEC (3) vs lines expressing it (47) | 3.93× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[FGFRL1]] | C | PLEC activity raises FGFRL1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 2.69× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[EPHA2]] | C | PLEC activity raises EPHA2's level | lines that do not express PLEC (3) vs lines expressing it (47) | 2.47× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[AGRN]] | C | PLEC activity raises AGRN's level | lines that do not express PLEC (3) vs lines expressing it (47) | 2.28× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[PLCB3]] | C | PLEC activity raises PLCB3's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.93× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[CEP170B]] | C | PLEC activity raises CEP170B's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.59× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[INF2]] | C | PLEC activity raises INF2's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.49× lower at baseline in the lines without PLEC | 0.060 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[LAMA5]] | C | PLEC activity raises LAMA5's level | lines that do not express PLEC (3) vs lines expressing it (47) | 3.34× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[CLIC1]] | C | PLEC activity raises CLIC1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.55× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[UBA1]] | C | PLEC activity raises UBA1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.50× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |
| [[PCBD1]] | C | PLEC activity raises PCBD1's level | lines that do not express PLEC (3) vs lines expressing it (47) | 1.30× lower at baseline in the lines without PLEC | 0.089 | ⚠ few lines (3 vs 47); within organs, on part of the lines; also absent: BOK, MYH16, PER3; maybe low, not absent; its own permutation p |

## Where it sits

- **Module**: [[Module 078]] — apical junction; 58 genes; every member is in the + arm (projection on the module's main direction 0.654). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.20; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (16.1, -4.5); signed map (-7.8, 32.2). **Vector** length 161, 56.1% of its response variance represented; |z| ≥ 3 in 1,269 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Harringtonine (drug)]] 0.5 µM |  | +5.8 | +3.7 |
|  | [[Harringtonine (drug)]] 5 µM |  | +5.7 | +6.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +5.3 | +4.0 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | +5.2 | +5.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | +5.0 | +3.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +5.0 | +2.0 |
|  | [[Pitavastatin (Calcium) (drug)]] 0.5 µM |  | +4.0 | +2.0 |
|  | [[Budesonide (drug)]] 5 µM |  | +3.6 | +2.1 |
|  | [[PH-797804 (drug)]] 0.05 µM |  | +3.5 | +2.2 |
| fall | [[Bortezomib (drug)]] 0.05 µM |  | -9.4 | -6.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -8.2 | -6.5 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -7.6 | -6.7 |
|  | [[Bortezomib (drug)]] 5 µM | ⚠ toxic | -7.1 | -8.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -6.8 | -3.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -6.1 | -2.7 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -4.9 | -3.0 |
|  | [[Trametinib (drug)]] 0.5 µM |  | -4.8 | -2.9 |
|  | [[Binimetinib (drug)]] 0.5 µM |  | -4.5 | -2.4 |

## What is on record

|  |  |
|---|---|
| Name | plectin |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 8q24.3 — chr8:143,915,153-143,976,734 (-) |
| Ensembl biotype | protein_coding |
| Also known as | PCN, PLTN; previously EBS1, PLEC1 |
| Gene groups (HGNC) | Plakins; MicroRNA protein coding host genes; Spectrin repeat containing; SH3 domain containing |
| Hallmark sets | IL2_STAT5_SIGNALING |
| Reactome | 11 pathways, smallest: Type I hemidesmosome assembly; Caspase-mediated cleavage of cytoskeletal proteins; Apoptotic cleavage of cellular proteins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q15149](https://www.uniprot.org/uniprotkb/Q15149) (Plectin):

> Interlinks intermediate filaments with microtubules and microfilaments and anchors intermediate filaments to desmosomes or hemidesmosomes. Could also bind muscle proteins such as actin to membrane complexes in muscle. May be involved not only in the filaments network, but also in the regulation of their dynamics. Structural component of muscle. Isoform 9 plays a major role in the maintenance of myofiber integrity.

**Summary**, from NCBI Gene [5339](https://www.ncbi.nlm.nih.gov/gene/5339):

> Plectin is a prominent member of an important family of structurally and in part functionally related proteins, termed plakins or cytolinkers, that are capable of interlinking different elements of the cytoskeleton. Plakins, with their multi-domain structure and enormous size, not only play crucial roles in maintaining cell and tissue integrity and orchestrating dynamic changes in cytoarchitecture and cell shape, but also serve as scaffolding platforms for the assembly, positioning, and …

**Accessions** — [HGNC:9069](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:9069) · Entrez [5339](https://www.ncbi.nlm.nih.gov/gene/5339) · UniProt [Q15149](https://www.uniprot.org/uniprotkb/Q15149) · Ensembl [ENSG00000178209](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000178209)

## Data

Gene col 10908: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 10908); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 10908, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 10908]; `tensor/DDL_lfc|DDL_z.npy` [10908]; `embed/gene_vectors.npy` [10908]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 10908 or target_col == 10908). Every well: [[PLEC — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/PLEC.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
