---
symbol: "EAF2"
type: "gene"
col: 6956
ensembl_id: "ENSG00000145088"
name: "ELL associated factor 2"
location: "3q13.33"
module: 56
arm: "+"
pooled_cpm: 15.0
n_lines_expressing: 50
n_dd_up: 18
n_dd_down: 22
n_dd_up_clean: 16
n_dd_down_clean: 19
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/056"]
generated_by: "tahoemap"
---

# EAF2

*ELL associated factor 2* — 3q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 18 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 3.09× (z +12.4, q 2e-32, up in 40 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 22 drug-doses (3 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.648× (z -4.8, q 6e-04, down in 25 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC15A2]] (+0.92, fdr 7e-06, ⚠ same locus), [[SRP54]] (+0.78, fdr 7e-06), [[DNAJC25]] (+0.78, fdr 7e-06), [[TMEM263]] (+0.77, fdr 7e-06); moves opposite to [[TULP4]] (-0.59, fdr 1e-05), [[TMEM33]] (-0.58, fdr 1e-05).
> It is in [[Module 056]], a single-armed module (Asparagine N-linked glycosylation).
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[MCTP2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 18 in all, 2 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 18 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6956.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **3.09×** | +12.4 | 2e-32 | 40/48 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Homoharringtonine (drug)]] 5 µM |  | **2.05×** | +10.9 | 3e-25 | 29/46 (AsPC-1, LOX-IMVI, …) | top dose only | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.62×** | +10.6 | 8e-24 | 37/47 (A-427, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.56×** | +10.3 | 1e-22 | 35/48 (A-427, PANC-1, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.86×** | +9.4 | 5e-19 | 31/44 (J82, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~12% here) |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.80×** | +6.4 | 1e-08 | 31/48 (A-427, SW1417, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.73×** | +5.7 | 7e-07 | 26/43 (Panc 03.27, A-427, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~29% of this change | **1.59×** | +4.9 | 7e-05 | 18/38 (MIA PaCa-2, J82, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.55×** | +4.6 | 3e-04 | 23/42 (A-172, Panc 03.27, …) | top dose only | cell-cycle shift (explains ~24% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **1.30×** | +4.1 | 0.003 | 18/47 (SW1417, RKO, …) | rises with dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.44×** | +4.0 | 0.003 | 20/48 (HOP62, A-172, …) | top dose only |  |
| [[Terfenadine (drug)]] 5 µM |  | **1.30×** | +3.9 | 0.004 | 15/47 (Hs 766T, HS-578T, …) | rises with dose |  |
| [[Fluvoxamine (maleate) (drug)]] 0.5 µM |  | **1.38×** | +3.5 | 0.020 | 18/45 (A498, H4, …) | two highest doses |  |
| [[HI-TOPK-032 (drug)]] 5 µM |  | **1.82×** | +3.4 | 0.023 | 9/42 (PANC-1, SW480, …) | top dose only | noisy plate (z scaled) |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~28% of this change | **1.35×** | +3.3 | 0.042 | 16/46 (J82, PANC-1, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.35×** | +3.2 | 0.042 | 17/43 (SK-MEL-2, SHP-77, …) | rises with dose | cell-cycle shift (explains ~11% here) |
| [[Vilanterol (drug)]] 5 µM |  | **1.24×** | +3.2 | 0.048 | 10/47 (NCI-H2347, NCI-H1792, …) | top dose only |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 23 in all, 4 with an alert ⚠; shown: the 15 strongest and the 2 next strongest without an alert. 22 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 6956.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.648×** | -4.8 | 6e-04 | 25/48 (SW480, KATO III, …) | all doses, flat | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.629×** | -4.7 | 6e-04 | 21/31 (BT-474, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.580×** | -4.4 | 0.002 | 21/46 (A498, RPMI-7951, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.603×** | -4.1 | 0.005 | 16/48 (A498, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | **0.768×** | -4.0 | 0.006 | 21/48 (HEC-1-A, HT-29, …) | inconsistent across doses |  |
| [[Busulfan (drug)]] 0.05 µM |  | **0.613×** | -4.0 | 0.006 | 18/48 (LS 180, HT-29, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Megestrol (drug)]] 0.05 µM |  | **0.620×** | -3.9 | 0.007 | 17/48 (HT-29, A498, …) | inconsistent across doses | cell-cycle shift (explains ~2% here); noisy plate (z scaled) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 0.909× | -3.8 | 0.009 | 5/48 (NCI-H2030, AN3 CA, …) | inconsistent across doses |  |
| [[Palmatine (chloride) (drug)]] 0.05 µM |  | **0.636×** | -3.7 | 0.013 | 13/48 (LS 180, KATO III, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.697×** | -3.7 | 0.013 | 15/43 (H4, A549, …) | inconsistent across doses | low cells (technical?) |
| [[Berbamine (drug)]] 0.05 µM |  | **0.643×** | -3.6 | 0.016 | 20/48 (LS 180, Hs 766T, …) | inconsistent across doses | noisy plate (z scaled) |
| [[5-Azacytidine (drug)]] 5 µM |  | **0.723×** | -3.6 | 0.016 | 11/47 (HepG2/C3A, SW 1271, …) | top dose only |  |
| [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | **0.647×** | -3.6 | 0.016 | 16/48 (HT-29, LS 180, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.656×** | -3.4 | 0.023 | 12/48 (HCT15, LOX-IMVI, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Demeclocycline (drug)]] 5 µM |  | **0.800×** | -3.4 | 0.025 | 10/47 (MIA PaCa-2, PANC-1, …) | top dose only |  |
| [[Thymol (drug)]] 5 µM |  | **0.800×** | -3.4 | 0.025 | 21/47 (Panc 03.27, MIA PaCa-2, …) | top dose only |  |
| [[Allantoin (drug)]] 5 µM |  | **0.798×** | -3.4 | 0.025 | 11/48 (CFPAC-1, LS 180, …) | top dose only |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.30 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6956. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HCT15 (line)]] | alt | 38.8 | 0 | 4 (3 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0901× (z -10.9) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.101× (z -10.8) |
| [[KATO III (line)]] | alt | 39.7 | 0 | 4 (3 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.195× (z -11.2) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 5 µM 0.267× (z -8.7) |
| [[A-427 (line)]] | wt | 18.6 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 7.85× (z +12.9) | — |
| [[H4 (line)]] | wt | 23.4 | 0 | 3 (1 ⚠) | — | [[Harringtonine (drug)]] 0.05 µM 0.0481× (z -11.7) |
| [[PANC-1 (line)]] | alt | 10.7 | 3 | 0 | [[Panobinostat (drug)]] 5 µM 4.83× (z +9.2) | — |
| [[J82 (line)]] | alt | 10.1 | 2 (1 ⚠) | 0 | [[Selinexor (drug)]] 5 µM 4.80× (z +10.4) ⚠ cell-cycle shift, explains ~40% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.58× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 19.4 | 2 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.73× (z +9.7) | — |
| [[AsPC-1 (line)]] | alt | 14.6 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.23× (z +10.4) | — |
| [[BT-474 (line)]] | alt | 34.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0770× (z -11.4) ⚠ toxic; transcription drop |
| [[C32 (line)]] | wt | 5.71 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 7.42× (z +8.7) | — |
| [[CFPAC-1 (line)]] | alt | 24.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 3.34× (z +10.2) | — |
| [[HEC-1-A (line)]] | alt | 15.6 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.143× (z -9.7) ⚠ toxic; transcription drop |
| [[HT-29 (line)]] | alt | 32.2 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.120× (z -11.0) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 7.77 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.06× (z +10.2) | — |
| [[LS 180 (line)]] | wt | 21.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.0953× (z -10.3) ⚠ toxic; transcription drop |
| [[NCI-H2030 (line)]] | alt | 5.42 | 0 | 1 | — | [[Fenofibrate (drug)]] 5 µM 0.0808× (z -10.0) |
| [[NCI-H23 (line)]] | alt | 15.3 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 6.07× (z +9.2) | — |
| [[NCI-H460 (line)]] | wt | 4.17 | 0 | 1 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.109× (z -9.2) |
| [[Panc 03.27 (line)]] | alt | 15.1 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 4.19× (z +8.8) | — |
| [[SHP-77 (line)]] | alt | 10.2 | 0 | 1 | — | [[Bendamustine (drug)]] 5 µM 0.139× (z -8.7) |
| [[SK-MEL-2 (line)]] | alt | 7.12 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 6.11× (z +9.3) | — |
| [[SNU-423 (line)]] | alt | 7.50 | 0 | 1 | — | [[Doxycycline (monohydrate) (drug)]] 0.5 µM 0.0567× (z -10.9) |
| [[SW480 (line)]] | alt | 17.0 | 1 | 0 | [[Homoharringtonine (drug)]] 5 µM 2.53× (z +9.5) | — |
| [[A-172 (line)]] | wt | 7.57 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 19.3 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 8.50 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 5.47 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.28 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 40.1 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.8 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 7.55 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 10.8 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 29.5 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 17.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 16.5 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 17.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.48 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 18.4 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 9.37 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 22.4 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 17.2 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 5.97 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6956), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC15A2]] | +0.92 | +0.93 / +0.92 | both halves | 7e-06 | ⚠ same locus (7.9 kb, same strand: neighbours can correlate without regulation) |
| [[SRP54]] | +0.78 | +0.70 / +0.72 | both halves | 7e-06 |  |
| [[DNAJC25]] | +0.78 | +0.72 / +0.76 | both halves | 7e-06 |  |
| [[TMEM263]] | +0.77 | +0.64 / +0.69 | both halves | 7e-06 |  |
| [[COG6]] | +0.77 | +0.62 / +0.78 | both halves | 7e-06 |  |
| [[GOLPH3L]] | +0.73 | +0.67 / +0.72 | both halves | 7e-06 |  |
| [[PGM3]] | +0.73 | +0.67 / +0.68 | both halves | 7e-06 |  |
| [[EIF2AK3]] | +0.72 | +0.62 / +0.71 | both halves | 7e-06 |  |
| [[MCEE]] | +0.72 | +0.62 / +0.75 | both halves | 7e-06 |  |
| [[SERP1]] | +0.71 | +0.67 / +0.67 | both halves | 7e-06 |  |
| [[GMPPA]] | +0.70 | +0.57 / +0.68 | both halves | 1e-05 |  |
| [[ACBD3]] | +0.70 | +0.57 / +0.67 | both halves | 1e-05 |  |
| [[SSR2]] | +0.68 | +0.51 / +0.66 | both halves | 1e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[TULP4]] | -0.59 | -0.52 / -0.52 | both halves | 1e-05 |  |
| [[TMEM33]] | -0.58 | -0.60 / -0.50 | both halves | 1e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[MCTP2]] | B | MCTP2 activity raises EAF2's level | lines that do not express MCTP2 (20) vs lines expressing it (30) | 1.62× lower at baseline in the lines without MCTP2 | 0.035 | ⚠ within organs, on part of the lines; also absent: ENSG00000227486, ENSG00000284644, MPZL3 |
| [[GALNT3]] | B | GALNT3 activity raises EAF2's level | lines that do not express GALNT3 (30) vs lines expressing it (20) | 1.76× lower at baseline in the lines without GALNT3 | 0.058 | ⚠ within organs, on part of the lines; also absent: TMEM125, GRHL2, SKAP1 |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 056]] — Asparagine N-linked glycosylation; 87 genes; every member is in the + arm (projection on the module's main direction 0.772). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (12.0, -35.3); signed map (-50.8, 12.5). **Vector** length 110, 28.5% of its response variance represented; |z| ≥ 3 in 1,085 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Asparagine N-linked glycosylation* (reactome, mean cos +0.61 to 23); *ER to Golgi Anterograde Transport* (reactome, mean cos +0.62 to 16); *Transport to the Golgi and subsequent modification* (reactome, mean cos +0.62 to 16).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Terfenadine (drug)]] 5 µM |  | +3.2 | +3.9 |
|  | [[Homoharringtonine (drug)]] 5 µM |  | +3.2 | +10.9 |
|  | [[Vilanterol (drug)]] 5 µM |  | +2.2 | +3.2 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | +2.2 | +3.4 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | +2.1 | +4.0 |
|  | [[Docetaxel (Trihydrate) (drug)]] 0.5 µM |  | +2.1 | +2.3 |
| fall | [[Homoharringtonine (drug)]] 0.05 µM |  | -5.1 | -4.4 |
|  | [[Belumosudil (drug)]] 5 µM |  | -3.7 | -3.2 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -3.5 | -3.4 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -3.5 | -4.7 |
|  | [[Megestrol (drug)]] 0.05 µM |  | -3.5 | -3.9 |
|  | [[Berbamine (drug)]] 0.05 µM |  | -3.4 | -3.6 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | -3.3 | -4.1 |

## What is on record

|  |  |
|---|---|
| Name | ELL associated factor 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 3q13.33 — chr3:121,835,183-121,886,526 (+) |
| Ensembl biotype | protein_coding |
| Also known as | BM040, TRAITS, U19 |
| Reactome | 7 pathways, smallest: Formation of RNA Pol II elongation complex; RNA Polymerase II Transcription Elongation; RNA Polymerase II Pre-transcription Events |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96CJ1](https://www.uniprot.org/uniprotkb/Q96CJ1) (ELL-associated factor 2):

> Acts as a transcriptional transactivator of TCEA1 elongation activity (By similarity). Acts as a transcriptional transactivator of ELL and ELL2 elongation activities. Potent inducer of apoptosis in prostatic and non-prostatic cell lines. Inhibits prostate tumor growth in vivo.

**Summary**, from NCBI Gene [55840](https://www.ncbi.nlm.nih.gov/gene/55840):

> Enables transcription elongation factor activity. Involved in positive regulation of transcription by RNA polymerase II and regulation of transcription elongation by RNA polymerase II. Part of transcription elongation factor complex. Biomarker of prostate cancer. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:23115](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23115) · Entrez [55840](https://www.ncbi.nlm.nih.gov/gene/55840) · UniProt [Q96CJ1](https://www.uniprot.org/uniprotkb/Q96CJ1) · Ensembl [ENSG00000145088](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000145088)

## Data

Gene col 6956: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6956); `tables/drug_effects.parquet` (41 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6956, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6956]; `tensor/DDL_lfc|DDL_z.npy` [6956]; `embed/gene_vectors.npy` [6956]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6956 or target_col == 6956). Every well: [[EAF2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/EAF2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
