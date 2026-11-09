---
symbol: "MAP3K12"
type: "gene"
col: 6323
ensembl_id: "ENSG00000139625"
name: "mitogen-activated protein kinase kinase kinase 12"
location: "12q13.13"
module: 21
arm: "+"
pooled_cpm: 16.75
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 3
n_dd_up_clean: 10
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 3
direction_downstream: 0
tags: ["gene", "module/021"]
generated_by: "tahoemap"
---

# MAP3K12

*mitogen-activated protein kinase kinase kinase 12* — 12q13.13

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (4 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.43× (z +12.3, q 4e-32, up in 37 of 42 measured lines) ⚠ toxic; transcription drop. The strongest without an alert is [[Epirubicin (hydrochloride) (drug)]] 5 µM: 1.45× (z +4.9, q 9e-05, up in 19 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Harringtonine (drug)]] 5 µM: 0.699× (z -4.8, q 0.001, down in 19 of 47 measured lines).
> Its strongest partners by |cos| (99 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ZBTB47-AS1]] (+0.64, fdr 1e-05), [[ZNF451-AS1]] (+0.60, fdr 7e-06), [[CNGB3]] (+0.59, fdr 1e-05); moves opposite to [[APEX2]] (-0.49, fdr 4e-05), [[DCLRE1B]] (-0.48, fdr 2e-04), [[FADD]] (-0.47, fdr 4e-04).
> It is in [[Module 021]], a single-armed module.
> Probable direction (from the cell lines, not proof of direct regulation): 3 arrows point to it, the strongest [[C1orf116]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 4 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 4 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 6323.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **2.43×** | +12.3 | 4e-32 | 37/42 (NCI-H460, NCI-H1573, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **2.36×** | +11.5 | 6e-28 | 26/31 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **2.15×** | +8.7 | 7e-16 | 30/38 (LoVo, HEC-1-A, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled); position effect removed |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop | **1.49×** | +5.5 | 5e-06 | 25/45 (HS-578T, HOP62, …) | inconsistent across doses | low cells (technical?); cell-cycle shift (explains ~0% here) |
| [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | **1.45×** | +4.9 | 9e-05 | 19/48 (HEC-1-A, BT-474, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Allantoin (drug)]] 5 µM |  | **1.23×** | +3.9 | 0.010 | 20/48 (NCI-H2030, H4, …) | inconsistent across doses | position effect removed |
| [[Cepharanthine (drug)]] 5 µM |  | **1.22×** | +3.8 | 0.013 | 21/48 (NCI-H2030, PANC-1, …) | inconsistent across doses | position effect removed |
| [[Triamcinolone (drug)]] 5 µM |  | **1.21×** | +3.7 | 0.017 | 15/48 (PANC-1, NCI-H23, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM |  | **1.30×** | +3.6 | 0.020 | 15/47 (SW1417, Panc 03.27, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Bicalutamide (drug)]] 0.5 µM |  | **1.28×** | +3.4 | 0.036 | 11/47 (BT-474, J82, …) | inconsistent across doses | position effect removed |
| [[Temsirolimus (drug)]] 0.05 µM |  | **1.26×** | +3.2 | 0.067 | 9/48 (RPMI-7951, NCI-H2030, …) | inconsistent across doses | position effect removed |
| [[Budesonide (drug)]] 0.5 µM |  | **1.26×** | +3.2 | 0.067 | 6/47 (HepG2/C3A, A549, …) | inconsistent across doses | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 1.17× | +3.2 | 0.070 | 12/48 (HEC-1-A, SW480, …) | rises with dose | position effect removed |
| [[Dexmedetomidine (drug)]] 0.05 µM |  | **1.32×** | +3.1 | 0.072 | 3/47 (SHP-77, SW1417, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |
| [[Riluzole hydrochloride (drug)]] 5 µM |  | 1.18× | +3.1 | 0.083 | 14/48 (PANC-1, SK-MEL-2, …) | top dose only | position effect removed |
| [[Bimatoprost (drug)]] 0.5 µM |  | **1.24×** | +3.0 | 0.083 | 6/47 (NCI-H2347, KATO III, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 4 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 6323.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 5 µM |  | **0.699×** | -4.8 | 0.001 | 19/47 (H4, LOX-IMVI, …) | rises with dose | cell-cycle shift (explains ~4% here); composition shift; position effect removed |
| [[Harringtonine (drug)]] 0.5 µM |  | **0.762×** | -3.8 | 0.048 | 14/48 (AN3 CA, H4, …) | rises with dose | cell-cycle shift (explains ~3% here); position effect removed |
| [[Larotrectinib (drug)]] 5 µM |  | **0.831×** | -3.5 | 0.085 | 13/48 (CHP-212, RKO, …) | top dose only | position effect removed |
| [[Lumateperone (tosylate) (drug)]] 5 µM |  | 0.845× | -3.2 | 0.23 | 4/48 (MIA PaCa-2, NCI-H1573, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.04 per unit of S-phase module lfc, -0.03 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 6323. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[H4 (line)]] | wt | 20.6 | 0 | 2 | — | [[Temsirolimus (drug)]] 0.5 µM 0.116× (z -9.8) |
| [[KATO III (line)]] | alt | 12.4 | 1 (1 ⚠) | 1 (1 ⚠) | [[Dinaciclib (drug)]] 0.5 µM 5.76× (z +8.6) ⚠ toxic; transcription drop | [[Digitoxin (drug)]] 5 µM 0.153× (z -9.2) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[MIA PaCa-2 (line)]] | alt | 14.0 | 0 | 1 (1 ⚠) | — | [[Homoharringtonine (drug)]] 0.5 µM 0.169× (z -9.9) ⚠ cell-cycle shift, explains ~2% of this change |
| [[NCI-H1573 (line)]] | alt | 15.1 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.19× (z +9.6) ⚠ toxic; transcription drop | — |
| [[NCI-H460 (line)]] | wt | 16.0 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.14× (z +9.9) ⚠ toxic; transcription drop | — |
| [[PANC-1 (line)]] | alt | 16.2 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 2.82× (z +8.7) ⚠ toxic; transcription drop | — |
| [[SK-MEL-2 (line)]] | alt | 18.9 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.298× (z -8.7) ⚠ cell-cycle shift, would explain all of this change |
| [[SW480 (line)]] | alt | 15.9 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 3.42× (z +9.5) ⚠ toxic; transcription drop | — |
| [[A-172 (line)]] | wt | 19.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 35.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 15.7 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 19.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 20.2 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 12.1 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 22.0 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 20.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 14.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 23.2 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 18.0 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 16.0 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 12.4 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.4 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 13.9 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 13.0 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 20.0 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 9.91 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 39.1 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 22.1 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 16.8 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 23.3 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 12.2 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 22.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 15.8 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 18.2 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 21.9 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 15.2 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 13.5 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 18.3 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.8 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 21.4 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 11.3 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 13.7 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 6323), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*92 of its nearest partners move with it, 2 of them with an alert (⚠; 1 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ZBTB47-AS1]] | +0.64 | +0.50 / +0.68 | both halves | 1e-05 |  |
| [[ZNF451-AS1]] | +0.60 | +0.60 / +0.64 | both halves | 7e-06 |  |
| [[CNGB3]] | +0.59 | +0.59 / +0.52 | both halves | 1e-05 |  |
| [[TICAM2-AS1]] | +0.56 | +0.55 / +0.53 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | +0.56 | +0.62 / +0.49 | both halves | 1e-05 |  |
| [[GEMIN7-AS1]] | +0.56 | +0.57 / +0.53 | both halves | 1e-05 |  |
| [[CSMD1]] | +0.56 | +0.47 / +0.55 | both halves | 2e-05 |  |
| [[ABHD15-AS1]] | +0.56 | +0.49 / +0.58 | both halves | 1e-05 |  |
| [[PLCG1-AS1]] | +0.56 | +0.64 / +0.45 | both halves | 3e-05 |  |
| [[TCEA2]] | +0.55 | +0.48 / +0.66 | both halves | 2e-05 |  |
| [[FLJ40194]] | +0.55 | +0.50 / +0.52 | both halves | 1e-05 |  |
| [[SPTBN1-AS2]] | +0.55 | +0.47 / +0.53 | both halves | 2e-05 |  |

## Genes that move opposite

*8 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[APEX2]] | -0.49 | -0.45 / -0.40 | both halves | 4e-05 |  |
| [[DCLRE1B]] | -0.48 | -0.32 / -0.48 | both halves | 2e-04 |  |
| [[FADD]] | -0.47 | -0.25 / -0.52 | both halves | 4e-04 |  |
| [[DCTPP1]] | -0.46 | -0.37 / -0.41 | both halves | 8e-05 |  |
| [[C1orf116]] | -0.46 | -0.50 / -0.39 | both halves | 6e-05 |  |
| [[MIS18A]] | -0.46 | -0.33 / -0.44 | both halves | 1e-04 |  |
| [[GEMIN4]] | -0.45 | -0.34 / -0.43 | both halves | 1e-04 |  |
| [[ARF6]] | -0.45 | -0.35 / -0.51 | both halves | 1e-04 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*3 arrows, 3 of them with an alert ⚠; grade A 0, B 3, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[C1orf116]] | B | C1orf116 activity lowers MAP3K12's level | lines that do not express C1orf116 (31) vs lines expressing it (19) | 1.41× higher at baseline in the lines without C1orf116 | 0.008 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125 |
| [[CERCAM]] | B | CERCAM activity raises MAP3K12's level | lines that do not express CERCAM (9) vs lines expressing it (41) | 1.44× lower at baseline in the lines without CERCAM | 0.048 | ⚠ within organs, on part of the lines; also absent: FGD1, EBF4, STARD9 |
| [[C1orf116]] | B | C1orf116 activity weakens MAP3K12's drug response | lines that do not express C1orf116 (31) vs lines expressing it (17) | the lines without C1orf116 respond 1.07× as strongly (z diff -0.17); strongest at Cepharanthine 5 µM: 1.42x vs 0.92x (z diff -3.0) | 0.099 | ⚠ within organs, on part of the lines; co-absent genes; also absent: ST14, TMPRSS4, TMEM125; target measured in part of the lines; both ways |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 021]]; 188 genes; every member is in the + arm (projection on the module's main direction 0.553). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (13.3, 26.2); signed map (33.5, 3.4). **Vector** length 60.1, 9.07% of its response variance represented; |z| ≥ 3 in 655 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | +6.7 | +12.3 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | +6.4 | +11.5 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | +5.8 | +8.7 |
|  | [[Tucidinostat (drug)]] 5 µM |  | +3.5 | +3.2 |
|  | [[Tucidinostat (drug)]] 0.5 µM |  | +3.3 | +3.6 |
|  | [[GSK1059615 (drug)]] 5 µM |  | +1.4 | -0.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | +1.3 | +1.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.3 | +0.2 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | +1.2 | +2.0 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -3.8 | -3.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -2.2 | -1.1 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -1.8 | -1.5 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.7 | -1.7 |
|  | [[Daptomycin (drug)]] 0.5 µM | ⚠ unreliable plate only | -1.7 | -0.6 |
|  | [[Peretinoin (drug)]] 0.5 µM |  | -1.5 | -1.4 |
|  | [[Vinblastine (sulfate) (drug)]] 0.5 µM |  | -1.4 | -0.5 |

