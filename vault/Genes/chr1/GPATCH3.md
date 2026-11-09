---
symbol: "GPATCH3"
type: "gene"
col: 12665
ensembl_id: "ENSG00000198746"
name: "G-patch domain containing 3"
location: "1p36.11"
module: 172
arm: "+"
pooled_cpm: 8.6
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 6
n_dd_up_clean: 20
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/172"]
generated_by: "tahoemap"
---

# GPATCH3

*G-patch domain containing 3* — 1p36.11

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (6 with an alert ⚠); the strongest is [[Ixazomib citrate (drug)]] 5 µM: 2.55× (z +13.7, q 3e-40, up in 43 of 47 measured lines).
> Pooled over the cell lines (median), lowered significantly by 6 drug-doses (3 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 0.5 µM: 0.523× (z -9.5, q 1e-18, down in 32 of 45 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[SLC38A7]] (+0.76, fdr 7e-06), [[ZFYVE26]] (+0.72, fdr 7e-06), [[C12orf43]] (+0.70, fdr 8e-06); moves opposite to [[EPB41L2]] (-0.59, fdr 2e-05), [[C12orf75]] (-0.55, fdr 3e-05).
> It is in [[Module 172]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 27 in all, 7 with an alert ⚠; shown: the 15 strongest and the 3 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12665.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Ixazomib citrate (drug)]] 5 µM |  | **2.55×** | +13.7 | 3e-40 | 43/47 (PANC-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.50×** | +13.5 | 8e-39 | 40/47 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~7% here); composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **4.19×** | +11.0 | 6e-26 | 39/45 (NCI-H1573, SW480, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~4% here); composition shift; noisy plate (z scaled) |
| [[Ixazomib citrate (drug)]] 0.5 µM |  | **2.22×** | +11.0 | 6e-26 | 42/47 (PANC-1, LS 180, …) | rises with dose |  |
| [[Bortezomib (drug)]] 0.05 µM |  | **2.09×** | +10.2 | 2e-22 | 39/45 (SW480, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~0% here) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.88×** | +9.3 | 2e-18 | 29/44 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Homoharringtonine (drug)]] 5 µM |  | **1.54×** | +8.9 | 4e-17 | 29/44 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~21% here); composition shift; position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.71×** | +7.4 | 1e-11 | 25/46 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~8% here); position effect removed |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.64×** | +6.8 | 6e-10 | 22/46 (NCI-H460, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Auranofin (drug)]] 5 µM |  | **1.56×** | +6.6 | 3e-09 | 24/46 (LoVo, HT-29, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.59×** | +6.5 | 4e-09 | 20/39 (HT-29, NCI-H1573, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Homoharringtonine (drug)]] 0.5 µM |  | **1.55×** | +6.4 | 6e-09 | 18/40 (NCI-H1573, A498, …) | all doses, stronger at high dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[PH-797804 (drug)]] 5 µM |  | **2.29×** | +6.4 | 8e-09 | 25/42 (SW480, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Bortezomib (drug)]] 0.5 µM |  | **1.72×** | +5.7 | 6e-07 | 17/47 (PANC-1, KATO III, …) | all doses, flat | noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.47×** | +5.7 | 6e-07 | 11/47 (Hs 766T, HT-29, …) | inconsistent across doses |  |
| [[Harringtonine (drug)]] 5 µM |  | **1.49×** | +5.6 | 6e-07 | 18/45 (NCI-H1573, A498, …) | rises with dose | cell-cycle shift (explains ~19% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **1.43×** | +5.2 | 6e-06 | 10/46 (NCI-H1573, PANC-1, …) | rises with dose | cell-cycle shift (explains ~9% here); position effect removed |
| [[Medroxyprogesterone acetate (drug)]] 0.5 µM |  | **1.42×** | +5.1 | 1e-05 | 12/44 (SW480, NCI-H460, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 8 in all, 3 with an alert ⚠. 6 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 12665.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 0.5 µM |  | **0.523×** | -9.5 | 1e-18 | 32/45 (RKO, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~1% here) |
| [[Tucidinostat (drug)]] 5 µM |  | **0.668×** | -8.4 | 2e-14 | 39/48 (HOP62, NCI-H460, …) | all doses, stronger at high dose |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.592×** | -7.7 | 3e-12 | 21/34 (HS-578T, NCI-H2347, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.645×** | -6.2 | 9e-08 | 13/15 (SW480, NCI-H460, …) | two highest doses | cell-cycle shift (explains ~0% here); composition shift |
| [[Panobinostat (drug)]] 0.05 µM |  | **0.704×** | -5.1 | 3e-05 | 19/47 (NCI-H460, CHP-212, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.757×** | -4.1 | 0.004 | 15/47 (SNU-423, SW480, …) | inconsistent across doses |  |
| [[Ferulic acid (drug)]] 0.5 µM |  | 0.803× | -3.2 | 0.11 | 7/46 (NCI-H661, NCI-H460, …) | inconsistent across doses | low cells (technical?) |
| [[Brivudine (drug)]] 5 µM |  | 0.668× | -3.1 | 0.14 | 5/47 (SHP-77, SW48, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.02 per unit of S-phase module lfc, +0.15 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12665. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 9.39 | 4 (2 ⚠) | 1 (1 ⚠) | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.66× (z +12.5) | [[Dinaciclib (drug)]] 5 µM 0.259× (z -9.4) ⚠ toxic; transcription drop |
| [[NCI-H1573 (line)]] | alt | 15.9 | 2 | 1 (1 ⚠) | [[Homoharringtonine (drug)]] 5 µM 3.60× (z +11.9) | [[Dinaciclib (drug)]] 0.5 µM 0.136× (z -13.2) ⚠ toxic; transcription drop |
| [[MIA PaCa-2 (line)]] | alt | 5.65 | 0 | 2 | — | [[Ropivacaine (hydrochloride monohydrate) (drug)]] 0.5 µM 0.0719× (z -10.9) |
| [[NCI-H23 (line)]] | alt | 13.4 | 0 | 2 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.159× (z -10.7) |
| [[SW480 (line)]] | alt | 9.85 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -11.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 11.0 | 0 | 1 | — | [[Epirubicin (hydrochloride) (drug)]] 5 µM 0.201× (z -8.6) |
| [[HCT15 (line)]] | alt | 10.4 | 0 | 1 | — | [[Saquinavir (drug)]] 0.5 µM 0.129× (z -8.5) |
| [[HS-578T (line)]] | alt | 9.37 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0507× (z -14.1) ⚠ toxic; transcription drop |
| [[J82 (line)]] | alt | 8.99 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.168× (z -8.6) ⚠ toxic; transcription drop |
| [[LOX-IMVI (line)]] | wt | 8.68 | 0 | 1 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.175× (z -8.8) |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.0774× (z -14.1) ⚠ toxic; transcription drop |
| [[PANC-1 (line)]] | alt | 8.42 | 1 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 5.14× (z +10.6) | — |
| [[RKO (line)]] | wt | 11.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0848× (z -11.2) ⚠ toxic; cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 4.55 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 5.11 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 6.12 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 6.85 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.00 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 8.37 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 5.19 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 5.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 5.32 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 9.79 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 5.81 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 8.85 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 9.70 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.37 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 5.37 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 7.99 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.75 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 9.88 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 8.77 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.41 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 12.5 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.86 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 11.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 9.48 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 11.0 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.63 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 7.46 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 7.20 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 7.12 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.41 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12665), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*98 of its nearest partners move with it, 2 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[SLC38A7]] | +0.76 | +0.68 / +0.76 | both halves | 7e-06 |  |
| [[ZFYVE26]] | +0.72 | +0.67 / +0.71 | both halves | 7e-06 |  |
| [[C12orf43]] | +0.70 | +0.70 / +0.57 | both halves | 8e-06 |  |
| [[NGDN]] | +0.69 | +0.62 / +0.68 | both halves | 7e-06 |  |
| [[MRM3]] | +0.68 | +0.54 / +0.68 | both halves | 1e-05 |  |
| [[VPS11]] | +0.68 | +0.76 / +0.57 | both halves | 1e-05 |  |
| [[WDR81]] | +0.68 | +0.62 / +0.61 | both halves | 7e-06 |  |
| [[TMEM199]] | +0.67 | +0.57 / +0.69 | both halves | 9e-06 |  |
| [[POLR3F]] | +0.67 | +0.54 / +0.74 | both halves | 1e-05 |  |
| [[CCDC12]] | +0.67 | +0.54 / +0.70 | both halves | 1e-05 |  |
| [[POLL]] | +0.66 | +0.58 / +0.64 | both halves | 8e-06 |  |
| [[NKAPD1]] | +0.65 | +0.45 / +0.71 | both halves | 3e-05 |  |

## Genes that move opposite

*2 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[EPB41L2]] | -0.59 | -0.48 / -0.64 | both halves | 2e-05 |  |
| [[C12orf75]] | -0.55 | -0.45 / -0.55 | both halves | 3e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[HDAC1]], [[HDAC2]], [[HDAC3]], [[HDAC8]], [[HDAC10]], [[HDAC11]] | B | HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11 activity raises GPATCH3's level | compounds that target HDAC1, HDAC2, HDAC3, HDAC8, HDAC10, HDAC11: 2 of 2 lower it (Panobinostat, Tucidinostat) | 100% of the class's compounds vs 1.1% of all compounds | 0.059 | ⚠ off-target possible; 2 compounds; artifact flags; shared targets |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 172]]; 24 genes; every member is in the + arm (projection on the module's main direction 0.756). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.36; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-43.9, 11.0); signed map (-8.3, -19.8). **Vector** length 71.1, 11.9% of its response variance represented; |z| ≥ 3 in 988 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM |  | +5.3 | +13.7 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +4.6 | +11.0 |
|  | [[Bortezomib (drug)]] 0.05 µM |  | +4.6 | +10.2 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.9 | +6.5 |
|  | [[TAK-901 (drug)]] 5 µM |  | +2.7 | +11.0 |
|  | [[Auranofin (drug)]] 5 µM |  | +2.5 | +6.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +2.1 | +5.7 |
|  | [[Trametinib (drug)]] 0.5 µM |  | +1.9 | +1.2 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.8 | +3.8 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -6.4 | -8.4 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | -4.9 | -9.5 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -4.2 | -7.7 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | -4.2 | -6.2 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~0% of this change | -3.7 | -1.5 |
|  | [[Brivudine (drug)]] 5 µM |  | -1.8 | -3.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -1.8 | -2.3 |
|  | [[HI-TOPK-032 (drug)]] 5 µM |  | -1.6 | -0.7 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -1.6 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | G-patch domain containing 3 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 1p36.11 — chr1:26,890,488-26,900,467 (-) |
| Ensembl biotype | protein_coding |
| Also known as | FLJ12455; previously GPATC3 |
| Gene groups (HGNC) | G-patch domain containing |
| Matched by | ensembl_id |

**Function**, from UniProt [Q96I76](https://www.uniprot.org/uniprotkb/Q96I76) (G patch domain-containing protein 3):

> Involved in transcriptional regulation. It is able to activate transcription from the CXCR4 promoter and therefore it might control neural crest cell migration involved in ocular and craniofacial development. Is a negative regulator of immune antiviral response, acting via down-regulation of RIG-I-like receptors signaling and inhibition of type I interferon production. The control mechanism involves interaction with mitochondrial MAVS and inhibition of MAVS assembly with downstream proteins …

**Summary**, from NCBI Gene [63906](https://www.ncbi.nlm.nih.gov/gene/63906):

> Predicted to enable nucleic acid binding activity. Involved in negative regulation of RIG-I signaling pathway; negative regulation of type I interferon production; and positive regulation of DNA-templated transcription. Located in cytosol and nucleoplasm. [provided by Alliance of Genome Resources, Jul 2025]

**Accessions** — [HGNC:25720](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25720) · Entrez [63906](https://www.ncbi.nlm.nih.gov/gene/63906) · UniProt [Q96I76](https://www.uniprot.org/uniprotkb/Q96I76) · Ensembl [ENSG00000198746](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000198746)

## Data

Gene col 12665: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12665); `tables/drug_effects.parquet` (35 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12665, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12665]; `tensor/DDL_lfc|DDL_z.npy` [12665]; `embed/gene_vectors.npy` [12665]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12665 or target_col == 12665). Every well: [[GPATCH3 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GPATCH3.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
