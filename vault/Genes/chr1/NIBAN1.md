---
symbol: "NIBAN1"
type: "gene"
col: 5766
ensembl_id: "ENSG00000135842"
name: "niban apoptosis regulator 1"
location: "1q25.3"
module: 133
arm: "+"
pooled_cpm: 79.8
n_lines_expressing: 39
n_dd_up: 49
n_dd_down: 13
n_dd_up_clean: 43
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 1
direction_downstream: 6
tags: ["gene", "module/133"]
generated_by: "tahoemap"
---

# NIBAN1

*niban apoptosis regulator 1* — 1q25.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 49 drug-doses (6 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 3.84× (z +29.1, q 0e+00, up in 30 of 37 measured lines).
> Pooled over the cell lines (median), lowered significantly by 13 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 0.409× (z -14.7, q 0e+00, down in 32 of 37 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[CEBPG]] (+0.78, fdr 7e-06), [[ADM2]] (+0.71, fdr 7e-06), [[EIF2S2]] (+0.70, fdr 7e-06); moves opposite to [[CYBA]] (-0.46, fdr 1e-04).
> It is in [[Module 133]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[FAM149A]] → it (grade B ⚠); 6 go from it, the strongest it → [[FAM149A]] (grade B ⚠). See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 55 in all, 7 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 49 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 5766.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM |  | **3.84×** | +29.1 | 0e+00 | 30/37 (CFPAC-1, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **3.66×** | +21.3 | 0e+00 | 29/37 (A498, NCI-H2347, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 5 µM |  | **3.17×** | +18.2 | 0e+00 | 31/37 (NCI-H2347, SW 900, …) | rises with dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Bortezomib (drug)]] 0.05 µM |  | **3.05×** | +17.3 | 0e+00 | 36/37 (NCI-H460, LoVo, …) | all doses, flat | cell-cycle shift (explains ~7% here) |
| [[Artesunate (drug)]] 5 µM |  | **2.14×** | +16.7 | 0e+00 | 33/37 (HEC-1-A, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~5% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.63×** | +15.8 | 0e+00 | 35/37 (NCI-H460, SW 900, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[5-Azacytidine (drug)]] 5 µM |  | **2.55×** | +15.3 | 0e+00 | 32/37 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.47×** | +14.8 | 0e+00 | 32/37 (NCI-H460, LoVo, …) | all doses, stronger at high dose |  |
| [[Artesunate (drug)]] 0.5 µM |  | **2.18×** | +12.7 | 2e-35 | 31/37 (HEC-1-A, HCT15, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **2.11×** | +11.8 | 3e-30 | 30/36 (A-172, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.03×** | +11.6 | 1e-29 | 31/37 (NCI-H460, PANC-1, …) | inconsistent across doses |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.67×** | +11.4 | 2e-28 | 32/37 (NCI-H460, NCI-H2030, …) | rises with dose |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **2.00×** | +11.3 | 4e-28 | 32/37 (NCI-H460, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.99×** | +11.3 | 7e-28 | 31/36 (NCI-H460, SW 900, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.52×** | +9.1 | 3e-18 | 25/38 (NCI-H460, MIA PaCa-2, …) | top dose only |  |
| [[Ponatinib (drug)]] 5 µM |  | **1.74×** | +9.1 | 5e-18 | 31/37 (NCI-H460, C-33 A, …) | rises with dose |  |
| [[Neratinib (drug)]] 5 µM |  | **1.67×** | +8.4 | 2e-15 | 26/37 (NCI-H460, hTERT-HPNE, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 3 with an alert ⚠. 13 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 5766.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **0.409×** | -14.7 | 0e+00 | 32/37 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~8% here) |
| [[Belinostat (drug)]] 5 µM |  | **0.448×** | -13.2 | 2e-37 | 28/37 (HT-29, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.500×** | -11.4 | 7e-28 | 29/37 (KATO III, HT-29, …) | rises with dose | cell-cycle shift (explains ~9% here) |
| [[Belinostat (drug)]] 0.5 µM |  | **0.698×** | -5.9 | 4e-07 | 20/37 (KATO III, HT-29, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **0.708×** | -5.5 | 4e-06 | 22/36 (HT-29, SW480, …) | top dose only | cell-cycle shift (explains ~2% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.736×** | -4.7 | 3e-04 | 21/36 (LoVo, SW480, …) | inconsistent across doses | low cells (technical?) |
| [[Filgotinib (drug)]] 5 µM |  | **0.810×** | -3.5 | 0.038 | 12/37 (LoVo, HEC-1-A, …) | top dose only |  |
| [[Berbamine (dihydrochloride) (drug)]] 0.5 µM |  | **0.813×** | -3.4 | 0.041 | 16/37 (HEC-1-A, CFPAC-1, …) | all doses, flat | position effect removed |
| [[Omeprazole (drug)]] 5 µM |  | **0.815×** | -3.4 | 0.044 | 11/37 (NCI-H1573, HEC-1-A, …) | inconsistent across doses | position effect removed |
| [[Phenylephrine (hydrochloride) (drug)]] 5 µM |  | **0.821×** | -3.3 | 0.060 | 15/37 (NCI-H2347, A498, …) | top dose only |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.823×** | -3.2 | 0.060 | 14/38 (KATO III, A-172, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | **0.823×** | -3.2 | 0.060 | 14/37 (LoVo, KATO III, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~33% of this change | **0.830×** | -3.1 | 0.089 | 17/36 (NCI-H460, PANC-1, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.11 per unit of S-phase module lfc, -0.16 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 5766. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 128 | 15 (1 ⚠) | 6 (3 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 3.89× (z +21.1) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.344× (z -12.1) ⚠ toxic · without an alert: [[Panobinostat (drug)]] 5 µM 0.364× (z -11.8) |
| [[HT-29 (line)]] | alt | 147 | 5 | 14 (7 ⚠) | [[Bortezomib (drug)]] 0.05 µM 4.54× (z +12.3) | [[Panobinostat (drug)]] 5 µM 0.0644× (z -23.4) |
| [[LoVo (line)]] | wt | 133 | 7 | 10 (4 ⚠) | [[Bortezomib (drug)]] 0.05 µM 6.60× (z +14.8) | [[Belinostat (drug)]] 5 µM 0.104× (z -18.8) |
| [[A-172 (line)]] | wt | 241 | 13 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 3.45× (z +19.4) | [[Panobinostat (drug)]] 5 µM 0.297× (z -14.4) |
| [[KATO III (line)]] | alt | 185 | 0 | 14 (6 ⚠) | — | [[Panobinostat (drug)]] 5 µM 0.0361× (z -26.4) |
| [[J82 (line)]] | alt | 156 | 10 (2 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.63× (z +23.5) | [[Panobinostat (drug)]] 5 µM 0.304× (z -13.9) |
| [[SW480 (line)]] | alt | 37.4 | 2 | 10 (6 ⚠) | [[Artesunate (drug)]] 5 µM 2.56× (z +10.7) | [[Panobinostat (drug)]] 5 µM 0.154× (z -15.9) |
| [[A-427 (line)]] | wt | 200 | 4 | 7 (5 ⚠) | [[Neratinib (maleate) (drug)]] 0.5 µM 2.17× (z +10.0) | [[Panobinostat (drug)]] 5 µM 0.334× (z -14.3) |
| [[SW 900 (line)]] | alt | 53.2 | 11 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 9.23× (z +20.5) | — |
| [[A498 (line)]] | wt | 239 | 10 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 6.98× (z +24.3) | — |
| [[SNU-423 (line)]] | alt | 89.7 | 7 (1 ⚠) | 3 | [[Homoharringtonine (drug)]] 5 µM 4.51× (z +17.6) | [[Belinostat (drug)]] 5 µM 0.267× (z -11.8) |
| [[HEC-1-A (line)]] | alt | 105 | 9 (2 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.29× (z +18.8) | — |
| [[NCI-H2030 (line)]] | alt | 51.3 | 9 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.85× (z +18.5) | — |
| [[HOP62 (line)]] | alt | 25.4 | 8 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 22.5× (z +25.0) | — |
| [[MIA PaCa-2 (line)]] | alt | 30.2 | 8 | 0 | [[Homoharringtonine (drug)]] 0.5 µM 17.1× (z +14.8) | — |
| [[H4 (line)]] | wt | 226 | 2 | 5 (2 ⚠) | [[Ixazomib citrate (drug)]] 5 µM 3.85× (z +10.8) | [[Belinostat (drug)]] 5 µM 0.193× (z -13.2) |
| [[hTERT-HPNE (line)]] | wt | 75.2 | 7 | 0 | [[Homoharringtonine (drug)]] 5 µM 9.30× (z +18.7) | — |
| [[PANC-1 (line)]] | alt | 28.0 | 7 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.90× (z +14.4) | — |
| [[NCI-H1792 (line)]] | alt | 118 | 5 | 1 | [[Homoharringtonine (drug)]] 5 µM 3.06× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.351× (z -10.6) |
| [[NCI-H2347 (line)]] | alt | 105 | 4 | 2 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 6.40× (z +25.2) | [[Panobinostat (drug)]] 5 µM 0.409× (z -9.3) |
| [[AsPC-1 (line)]] | alt | 45.4 | 5 (1 ⚠) | 0 | [[Bortezomib (drug)]] 0.05 µM 9.54× (z +12.8) | — |
| [[C-33 A (line)]] | alt | 37.8 | 5 | 0 | [[5-Azacytidine (drug)]] 5 µM 8.08× (z +12.4) | — |
| [[HS-578T (line)]] | alt | 62.9 | 4 | 1 | [[Harringtonine (drug)]] 0.5 µM 6.79× (z +14.8) | [[Panobinostat (drug)]] 5 µM 0.295× (z -9.5) |
| [[C32 (line)]] | wt | 40.9 | 4 | 0 | [[Ixazomib citrate (drug)]] 5 µM 9.44× (z +12.0) | — |
| [[CFPAC-1 (line)]] | alt | 57.8 | 4 | 0 | [[Homoharringtonine (drug)]] 5 µM 19.4× (z +26.2) | — |
| [[NCI-H23 (line)]] | alt | 47.5 | 4 | 0 | [[Bortezomib (drug)]] 0.05 µM 6.47× (z +11.9) | — |
| [[HCT15 (line)]] | alt | 56.3 | 3 | 0 | [[Artesunate (drug)]] 5 µM 4.90× (z +12.0) | — |
| [[Panc 03.27 (line)]] | alt | 28.4 | 3 | 0 | [[Homoharringtonine (drug)]] 5 µM 30.1× (z +25.2) | — |
| [[Hs 766T (line)]] | wt | 21.2 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 11.1× (z +18.0) | — |
| [[LOX-IMVI (line)]] | wt | 75.2 | 0 | 2 | — | [[Panobinostat (drug)]] 5 µM 0.313× (z -10.7) |
| [[NCI-H1573 (line)]] | alt | 92.5 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.24× (z +15.4) | — |
| [[RPMI-7951 (line)]] | alt | 69.6 | 2 | 0 | [[Harringtonine (drug)]] 5 µM 8.07× (z +13.7) | — |
| [[SW48 (line)]] | wt | 46.9 | 2 | 0 | [[Artesunate (drug)]] 5 µM 4.02× (z +9.1) | — |
| [[CHP-212 (line)]] | wt | 54.3 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0820× (z -9.5) |
| [[SW 1271 (line)]] | alt | 97.3 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 5.32× (z +8.5) | — |
| [[A549 (line)]] | wt | 14.9 n.m. | — | — | — | — |
| [[AN3 CA (line)]] | alt | 11.9 n.m. | — | — | — | — |
| [[BT-474 (line)]] | alt | 12.5 n.m. | — | — | — | — |
| [[COLO 205 (line)]] | alt | 6.32 n.m. | — | — | — | — |
| [[HepG2_C3A (line)]] | wt | 6.82 n.m. | — | — | — | — |
| [[LS 180 (line)]] | wt | 19.3 n.m. | — | — | — | — |
| [[NCI-H2122 (line)]] | alt | 62.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 67.3 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 132 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 6.49 n.m. | — | — | — | — |
| [[SHP-77 (line)]] | alt | 5.48 n.m. | — | — | — | — |
| [[SK-MEL-2 (line)]] | alt | 8.11 n.m. | — | — | — | — |
| [[SNU-1 (line)]] | wt | 7.47 n.m. | — | — | — | — |
| [[SW 1088 (line)]] | alt | 41.3 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 8.77 n.m. | — | — | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 5766), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPG]] | +0.78 | +0.76 / +0.73 | both halves | 7e-06 | **novel candidate** |
| [[ADM2]] | +0.71 | +0.64 / +0.72 | both halves | 7e-06 | **novel candidate** |
| [[EIF2S2]] | +0.70 | +0.71 / +0.62 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[YARS1]] | +0.70 | +0.63 / +0.72 | both halves | 7e-06 |  |
| [[DMGDH]] | +0.69 | +0.65 / +0.69 | both halves | 7e-06 | **novel candidate** |
| [[XPOT]] | +0.67 | +0.61 / +0.70 | both halves | 7e-06 |  |
| [[LURAP1L-AS1]] | +0.67 | +0.63 / +0.61 | both halves | 7e-06 |  |
| [[SLC7A11]] | +0.65 | +0.60 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[HSPA9]] | +0.65 | +0.62 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[TARS1]] | +0.65 | +0.60 / +0.62 | both halves | 7e-06 |  |
| [[SLC3A2]] | +0.64 | +0.64 / +0.58 | both halves | 8e-06 |  |
| [[PCK2]] | +0.64 | +0.61 / +0.60 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CYBA]] | -0.46 | -0.53 / -0.34 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM149A]] | B | FAM149A activity raises NIBAN1's level | lines that do not express FAM149A (25) vs lines expressing it (25) | 2.44× lower at baseline in the lines without FAM149A | 0.040 | ⚠ within organs, on part of the lines; also absent: SKAP1, ENSG00000286133, CSRNP3 |

### Downstream of this gene

*6 arrows, 6 of them with an alert ⚠; grade A 0, B 6, C 0.*

| Target | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[FAM149A]] | B | NIBAN1 activity raises FAM149A's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 2.51× lower at baseline in the lines without NIBAN1 | 0.028 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[ERICH2]] | B | NIBAN1 activity raises ERICH2's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.61× lower at baseline in the lines without NIBAN1 | 0.030 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[MTO1]] | B | NIBAN1 activity raises MTO1's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.21× lower at baseline in the lines without NIBAN1 | 0.056 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| cells under [[Ixazomib (drug)]] 5 µM | B | NIBAN1 activity lowers the cells' numbers under Ixazomib 5 µM (makes them more sensitive) | lines that do not express NIBAN1 (11) vs lines expressing it (37) | the lines without NIBAN1: 1.34× the cells of the other lines | 0.091 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[ULBP1]] | B | NIBAN1 activity raises ULBP1's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.74× lower at baseline in the lines without NIBAN1 | 0.094 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |
| [[SLC6A9]] | B | NIBAN1 activity raises SLC6A9's level | lines that do not express NIBAN1 (11) vs lines expressing it (39) | 1.16× lower at baseline in the lines without NIBAN1 | 0.097 | ⚠ within organs, on part of the lines; also absent: CAV1, FGF2, PCOLCE2 |

## Where it sits

- **Module**: [[Module 133]]; 36 genes; every member is in the + arm (projection on the module's main direction 0.793). A single-armed module: all its genes lie on one side of its main direction.
- **Nodal map** (x, y) = (-15.7, 47.6); signed map (-12.5, 23.0). **Vector** length 146, 46.7% of its response variance represented; |z| ≥ 3 in 1,617 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Bortezomib (drug)]] 0.05 µM |  | +10.4 | +17.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.9 | +15.3 |
|  | [[Artesunate (drug)]] 5 µM |  | +8.6 | +16.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +8.5 | +9.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | +8.5 | +15.8 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +7.8 | +14.8 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +7.5 | +11.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +6.3 | +9.1 |
| fall | [[Panobinostat (drug)]] 0.5 µM |  | -5.0 | -11.4 |
|  | [[Belinostat (drug)]] 5 µM |  | -4.8 | -13.2 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~42% of this change | -4.7 | -3.2 |
|  | [[Panobinostat (drug)]] 5 µM |  | -4.6 | -14.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | -3.7 | -5.5 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -3.5 | -4.7 |
|  | [[PH-797804 (drug)]] 5 µM |  | -3.3 | -1.6 |
|  | [[Filgotinib (drug)]] 5 µM |  | -2.5 | -3.5 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | -2.3 | -1.6 |
|  | [[Triamcinolone (drug)]] 0.5 µM |  | -2.2 | -2.6 |

## What is on record

|  |  |
|---|---|
| Name | niban apoptosis regulator 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1q25.3 — chr1:184,790,724-184,974,508 (-) |
| Ensembl biotype | protein_coding |
| Also known as | NIBAN, GIG39; previously C1orf24, FAM129A |
| Hallmark sets | CHOLESTEROL_HOMEOSTASIS, MTORC1_SIGNALING |
| Matched by | ensembl_id |

**Function**, from UniProt [Q9BZQ8](https://www.uniprot.org/uniprotkb/Q9BZQ8) (Protein Niban 1):

> Regulates phosphorylation of a number of proteins involved in translation regulation including EIF2A, EIF4EBP1 and RPS6KB1. May be involved in the endoplasmic reticulum stress response (By similarity).

**Summary**, from NCBI Gene [116496](https://www.ncbi.nlm.nih.gov/gene/116496):

> This gene encodes a member of the family with sequence similarity 129 protein family. This gene is highly expressed in several cancer cells and may serve as a prognostic marker for certain cancers. The encoded protein may play a role in regulating p53-mediated apoptosis. [provided by RefSeq, Sep 2016]

**Accessions** — [HGNC:16784](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:16784) · Entrez [116496](https://www.ncbi.nlm.nih.gov/gene/116496) · UniProt [Q9BZQ8](https://www.uniprot.org/uniprotkb/Q9BZQ8) · Ensembl [ENSG00000135842](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000135842)

## Data

Gene col 5766: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 5766); `tables/drug_effects.parquet` (68 rows, flagged included); `relations/gene_relations.parquet` (col_a == 5766, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 5766]; `tensor/DDL_lfc|DDL_z.npy` [5766]; `embed/gene_vectors.npy` [5766]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 5766 or target_col == 5766). Every well: [[NIBAN1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NIBAN1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