## What is on record

|  |  |
|---|---|
| Name | mitogen-activated protein kinase kinase kinase 12 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 12q13.13 — chr12:53,479,669-53,500,063 (-) |
| Ensembl biotype | protein_coding |
| Also known as | MUK, DLK, ZPKP1, MEKK12; previously ZPK |
| Gene groups (HGNC) | Mitogen-activated protein kinase kinase kinases; Mixed lineage kinase family |
| Matched by | ensembl_id |

**Function**, from UniProt [Q12852](https://www.uniprot.org/uniprotkb/Q12852) (Mitogen-activated protein kinase kinase kinase 12):

> Part of a non-canonical MAPK signaling pathway. Activated by APOE, enhances the AP-1-mediated transcription of APP, via a MAP kinase signal transduction pathway composed of MAP2K7 and MAPK1/ERK2 and MAPK3/ERK1. May be an activator of the JNK/SAPK pathway.

**Summary**, from NCBI Gene [7786](https://www.ncbi.nlm.nih.gov/gene/7786):

> This gene encodes a member of the serine/threonine protein kinase family. This kinase contains a leucine-zipper domain and is predominately expressed in neuronal cells. The phosphorylation state of this kinase in synaptic terminals was shown to be regulated by membrane depolarization via calcineurin. This kinase forms heterodimers with leucine zipper containing transcription factors, such as cAMP responsive element binding protein (CREB) and MYC, and thus may play a regulatory role in PKA or …

**Accessions** — [HGNC:6851](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6851) · Entrez [7786](https://www.ncbi.nlm.nih.gov/gene/7786) · UniProt [Q12852](https://www.uniprot.org/uniprotkb/Q12852) · Ensembl [ENSG00000139625](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000139625)

## Data

Gene col 6323: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 6323); `tables/drug_effects.parquet` (20 rows, flagged included); `relations/gene_relations.parquet` (col_a == 6323, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 6323]; `tensor/DDL_lfc|DDL_z.npy` [6323]; `embed/gene_vectors.npy` [6323]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 6323 or target_col == 6323). Every well: [[MAP3K12 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/MAP3K12.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
