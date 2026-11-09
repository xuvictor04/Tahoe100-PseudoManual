---
symbol: "TUBE1"
type: "gene"
col: 1095
ensembl_id: "ENSG00000074935"
name: "tubulin epsilon 1"
location: "6q21"
module: 63
arm: "+"
pooled_cpm: 26.35
n_lines_expressing: 50
n_dd_up: 8
n_dd_down: 29
n_dd_up_clean: 6
n_dd_down_clean: 23
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# TUBE1

*tubulin epsilon 1* — 6q21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 8 drug-doses (2 with an alert ⚠); the strongest is [[Artesunate (drug)]] 5 µM: 1.52× (z +5.1, q 2e-04, up in 34 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 29 drug-doses (6 with an alert ⚠); the strongest is [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM: 0.584× (z -6.9, q 4e-09, down in 37 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZFAND1]] (+0.72, fdr 7e-06), [[ASNS]] (+0.71, fdr 7e-06), [[TCEA1]] (+0.68, fdr 7e-06); moves opposite to [[ZNF407]] (-0.64, fdr 1e-05), [[PURB]] (-0.61, fdr 1e-05), [[PHF23]] (-0.59, fdr 1e-05).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[ANK2]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 2 with an alert ⚠. 8 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1095.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Artesunate (drug)]] 5 µM |  | **1.52×** | +5.1 | 2e-04 | 34/48 (HCT15, SHP-77, …) | rises with dose | cell-cycle shift (explains ~5% here); noisy plate (z scaled) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.62×** | +4.8 | 5e-04 | 30/48 (MIA PaCa-2, C-33 A, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **1.54×** | +4.2 | 0.004 | 27/48 (HCT15, SHP-77, …) | rises with dose |  |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **1.51×** | +3.9 | 0.014 | 26/45 (NCI-H2030, C32, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Ponatinib (drug)]] 5 µM |  | **1.44×** | +3.6 | 0.034 | 20/48 (BT-474, SW480, …) | top dose only |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.41×** | +3.4 | 0.069 | 21/47 (BT-474, HCT15, …) | rises with dose |  |
| [[Tomivosertib (drug)]] 5 µM |  | **1.91×** | +3.3 | 0.069 | 17/48 (LoVo, MIA PaCa-2, …) | top dose only | plate-row cell shift; noisy plate (z scaled) |
| [[Verteporfin (drug)]] 5 µM |  | **1.42×** | +3.3 | 0.072 | 13/47 (A-427, NCI-H2030, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 5 µM |  | 1.29× | +3.1 | 0.11 | 13/48 (BT-474, NCI-H460, …) | rises with dose | noisy plate (z scaled) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | 1.37× | +3.1 | 0.11 | 15/48 (MIA PaCa-2, Hs 766T, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 29 in all, 6 with an alert ⚠; shown: the 15 strongest and the 4 next strongest without an alert. 29 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 6 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 1095.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **0.584×** | -6.9 | 4e-09 | 37/48 (HOP62, HepG2/C3A, …) | top dose only | noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.535×** | -6.1 | 3e-07 | 25/41 (PANC-1, KATO III, …) | all doses, flat | cell-cycle shift (explains ~16% here); composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.620×** | -5.8 | 1e-06 | 31/48 (LoVo, SW480, …) | top dose only | cell-cycle shift (explains ~0% here); noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.529×** | -5.8 | 1e-06 | 22/37 (HT-29, SW1417, …) | all doses, flat | cell-cycle shift (explains ~7% here); composition shift |
| [[Filgotinib (drug)]] 5 µM |  | **0.573×** | -5.5 | 5e-06 | 36/48 (RKO, LOX-IMVI, …) | inconsistent across doses | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **0.581×** | -5.3 | 1e-05 | 31/48 (SW480, SW48, …) | two highest doses | cell-cycle shift (explains ~14% here) |
| [[Digitoxin (drug)]] 0.5 µM |  | **0.592×** | -5.1 | 2e-05 | 30/48 (SW480, KATO III, …) | rises with dose | cell-cycle shift (explains ~15% here) |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.607×** | -4.9 | 7e-05 | 34/48 (A-427, KATO III, …) | inconsistent across doses |  |
| [[Auranofin (drug)]] 5 µM |  | **0.609×** | -4.9 | 8e-05 | 27/48 (SW 1271, SW480, …) | top dose only |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.612×** | -4.8 | 8e-05 | 30/47 (SHP-77, A-172, …) | rises with dose | cell-cycle shift (explains ~21% here) |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.608×** | -4.7 | 1e-04 | 24/47 (NCI-H1792, PANC-1, …) | all doses, flat | composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.403×** | -4.7 | 1e-04 | 30/48 (H4, SHP-77, …) | inconsistent across doses | plate-row cell shift; cell-cycle shift (explains ~10% here); composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.626×** | -4.6 | 2e-04 | 25/48 (hTERT-HPNE, PANC-1, …) | all doses, flat | cell-cycle shift (explains ~12% here) |
| [[PH-797804 (drug)]] 5 µM |  | **0.420×** | -4.4 | 4e-04 | 26/47 (SNU-423, RKO, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.613×** | -4.4 | 4e-04 | 26/47 (KATO III, PANC-1, …) | all doses, flat | low cells (technical?) |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | **0.669×** | -3.9 | 0.003 | 25/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |
| [[Esmolol (hydrochloride) (drug)]] 5 µM |  | **0.690×** | -3.6 | 0.009 | 20/48 (LS 180, LOX-IMVI, …) | top dose only |  |
| [[Berbamine (drug)]] 0.05 µM |  | **0.698×** | -3.5 | 0.013 | 20/48 (NCI-H2347, A498, …) | inconsistent across doses |  |
| [[Retinoic acid (drug)]] 0.05 µM |  | **0.705×** | -3.4 | 0.017 | 17/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.06 per unit of S-phase module lfc, -0.29 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1095. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[SW480 (line)]] | alt | 26.7 | 0 | 4 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.171× (z -13.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Digitoxin (drug)]] 0.5 µM 0.261× (z -10.4) |
| [[SHP-77 (line)]] | alt | 24.5 | 0 | 3 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.116× (z -11.8) ⚠ toxic; transcription drop · without an alert: [[Fluvoxamine (maleate) (drug)]] 0.5 µM 0.208× (z -8.6) |
| [[KATO III (line)]] | alt | 36.3 | 0 | 2 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.176× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change · without an alert: [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.281× (z -9.2) |
| [[PANC-1 (line)]] | alt | 67.5 | 0 | 2 (2 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.262× (z -11.1) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[RKO (line)]] | wt | 25.2 | 1 (1 ⚠) | 1 | [[Homoharringtonine (drug)]] 5 µM 3.76× (z +8.7) ⚠ cell-cycle shift, explains ~0% of this change | [[PH-797804 (drug)]] 5 µM 0.0483× (z -8.7) |
| [[A-172 (line)]] | wt | 17.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.221× (z -8.7) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 20.7 | 0 | 1 | — | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM 0.190× (z -12.5) |
| [[HT-29 (line)]] | alt | 26.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.128× (z -10.9) ⚠ toxic; transcription drop |
| [[hTERT-HPNE (line)]] | wt | 42.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.198× (z -8.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~23% of this change |
| [[LoVo (line)]] | wt | 30.6 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.191× (z -12.2) |
| [[NCI-H1792 (line)]] | alt | 63.6 | 0 | 1 (1 ⚠) | — | [[Harringtonine (drug)]] 5 µM 0.176× (z -9.2) ⚠ cell-cycle shift, explains ~30% of this change |
| [[NCI-H661 (line)]] | alt | 35.8 | 0 | 1 (1 ⚠) | — | [[Simotinib (drug)]] 5 µM 0.0658× (z -8.5) ⚠ toxic |
| [[SNU-1 (line)]] | wt | 29.3 | 0 | 1 (1 ⚠) | — | [[Mitoxantrone (dihydrochloride) (drug)]] 0.5 µM 0.139× (z -8.5) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SNU-423 (line)]] | alt | 26.2 | 0 | 1 | — | [[PH-797804 (drug)]] 5 µM 0.0219× (z -9.7) |
| [[SW1417 (line)]] | alt | 8.55 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.116× (z -9.2) ⚠ toxic; transcription drop |
| [[A-427 (line)]] | wt | 17.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 19.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 9.20 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 31.2 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 27.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 9.73 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 36.0 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 8.69 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 30.3 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 64.4 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 19.4 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 28.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 30.7 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 14.6 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 23.3 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 66.2 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 27.9 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 17.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 13.2 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 14.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 27.7 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 31.6 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 15.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 32.2 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 38.3 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 23.1 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 37.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1095), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZFAND1]] | +0.72 | +0.72 / +0.68 | both halves | 7e-06 |  |
| [[ASNS]] | +0.71 | +0.67 / +0.69 | both halves | 7e-06 |  |
| [[TCEA1]] | +0.68 | +0.73 / +0.58 | both halves | 7e-06 |  |
| [[GARS1]] | +0.68 | +0.70 / +0.56 | both halves | 1e-05 |  |
| [[ANAPC4]] | +0.68 | +0.68 / +0.62 | both halves | 7e-06 |  |
| [[UBA5]] | +0.67 | +0.69 / +0.61 | both halves | 7e-06 |  |
| [[MTX2]] | +0.66 | +0.72 / +0.54 | both halves | 1e-05 |  |
| [[MTHFD2]] | +0.66 | +0.64 / +0.62 | both halves | 7e-06 |  |
| [[EPRS1]] | +0.65 | +0.69 / +0.52 | both halves | 1e-05 |  |
| [[XPOT]] | +0.65 | +0.69 / +0.53 | both halves | 1e-05 |  |
| [[SEPTIN7P2]] | +0.64 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[NFXL1]] | +0.64 | +0.59 / +0.58 | both halves | 7e-06 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZNF407]] | -0.64 | -0.65 / -0.54 | both halves | 1e-05 |  |
| [[PURB]] | -0.61 | -0.58 / -0.56 | both halves | 1e-05 |  |
| [[PHF23]] | -0.59 | -0.62 / -0.51 | both halves | 1e-05 |  |
| [[RASAL2]] | -0.58 | -0.55 / -0.60 | both halves | 1e-05 |  |
| [[SNRPB]] | -0.58 | -0.63 / -0.48 | both halves | 2e-05 |  |
| [[STAG1]] | -0.55 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[TRIP12]] | -0.55 | -0.48 / -0.51 | both halves | 2e-05 |  |
| [[ASXL2]] | -0.54 | -0.55 / -0.45 | both halves | 3e-05 |  |
| [[GPATCH8]] | -0.53 | -0.57 / -0.49 | both halves | 1e-05 |  |
| [[CDKN2B-AS1]] | -0.53 | -0.53 / -0.41 | both halves | 4e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ANK2]] | B | ANK2 activity raises TUBE1's level | lines that do not express ANK2 (16) vs lines expressing it (34) | 1.55× lower at baseline in the lines without ANK2 | 0.032 | ⚠ within organs, on part of the lines; also absent: VASH1, SOBP, GXYLT2; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.685). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-19.3, 47.8); signed map (-15.3, 24.6). **Vector** length 130, 37.9% of its response variance represented; |z| ≥ 3 in 1,011 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.56 to 16); *mTORC1 signaling* (hallmark, mean cos +0.50 to 20); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.59 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +6.2 | +5.1 |
|  | [[Ponatinib (drug)]] 5 µM |  | +4.1 | +3.6 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +4.1 | +4.8 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +4.0 | +3.9 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +3.7 | +4.2 |
|  | [[Niclosamide (olamine) (drug)]] 0.5 µM |  | +3.6 | +3.1 |
|  | [[Abemaciclib (drug)]] 5 µM |  | +3.5 | +1.5 |
|  | [[Abemaciclib (drug)]] 0.5 µM |  | +3.4 | +2.7 |
| fall | [[Digitoxin (drug)]] 0.5 µM |  | -6.2 | -5.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | -6.1 | -5.3 |
|  | [[TAK-901 (drug)]] 5 µM |  | -6.1 | -4.7 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -5.9 | -6.9 |
|  | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -5.7 | -5.8 |
|  | [[PH-797804 (drug)]] 5 µM |  | -4.8 | -4.4 |
|  | [[TAK-901 (drug)]] 0.05 µM |  | -4.2 | -2.9 |
|  | [[Filgotinib (drug)]] 5 µM |  | -4.2 | -5.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -4.1 | -4.9 |

