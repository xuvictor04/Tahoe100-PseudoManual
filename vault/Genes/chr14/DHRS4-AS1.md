---
symbol: "DHRS4-AS1"
type: "gene"
col: 13257
ensembl_id: "ENSG00000215256"
name: "DHRS4 antisense RNA 1"
location: "14q11.2"
module: 15
arm: "+"
pooled_cpm: 8.99
n_lines_expressing: 50
n_dd_up: 11
n_dd_down: 12
n_dd_up_clean: 7
n_dd_down_clean: 10
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/015"]
generated_by: "tahoemap"
---

# DHRS4-AS1

*DHRS4 antisense RNA 1* — 14q11.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 11 drug-doses (4 with an alert ⚠); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 2.26× (z +14.4, q 5e-44, up in 38 of 43 measured lines).
> Pooled over the cell lines (median), lowered significantly by 12 drug-doses (2 with an alert ⚠); the strongest is [[Digitoxin (drug)]] 0.5 µM: 0.496× (z -8.7, q 2e-15, down in 37 of 46 measured lines).
> Its strongest partners by |cos| (88 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 12 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[RWDD2B]] (+0.71, fdr 1e-05), [[TYSND1]] (+0.65, fdr 3e-05), [[PGAP4]] (+0.64, fdr 7e-05); moves opposite to [[GPRIN1]] (-0.58, fdr 1e-04), [[CADM4]] (-0.58, fdr 1e-04), [[KANK2]] (-0.56, fdr 3e-04).
> It sits in the **+** arm of [[Module 015]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[TOP2A]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 11 in all, 4 with an alert ⚠. 11 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13257.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **2.26×** | +14.4 | 5e-44 | 38/43 (A498, A549, …) | rises with dose | cell-cycle shift (explains ~2% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.97×** | +8.1 | 2e-13 | 13/16 (MIA PaCa-2, NCI-H2347, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **1.76×** | +7.0 | 4e-10 | 19/32 (Panc 03.27, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **1.63×** | +5.9 | 6e-07 | 26/43 (A498, LS 180, …) | top dose only | cell-cycle shift (explains ~4% here) |
| [[Selinexor (drug)]] 5 µM |  | **1.38×** | +5.7 | 1e-06 | 20/47 (NCI-H2347, J82, …) | rises with dose | low cells (technical?); cell-cycle shift (explains ~14% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.50×** | +5.1 | 4e-05 | 22/47 (MIA PaCa-2, A549, …) | all doses, stronger at high dose |  |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.33×** | +5.0 | 4e-05 | 19/47 (BT-474, NCI-H2030, …) | top dose only |  |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.41×** | +4.1 | 0.002 | 15/43 (NCI-H460, LS 180, …) | top dose only | cell-cycle shift (explains ~3% here) |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.32×** | +3.5 | 0.035 | 12/44 (A-427, NCI-H1792, …) | all doses, stronger at high dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.32×** | +3.3 | 0.047 | 14/39 (SW1417, SW480, …) | top dose only | cell-cycle shift (explains ~15% here) |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.31×** | +3.3 | 0.047 | 12/38 (Panc 03.27, Hs 766T, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 2 with an alert ⚠. 12 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13257.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Digitoxin (drug)]] 0.5 µM |  | **0.496×** | -8.7 | 2e-15 | 37/46 (PANC-1, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~3% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.509×** | -8.4 | 1e-14 | 30/44 (SNU-423, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **0.554×** | -7.4 | 4e-11 | 33/47 (PANC-1, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~6% here); composition shift |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.582×** | -6.7 | 2e-09 | 24/45 (AN3 CA, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~4% here) |
| [[Ixazomib citrate (drug)]] 5 µM |  | **0.612×** | -6.1 | 1e-07 | 26/47 (MIA PaCa-2, AN3 CA, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[TAK-901 (drug)]] 5 µM |  | **0.396×** | -6.0 | 2e-07 | 27/45 (KATO III, NCI-H23, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.05 µM |  | **0.632×** | -5.4 | 6e-06 | 25/44 (HEC-1-A, LOX-IMVI, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **0.670×** | -5.0 | 4e-05 | 22/46 (LoVo, LS 180, …) | rises with dose |  |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.706×** | -4.2 | 0.002 | 18/39 (A-172, PANC-1, …) | rises with dose | cell-cycle shift (explains ~6% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.537×** | -4.0 | 0.003 | 15/42 (A-427, HEC-1-A, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.05 µM |  | **0.741×** | -3.6 | 0.015 | 18/46 (HOP62, SNU-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **0.759×** | -3.3 | 0.041 | 15/48 (SW 900, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~10% here) |
| [[Dihydroartemisinin (drug)]] 5 µM |  | 0.784× | -3.0 | 0.11 | 7/46 (NCI-H460, PANC-1, …) | rises with dose |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.07 per unit of S-phase module lfc, -0.14 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13257. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 7.31 | 0 | 4 (2 ⚠) | — | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.165× (z -11.4) |
| [[NCI-H1792 (line)]] | alt | 4.94 | 0 | 2 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.0886× (z -8.6) ⚠ cell-cycle shift, explains ~54% of this change · without an alert: [[Bosentan (hydrate) (drug)]] 5 µM 0.0903× (z -8.5) |
| [[NCI-H460 (line)]] | wt | 7.39 | 1 | 1 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.11× (z +9.3) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.235× (z -8.5) |
| [[A-427 (line)]] | wt | 10.7 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.173× (z -8.6) |
| [[A498 (line)]] | wt | 7.44 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.48× (z +12.1) | — |
| [[A549 (line)]] | wt | 8.90 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 4.83× (z +10.2) | — |
| [[BT-474 (line)]] | alt | 14.6 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.50× (z +8.9) | — |
| [[C32 (line)]] | wt | 9.11 | 0 | 1 | — | [[Canagliflozin (drug)]] 0.05 µM 0.131× (z -8.6) |
| [[COLO 205 (line)]] | alt | 10.0 | 0 | 1 | — | [[Silodosin (drug)]] 5 µM 0.0832× (z -9.6) |
| [[H4 (line)]] | wt | 10.3 | 0 | 1 | — | [[Cytarabine (drug)]] 0.05 µM 0.0704× (z -8.6) |
| [[HEC-1-A (line)]] | alt | 9.07 | 1 | 0 | [[Idarubicin (hydrochloride) (drug)]] 5 µM 3.12× (z +8.7) | — |
| [[Hs 766T (line)]] | wt | 6.67 | 0 | 1 | — | [[Pyridoxine (drug)]] 0.5 µM 0.115× (z -8.7) |
| [[HS-578T (line)]] | alt | 5.04 | 0 | 1 | — | [[Canagliflozin (hemihydrate) (drug)]] 0.5 µM 0.0813× (z -9.4) |
| [[MIA PaCa-2 (line)]] | alt | 10.3 | 0 | 1 (1 ⚠) | — | [[Topotecan (hydrochloride) (drug)]] 5 µM 0.162× (z -8.6) ⚠ toxic |
| [[SHP-77 (line)]] | alt | 32.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.129× (z -12.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 6.78 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0749× (z -10.7) ⚠ toxic; transcription drop |
| [[SW48 (line)]] | wt | 22.6 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.104× (z -10.1) |
| [[A-172 (line)]] | wt | 4.41 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 3.62 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 7.78 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 6.06 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 7.56 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 4.46 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.98 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 7.00 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 5.68 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 6.44 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.53 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.68 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 11.8 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 8.12 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 7.88 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.33 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 5.67 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 4.96 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 7.89 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 7.67 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 8.25 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.94 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.83 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 4.50 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.4 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 11.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13257), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*94 of its nearest partners move with it, 12 of them with an alert (⚠; 12 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RWDD2B]] | +0.71 | +0.71 / +0.51 | both halves | 1e-05 |  |
| [[TYSND1]] | +0.65 | +0.60 / +0.43 | both halves | 3e-05 |  |
| [[PGAP4]] | +0.64 | +0.38 / +0.63 | both halves | 7e-05 |  |
| [[HOXB7]] | +0.63 | +0.42 / +0.51 | both halves | 4e-05 |  |
| [[SMIM19]] | +0.63 | +0.67 / +0.35 | both halves | 1e-04 |  |
| [[SENP8]] | +0.63 | +0.63 / +0.36 | both halves | 1e-04 |  |
| [[MAILR]] | +0.62 | +0.68 / +0.31 | both halves | 2e-04 |  |
| [[C17orf75]] | +0.62 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[UBE3B]] | +0.61 | +0.64 / +0.29 | both halves | 3e-04 |  |
| [[TP53]] | +0.61 | +0.62 / +0.40 | both halves | 5e-05 |  |
| [[ERCC6L2-AS1]] | +0.61 | +0.66 / +0.30 | both halves | 2e-04 | same gene group |
| [[C2orf76]] | +0.61 | +0.60 / +0.34 | both halves | 1e-04 |  |

## Genes that move opposite

*6 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[GPRIN1]] | -0.58 | -0.42 / -0.33 | both halves | 1e-04 |  |
| [[CADM4]] | -0.58 | -0.34 / -0.33 | both halves | 1e-04 |  |
| [[KANK2]] | -0.56 | -0.43 / -0.28 | both halves | 3e-04 |  |
| [[GIPC1]] | -0.55 | -0.34 / -0.28 | both halves | 3e-04 |  |
| [[SHF]] | -0.55 | -0.42 / -0.43 | both halves | 4e-05 |  |
| [[R3HDM4]] | -0.55 | -0.37 / -0.43 | both halves | 7e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[TOP2A]] | B | TOP2A activity lowers DHRS4-AS1's level | compounds that target TOP2A: 4 of 5 raise it (Doxorubicin, Epirubicin, Idarubicin, Mitoxantrone) | 80% of the class's compounds vs 2.5% of all compounds | 0.008 | ⚠ off-target possible; 4 compounds; artifact flags |
| [[PSMB5]] | B | PSMB5 activity raises DHRS4-AS1's level | compounds that target PSMB5: 2 of 2 lower it (Bortezomib, Ixazomib / Ixazomib citrate) | 100% of the class's compounds vs 2.0% of all compounds | 0.095 | ⚠ off-target possible; 2 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 015]]; 210 genes; this gene is in the **+** arm (projection on the module's main direction 0.449). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.27).
- **Nodal map** (x, y) = (1.1, 13.7); signed map (26.6, -14.9). **Vector** length 50.2, 6.29% of its response variance represented; |z| ≥ 3 in 950 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | +6.6 | +14.4 |
|  | [[Selinexor (drug)]] 5 µM |  | +4.2 | +5.7 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | +3.3 | +5.9 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | +2.9 | +4.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +2.5 | +5.0 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.0 | +5.1 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | +1.7 | +1.0 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +1.2 | +2.1 |
|  | [[XRK3F2 (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.4 | -1.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift | -2.2 | +0.5 |
|  | [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.2 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 5 µM |  | -1.9 | -6.1 |
|  | [[Panobinostat (drug)]] 0.05 µM | ⚠ cell-cycle shift | -1.8 | +0.4 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -1.4 | -0.1 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -1.4 | -5.0 |
|  | [[PF-06260933 (drug)]] 5 µM |  | -1.3 | -2.5 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.2 | -1.3 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -0.9 | -2.0 |

## What is on record

|  |  |
|---|---|
| Name | DHRS4 antisense RNA 1 |
| Locus type | RNA, long non-coding (non-coding RNA) |
| Location | 14q11.2 — chr14:23,938,219-24,052,555 (-) |
| Ensembl biotype | lncRNA |
| Also known as | PRO1488, AS1DHRS4; previously C14orf167 |
| Gene groups (HGNC) | Antisense RNAs |
| Matched by | ensembl_id |

UniProt [Q9P1J3](https://www.uniprot.org/uniprotkb/Q9P1J3) carries no function annotation.

NCBI Gene carries no summary paragraph for it.

**Accessions** — [HGNC:23175](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:23175) · Entrez [55449](https://www.ncbi.nlm.nih.gov/gene/55449) · UniProt [Q9P1J3](https://www.uniprot.org/uniprotkb/Q9P1J3) · Ensembl [ENSG00000215256](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000215256)

## Data

Gene col 13257: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13257); `tables/drug_effects.parquet` (24 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13257, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13257]; `tensor/DDL_lfc|DDL_z.npy` [13257]; `embed/gene_vectors.npy` [13257]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13257 or target_col == 13257). Every well: [[DHRS4-AS1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/DHRS4-AS1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
