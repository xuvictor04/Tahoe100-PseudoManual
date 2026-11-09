---
symbol: "SESN2"
type: "gene"
col: 5121
ensembl_id: "ENSG00000130766"
name: "sestrin 2"
location: "1p35.3"
module: 63
arm: "+"
pooled_cpm: 57.55
n_lines_expressing: 50
n_dd_up: 48
n_dd_down: 9
n_dd_up_clean: 43
n_dd_down_clean: 6
in_vector_space: true
direction_upstream: 5
direction_downstream: 1
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# SESN2

*sestrin 2* — 1p35.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 48 drug-doses (5 with an alert ⚠); the strongest is [[Auranofin (drug)]] 5 µM: 3.08× (z +10.9, q 1e-24, up in 46 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 9 drug-doses (3 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 5 µM: 0.250× (z -12.9, q 3e-35, down in 34 of 38 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Harringtonine (drug)]] 0.5 µM: 0.459× (z -6.8, q 2e-09, down in 28 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[GARS1]] (+0.84, fdr 7e-06), [[TRIB3]] (+0.84, fdr 7e-06), [[CHAC1]] (+0.83, fdr 7e-06); moves opposite to [[NHLRC2]] (-0.54, fdr 4e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 5 arrows point to it, the strongest [[ASNSP1]] → it (grade B ⚠); 1 goes from it, the strongest it → [[HSPA9]] (grade C ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 48 in all, 5 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 48 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5121.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Auranofin (drug)]] 5 µM |  | **3.08×** | +10.9 | 1e-24 | 46/48 (LoVo, SW480, …) | top dose only |  |
| [[Artesunate (drug)]] 5 µM |  | **2.12×** | +10.1 | 2e-21 | 43/48 (SW480, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.34×** | +8.2 | 4e-14 | 41/48 (C-33 A, SW480, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.32×** | +8.1 | 5e-14 | 41/48 (LOX-IMVI, SW 900, …) | inconsistent across doses |  |
| [[Panobinostat (drug)]] 5 µM |  | **2.13×** | +7.3 | 3e-11 | 36/48 (SW480, SW48, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.04×** | +6.9 | 6e-10 | 38/48 (LoVo, C-33 A, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Artesunate (drug)]] 0.5 µM |  | **2.02×** | +6.8 | 8e-10 | 40/48 (SW480, HEC-1-A, …) | rises with dose |  |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.64×** | +6.7 | 2e-09 | 31/47 (LoVo, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~14% here) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.62×** | +6.6 | 3e-09 | 35/48 (C-33 A, LoVo, …) | rises with dose |  |
| [[Vinblastine (sulfate) (drug)]] 5 µM |  | **1.63×** | +6.5 | 3e-09 | 39/48 (COLO 205, KATO III, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **1.88×** | +5.7 | 5e-07 | 36/48 (LoVo, SW480, …) | all doses, flat | cell-cycle shift (explains ~11% here) |
| [[Belinostat (drug)]] 5 µM |  | **1.78×** | +5.6 | 1e-06 | 32/48 (SW480, SHP-77, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **1.71×** | +5.2 | 1e-05 | 34/48 (SW480, AsPC-1, …) | rises with dose | cell-cycle shift (explains ~19% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **1.66×** | +4.9 | 4e-05 | 30/48 (LoVo, RKO, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.65×** | +4.8 | 5e-05 | 34/47 (Hs 766T, NCI-H23, …) | rises with dose |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.59×** | +4.8 | 5e-05 | 33/48 (LOX-IMVI, LoVo, …) | rises with dose | noisy plate (z scaled) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 9 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5121.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.250×** | -12.9 | 3e-35 | 34/38 (SW1417, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.378×** | -8.5 | 7e-15 | 40/46 (PANC-1, A-427, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.442×** | -7.3 | 6e-11 | 27/44 (A-427, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.459×** | -6.8 | 2e-09 | 28/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~5% here) |
| [[Harringtonine (drug)]] 5 µM |  | **0.582×** | -5.0 | 5e-05 | 31/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~20% here); composition shift |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.572×** | -5.0 | 5e-05 | 31/47 (A-427, HS-578T, …) | all doses, flat | low cells (technical?) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.863× | -5.0 | 5e-05 | 13/49 (MIA PaCa-2, NCI-H23, …) | inconsistent across doses |  |
| [[Filgotinib (drug)]] 5 µM |  | **0.683×** | -3.7 | 0.016 | 24/48 (NCI-H2347, SW48, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.692×** | -3.6 | 0.023 | 22/47 (H4, AN3 CA, …) | inconsistent across doses | cell-cycle shift (explains ~10% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.716×** | -3.2 | 0.069 | 23/48 (PANC-1, HS-578T, …) | inconsistent across doses | cell-cycle shift (explains ~6% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | 0.690× | -3.1 | 0.10 | 18/48 (NCI-H2347, A-172, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.27 per unit of S-phase module lfc, -0.30 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5121. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 148 | 0 | 12 (7 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.133× (z -21.5) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.0769× (z -19.7) |
| [[A-427 (line)]] | wt | 141 | 0 | 10 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0521× (z -21.5) ⚠ toxic; transcription drop · without an alert: [[Homoharringtonine (drug)]] 0.5 µM 0.104× (z -17.9) |
| [[SW480 (line)]] | alt | 27.9 | 8 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 5.57× (z +14.3) | [[Dinaciclib (drug)]] 0.05 µM 0.173× (z -13.5) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 83.2 | 0 | 7 (5 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.167× (z -13.5) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.194× (z -12.4) |
| [[NCI-H23 (line)]] | alt | 82.8 | 0 | 4 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.218× (z -11.1) ⚠ cell-cycle shift, explains ~0% of this change |
| [[NCI-H2347 (line)]] | alt | 59.4 | 0 | 4 (4 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0898× (z -16.4) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 149 | 2 | 2 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.67× (z +12.1) | [[Dinaciclib (drug)]] 5 µM 0.0739× (z -14.1) ⚠ toxic; transcription drop |
| [[AsPC-1 (line)]] | alt | 28.7 | 3 (1 ⚠) | 0 | [[Niclosamide (olamine) (drug)]] 5 µM 6.74× (z +9.6) ⚠ toxic · without an alert: [[Auranofin (drug)]] 5 µM 5.37× (z +8.8) | — |
| [[H4 (line)]] | wt | 119 | 0 | 3 (3 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.153× (z -16.0) ⚠ cell-cycle shift, explains ~0% of this change |
| [[HS-578T (line)]] | alt | 125 | 0 | 3 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.152× (z -12.0) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.05 µM 0.242× (z -8.7) |
| [[LoVo (line)]] | wt | 58.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 7.97× (z +14.8) | — |
| [[MIA PaCa-2 (line)]] | alt | 99.3 | 1 | 2 (2 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.01× (z +9.7) | [[Adagrasib (drug)]] 0.05 µM 0.542× (z -10.6) ⚠ position not correctable |
| [[A498 (line)]] | wt | 79.1 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.164× (z -11.4) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 26.1 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.42× (z +9.2) | [[Dinaciclib (drug)]] 5 µM 0.129× (z -10.6) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 38.8 | 2 | 0 | [[5-Azacytidine (drug)]] 5 µM 10.4× (z +11.6) | — |
| [[KATO III (line)]] | alt | 60.7 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.228× (z -10.1) |
| [[SW1417 (line)]] | alt | 45.9 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0293× (z -22.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 43.9 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.308× (z -9.9) ⚠ cell-cycle shift, explains ~0% of this change |
| [[BT-474 (line)]] | alt | 31.6 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.66× (z +9.4) | — |
| [[C32 (line)]] | wt | 32.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.90× (z +9.9) | — |
| [[CFPAC-1 (line)]] | alt | 57.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.0891× (z -11.3) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 25.2 | 1 | 0 | [[Vinblastine (sulfate) (drug)]] 5 µM 3.79× (z +8.6) | — |
| [[HCT15 (line)]] | alt | 55.4 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.26× (z +8.7) | — |
| [[HEC-1-A (line)]] | alt | 28.5 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.87× (z +8.5) | — |
| [[HOP62 (line)]] | alt | 22.3 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.38× (z +9.1) | — |
| [[Hs 766T (line)]] | wt | 32.2 | 1 | 0 | [[Chlorhexidine (diacetate) (drug)]] 5 µM 4.97× (z +10.3) | — |
| [[hTERT-HPNE (line)]] | wt | 43.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.137× (z -10.2) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 36.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.205× (z -8.7) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 29.5 | 1 | 0 | [[Auranofin (drug)]] 5 µM 6.88× (z +10.4) | — |
| [[NCI-H661 (line)]] | alt | 96.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.107× (z -8.5) ⚠ toxic; transcription drop |
| [[RKO (line)]] | wt | 94.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0948× (z -12.9) ⚠ toxic; transcription drop |
| [[RPMI-7951 (line)]] | alt | 51.8 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.154× (z -9.7) ⚠ toxic; transcription drop |
| [[SHP-77 (line)]] | alt | 15.7 | 1 | 0 | [[Auranofin (drug)]] 5 µM 7.84× (z +9.7) | — |
| [[SNU-423 (line)]] | alt | 55.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.138× (z -11.3) ⚠ toxic; transcription drop |
| [[SW 900 (line)]] | alt | 29.4 | 1 | 0 | [[Auranofin (drug)]] 5 µM 5.41× (z +9.0) | — |
| [[SW48 (line)]] | wt | 79.4 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.77× (z +9.5) | — |
| [[AN3 CA (line)]] | alt | 30.9 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 48.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 63.5 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 49.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 45.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 43.3 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 49.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 49.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 28.1 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 45.0 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 37.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5121), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GARS1]] | +0.84 | +0.82 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[TRIB3]] | +0.84 | +0.81 / +0.82 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 564 |
| [[CHAC1]] | +0.83 | +0.76 / +0.84 | both halves | 7e-06 | STRING 608 |
| [[SARS1]] | +0.83 | +0.81 / +0.82 | both halves | 7e-06 | **novel candidate** |
| [[GOT1]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CARS1]] | +0.80 | +0.76 / +0.81 | both halves | 7e-06 |  |
| [[ASNS]] | +0.77 | +0.79 / +0.77 | both halves | 7e-06 | pathway: Cellular response to starvation; STRING 467 |
| [[EIF2S2]] | +0.76 | +0.72 / +0.78 | both halves | 7e-06 | pathway: Cellular response to starvation |
| [[AARS1]] | +0.76 | +0.79 / +0.75 | both halves | 7e-06 |  |
| [[MARS1]] | +0.73 | +0.75 / +0.70 | both halves | 7e-06 |  |
| [[SLC1A4]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 |  |
| [[GPT2]] | +0.73 | +0.66 / +0.74 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NHLRC2]] | -0.54 | -0.41 / -0.54 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*5 arrows, 5 of them with an alert ⚠; grade A 0, B 4, C 1.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ASNSP1]] | B | ASNSP1 activity raises SESN2's level | lines that do not express ASNSP1 (35) vs lines expressing it (15) | 1.63× lower at baseline in the lines without ASNSP1 | 0.022 | ⚠ within organs, on part of the lines; co-occurs with TP53; also absent: ZNF208, GCG, GPR15 |
| [[ANK2]] | B | ANK2 activity raises SESN2's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.42× lower at baseline in the lines without ANK2 | 0.048 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |
| [[PSAT1]] | B | PSAT1 activity raises SESN2's level | lines that do not express PSAT1 (8) vs lines expressing it (42) | 1.61× lower at baseline in the lines without PSAT1 | 0.067 | ⚠ within organs, on part of the lines; also absent: SLC1A4, ACBD7; maybe low, not absent |
| [[DMGDH]] | B | DMGDH activity raises SESN2's level | lines that do not express DMGDH (8) vs lines expressing it (42) | 1.68× lower at baseline in the lines without DMGDH | 0.073 | ⚠ within organs, on part of the lines; maybe low, not absent |
| [[MORC4]] | C | MORC4 activity lowers SESN2's level | lines that do not express MORC4 (3) vs lines expressing it (47) | 2.72× higher at baseline in the lines without MORC4 | 0.053 | ⚠ few lines (3 vs 47); across organs; also absent: USP53, OSBPL10, TESK2; maybe low, not absent |

### Downstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 0, C 1.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HSPA9]] | C | SESN2's natural level weakens HSPA9's drug response | SESN2's natural level across 49 lines (lineage-adjusted; a glimpse) | r -0.65, reverse +0.07; direction not clear | 0.044 | ⚠ tissue can mimic it; precision caveat; direction unclear |

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.842). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.2, 48.7); signed map (-12.7, 24.9). **Vector** length 160, 59.0% of its response variance represented; |z| ≥ 3 in 1,463 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *mTORC1 signaling* (hallmark, mean cos +0.63 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.72 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.72 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +10.2 | +10.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +9.6 | +10.9 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.7 | +8.2 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +8.1 | +6.9 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +8.0 | +6.6 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.8 | +6.8 |
|  | [[Neratinib (drug)]] 5 µM |  | +6.6 | +4.0 |
| fall | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -8.4 | -3.2 |
|  | [[Harringtonine (drug)]] 5 µM |  | -8.1 | -5.0 |
|  | [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~38% of this change | -7.9 | -1.2 |
|  | [[Harringtonine (drug)]] 0.5 µM |  | -7.6 | -6.8 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift | -7.5 | -1.9 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.1 | -5.0 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -4.1 | -2.8 |
|  | [[Filgotinib (drug)]] 5 µM |  | -3.2 | -3.7 |
|  | [[Arbutin (drug)]] 0.05 µM |  | -3.1 | -1.6 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -3.0 | -1.4 |

## What is on record

|  |  |
|---|---|
| Name | sestrin 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p35.3 — chr1:28,259,518-28,282,491 (+) |
| Ensembl biotype | protein_coding |
| Also known as | SES2, DKFZp761M0212, HI95, SEST2 |
| Gene groups (HGNC) | Sestrin family |
| Reactome | 8 pathways, smallest: Amino acids regulate mTORC1; TP53 Regulates Metabolic Genes; KEAP1-NFE2L2 pathway |
| Matched by | ensembl_id |

**Function**, from UniProt [P58004](https://www.uniprot.org/uniprotkb/P58004) (Sestrin-2):

> Functions as an intracellular leucine sensor that negatively regulates the mTORC1 signaling pathway through the GATOR complex. In absence of leucine, binds the GATOR subcomplex GATOR2 and prevents mTORC1 signaling. Binding of leucine to SESN2 disrupts its interaction with GATOR2 thereby activating the TORC1 signaling pathway. This stress-inducible metabolic regulator also plays a role in protection against oxidative and genotoxic stresses. May negatively regulate protein translation in response …

**Summary**, from NCBI Gene [83667](https://www.ncbi.nlm.nih.gov/gene/83667):

> This gene encodes a member of the sestrin family of PA26-related proteins. The encoded protein may function in the regulation of cell growth and survival. This protein may be involved in cellular response to different stress conditions. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:20746](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20746) · Entrez [83667](https://www.ncbi.nlm.nih.gov/gene/83667) · UniProt [P58004](https://www.uniprot.org/uniprotkb/P58004) · Ensembl [ENSG00000130766](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000130766)

## Data

Gene col 5121: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5121); `tables/drug_effects.parquet` (59 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5121, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5121]; `tensor/DDL_lfc|DDL_z.npy` [5121]; `embed/gene_vectors.npy` [5121]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5121 or target_col == 5121). Every well: [[SESN2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/SESN2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
