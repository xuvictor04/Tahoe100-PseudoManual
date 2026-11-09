---
symbol: "BCL2L2"
type: "gene"
col: 4976
ensembl_id: "ENSG00000129473"
name: "BCL2 like 2"
location: "14q11.2"
module: 126
arm: "+"
pooled_cpm: 19.85
n_lines_expressing: 50
n_dd_up: 10
n_dd_down: 8
n_dd_up_clean: 5
n_dd_down_clean: 7
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/126"]
generated_by: "tahoemap"
---

# BCL2L2

*BCL2 like 2* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 10 drug-doses (5 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 1.66× (z +10.8, q 3e-24, up in 37 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 8 drug-doses (1 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 0.582× (z -11.6, q 4e-28, down in 37 of 47 measured lines) ⚠ cell-cycle shift, explains ~32% of this change. The strongest without an alert is [[Harringtonine (drug)]] 5 µM: 0.502× (z -10.0, q 4e-21, down in 38 of 47 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[LDB1]] (+0.68, fdr 1e-05), [[GARS1-DT]] (+0.68, fdr 7e-06), [[BCL2L2-PABPN1]] (+0.65, fdr 8e-06, ⚠ same locus), [[EOLA2]] (+0.65, fdr 7e-06); moves opposite to [[CEBPZ]] (-0.59, fdr 7e-06), [[MRPL57]] (-0.59, fdr 1e-05), [[MRPS18B]] (-0.58, fdr 1e-05).
> It is in [[Module 126]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 5 with an alert ⚠. 10 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 5 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4976.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.66×** | +10.8 | 3e-24 | 37/47 (HOP62, A-172, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.62×** | +7.2 | 1e-10 | 23/41 (NCI-H1573, LS 180, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.50×** | +5.9 | 7e-07 | 23/47 (RKO, HOP62, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **1.49×** | +5.5 | 5e-06 | 23/37 (MIA PaCa-2, Panc 03.27, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.35×** | +4.3 | 0.002 | 21/48 (HOP62, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~0% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.27×** | +3.6 | 0.024 | 16/47 (HEC-1-A, A-427, …) | top dose only | position effect removed |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.27×** | +3.6 | 0.024 | 15/47 (LoVo, A-172, …) | inconsistent across doses |  |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.27×** | +3.6 | 0.024 | 17/44 (BT-474, RPMI-7951, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here); position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.27×** | +3.5 | 0.033 | 16/32 (LoVo, NCI-H2030, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Bosentan (hydrate) (drug)]] 5 µM |  | **1.25×** | +3.2 | 0.076 | 15/46 (PANC-1, SNU-423, …) | top dose only | position effect removed |
| [[PF-06260933 (drug)]] 5 µM |  | 1.48× | +3.1 | 0.10 | 7/45 (C32, RPMI-7951, …) | top dose only | noisy plate (z scaled); position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 9 in all, 1 with an alert ⚠. 8 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 1 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4976.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **0.582×** | -11.6 | 4e-28 | 37/47 (NCI-H1792, CFPAC-1, …) | rises with dose | composition shift |
| [[Harringtonine (drug)]] 5 µM |  | **0.502×** | -10.0 | 4e-21 | 38/47 (MIA PaCa-2, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~22% here); composition shift |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **0.559×** | -8.8 | 3e-16 | 32/46 (MIA PaCa-2, RKO, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Panobinostat (drug)]] 5 µM |  | **0.588×** | -8.0 | 1e-13 | 36/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here); position effect removed |
| [[Panobinostat (drug)]] 0.5 µM |  | **0.597×** | -7.8 | 8e-13 | 37/48 (A549, C-33 A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~12% here); position effect removed |
| [[Belinostat (drug)]] 5 µM |  | **0.698×** | -5.4 | 5e-06 | 27/47 (C-33 A, SK-MEL-2, …) | top dose only | cell-cycle shift (explains ~21% here) |
| [[Lidocaine (hydrochloride) (drug)]] 5 µM |  | **0.810×** | -4.5 | 5e-04 | 19/48 (SW480, MIA PaCa-2, …) | top dose only | position effect removed |
| [[TAK-901 (drug)]] 0.05 µM |  | **0.750×** | -4.1 | 0.003 | 20/47 (Panc 03.27, NCI-H2347, …) | inconsistent across doses |  |
| [[Tucidinostat (drug)]] 5 µM |  | 0.860× | -3.3 | 0.072 | 16/48 (HT-29, LOX-IMVI, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.08 per unit of S-phase module lfc, -0.24 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4976. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[MIA PaCa-2 (line)]] | alt | 32.5 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.0802× (z -19.0) |
| [[NCI-H1573 (line)]] | alt | 25.1 | 0 | 3 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.356× (z -10.2) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[Harringtonine (drug)]] 5 µM 0.236× (z -9.7) |
| [[A-427 (line)]] | wt | 14.9 | 1 | 1 (1 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.72× (z +8.5) | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.0745× (z -15.9) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[Panc 03.27 (line)]] | alt | 24.2 | 0 | 2 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.387× (z -9.9) ⚠ cell-cycle shift, explains ~32% of this change · without an alert: [[TAK-901 (drug)]] 0.05 µM 0.292× (z -8.6) |
| [[A-172 (line)]] | wt | 15.2 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.93× (z +9.7) | — |
| [[C32 (line)]] | wt | 31.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -9.3) ⚠ cell-cycle shift, explains ~32% of this change |
| [[CFPAC-1 (line)]] | alt | 27.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.266× (z -14.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[H4 (line)]] | wt | 30.2 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.117× (z -10.5) ⚠ toxic; cell-cycle shift, would explain all of this change |
| [[HOP62 (line)]] | alt | 14.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.06× (z +10.9) | — |
| [[J82 (line)]] | alt | 19.6 | 0 | 1 (1 ⚠) | — | [[Torkinib (drug)]] 5 µM 0.0724× (z -9.8) ⚠ toxic |
| [[NCI-H1792 (line)]] | alt | 22.5 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.188× (z -15.5) ⚠ cell-cycle shift, explains ~32% of this change |
| [[NCI-H460 (line)]] | wt | 21.2 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.369× (z -12.2) ⚠ cell-cycle shift, explains ~32% of this change |
| [[RKO (line)]] | wt | 17.4 | 0 | 1 | — | [[Homoharringtonine (drug)]] 0.5 µM 0.211× (z -8.8) |
| [[SW480 (line)]] | alt | 17.7 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.14× (z +9.2) | — |
| [[A498 (line)]] | wt | 12.9 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.1 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 14.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 22.9 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 45.2 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 16.7 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 19.7 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 12.6 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 21.5 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 14.3 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 16.6 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 26.0 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.5 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 18.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 19.8 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 16.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 18.8 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 18.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 20.4 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 20.8 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 17.0 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 19.8 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 29.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 30.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 27.0 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 13.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 21.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 22.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4976), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*78 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[LDB1]] | +0.68 | +0.57 / +0.60 | both halves | 1e-05 |  |
| [[GARS1-DT]] | +0.68 | +0.60 / +0.60 | both halves | 7e-06 |  |
| [[BCL2L2-PABPN1]] | +0.65 | +0.58 / +0.58 | both halves | 8e-06 | STRING 554; ⚠ same locus (0.0 kb, same strand: neighbours can correlate without regulation) |
| [[EOLA2]] | +0.65 | +0.64 / +0.68 | both halves | 7e-06 |  |
| [[CRYBB2P1]] | +0.65 | +0.62 / +0.74 | both halves | 7e-06 |  |
| [[HFM1]] | +0.64 | +0.52 / +0.56 | both halves | 1e-05 |  |
| [[CERS2]] | +0.64 | +0.52 / +0.59 | both halves | 1e-05 |  |
| [[NADSYN1]] | +0.63 | +0.62 / +0.54 | both halves | 1e-05 |  |
| [[MSL3]] | +0.63 | +0.55 / +0.54 | both halves | 1e-05 |  |
| [[SNHG22]] | +0.62 | +0.38 / +0.58 | both halves | 6e-05 |  |
| [[AJM1]] | +0.61 | +0.62 / +0.59 | both halves | 7e-06 |  |
| [[PCGF2]] | +0.60 | +0.52 / +0.57 | both halves | 1e-05 |  |
| [[EEF1AKMT3]] | +0.60 | +0.50 / +0.57 | both halves | 1e-05 |  |

## Genes that move opposite

*22 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CEBPZ]] | -0.59 | -0.59 / -0.63 | both halves | 7e-06 |  |
| [[MRPL57]] | -0.59 | -0.55 / -0.55 | both halves | 1e-05 |  |
| [[MRPS18B]] | -0.58 | -0.54 / -0.61 | both halves | 1e-05 |  |
| [[PIGBOS1]] | -0.58 | -0.50 / -0.59 | both halves | 1e-05 |  |
| [[MTRES1]] | -0.58 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[AGGF1]] | -0.55 | -0.49 / -0.55 | both halves | 1e-05 |  |
| [[KBTBD6]] | -0.55 | -0.42 / -0.54 | both halves | 4e-05 |  |
| [[GPATCH11]] | -0.55 | -0.40 / -0.52 | both halves | 4e-05 |  |
| [[KBTBD7]] | -0.54 | -0.52 / -0.48 | both halves | 2e-05 |  |
| [[WDR70]] | -0.53 | -0.51 / -0.39 | both halves | 6e-05 |  |
| [[MIS18A]] | -0.53 | -0.55 / -0.41 | both halves | 4e-05 |  |
| [[TTC26]] | -0.53 | -0.44 / -0.47 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers BCL2L2's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin) | 60% of the class's compounds vs 2.2% of all compounds | 0.059 | ⚠ off-target possible; 3 compounds; artifact flags |
| [[HDAC6]] | B | HDAC6 activity raises BCL2L2's level | compounds that target HDAC6: 2 of 2 lower it (Belinostat, Panobinostat) | 100% of the class's compounds vs 1.7% of all compounds | 0.084 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 126]]; 39 genes; every member is in the + arm (projection on the module's main direction 0.718). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-15.9, -21.6); signed map (2.2, 1.8). **Vector** length 98.4, 21.1% of its response variance represented; |z| ≥ 3 in 908 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +8.6 | +10.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +6.1 | +5.9 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.7 | +5.5 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +5.3 | +4.3 |
|  | [[Auranofin (drug)]] 5 µM |  | +4.7 | +3.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +3.5 | -0.6 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +2.5 | +3.2 |
|  | [[venetoclax (drug)]] 5 µM |  | +2.0 | +1.8 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 0.5 µM |  | +1.8 | +1.9 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~32% of this change | -6.9 | -11.6 |
|  | [[Homoharringtonine (drug)]] 0.5 µM |  | -6.1 | -8.8 |
|  | [[Harringtonine (drug)]] 5 µM |  | -5.9 | -10.0 |
|  | [[Panobinostat (drug)]] 0.5 µM |  | -2.8 | -7.8 |
|  | [[Ribociclib (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | -2.7 | +1.1 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -2.4 | -4.1 |
|  | [[PH-797804 (drug)]] 5 µM |  | -2.2 | -1.6 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.0 | -3.3 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.05 µM |  | -1.8 | -1.4 |
|  | [[Arbutin (drug)]] 5 µM |  | -1.8 | -1.7 |

## What is on record

|  |  |
|---|---|
| Name | BCL2 like 2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 14q11.2 — chr14:23,298,790-23,311,751 (+) |
| Ensembl biotype | protein_coding |
| Also known as | KIAA0271, BCL-W, PPP1R51 |
| Gene groups (HGNC) | Protein phosphatase 1 regulatory subunits; BCL2 family |
| Hallmark sets | APOPTOSIS |
| Matched by | ensembl_id |

**Function**, from UniProt [Q92843](https://www.uniprot.org/uniprotkb/Q92843) (Bcl-2-like protein 2):

> Promotes cell survival. Blocks dexamethasone-induced apoptosis. Mediates survival of postmitotic Sertoli cells by suppressing death-promoting activity of BAX.

**Summary**, from NCBI Gene [599](https://www.ncbi.nlm.nih.gov/gene/599):

> This gene encodes a member of the BCL-2 protein family. The proteins of this family form hetero- or homodimers and act as anti- and pro-apoptotic regulators. Expression of this gene in cells has been shown to contribute to reduced cell apoptosis under cytotoxic conditions. Studies of the related gene in mice indicated a role in the survival of NGF- and BDNF-dependent neurons. Mutation and knockout studies of the mouse gene demonstrated an essential role in adult spermatogenesis. Alternative …

**Accessions** — [HGNC:995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:995) · Entrez [599](https://www.ncbi.nlm.nih.gov/gene/599) · UniProt [Q92843](https://www.uniprot.org/uniprotkb/Q92843) · Ensembl [ENSG00000129473](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000129473)

## Data

Gene col 4976: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4976); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4976, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4976]; `tensor/DDL_lfc|DDL_z.npy` [4976]; `embed/gene_vectors.npy` [4976]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4976 or target_col == 4976). Every well: [[BCL2L2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/BCL2L2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