## What is on record

|  |  |
|---|---|
| Name | tubulin epsilon 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 6q21 — chr6:112,070,663-112,087,529 (-) |
| Ensembl biotype | protein_coding |
| Also known as | dJ142L7.2, FLJ22589, TUBE |
| Gene groups (HGNC) | Tubulin epsilon family |
| Matched by | ensembl_id |

UniProt [Q9UJT0](https://www.uniprot.org/uniprotkb/Q9UJT0) carries no function annotation.

**Summary**, from NCBI Gene [51175](https://www.ncbi.nlm.nih.gov/gene/51175):

> This gene encodes a member of the tubulin superfamily. This protein localizes to the centriolar sub-distal appendages that are associated with the older of the two centrioles after centrosome duplication. This protein plays a central role in organization of the microtubules during centriole duplication. A pseudogene of this gene is found on chromosome 5.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:20775](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:20775) · Entrez [51175](https://www.ncbi.nlm.nih.gov/gene/51175) · UniProt [Q9UJT0](https://www.uniprot.org/uniprotkb/Q9UJT0) · Ensembl [ENSG00000074935](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000074935)

## Data

Gene col 1095: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1095); `tables/drug_effects.parquet` (39 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1095, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1095]; `tensor/DDL_lfc|DDL_z.npy` [1095]; `embed/gene_vectors.npy` [1095]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1095 or target_col == 1095). Every well: [[TUBE1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/TUBE1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
