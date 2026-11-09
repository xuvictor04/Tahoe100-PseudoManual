---
symbol: "GOT1"
type: "gene"
col: 4153
ensembl_id: "ENSG00000120053"
name: "glutamic-oxaloacetic transaminase 1"
location: "10q24.2"
module: 63
arm: "+"
pooled_cpm: 67.99
n_lines_expressing: 50
n_dd_up: 26
n_dd_down: 11
n_dd_up_clean: 24
n_dd_down_clean: 8
in_vector_space: true
direction_upstream: 1
direction_downstream: 0
tags: ["gene", "module/063"]
generated_by: "tahoemap"
---

# GOT1

*glutamic-oxaloacetic transaminase 1* — 10q24.2

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 26 drug-doses (2 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +10.7, q 6e-24, up in 41 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (3 with an alert ⚠); the strongest is [[Harringtonine (drug)]] 0.5 µM: 0.606× (z -5.8, q 5e-06, down in 30 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[ASNS]] (+0.82, fdr 7e-06), [[SESN2]] (+0.82, fdr 7e-06), [[CHAC1]] (+0.82, fdr 7e-06).
> It is in [[Module 063]], a single-armed module (ISR ATF4).
> Probable direction (from the cell lines, not proof of direct regulation): 1 arrow points to it, the strongest [[CTH]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 26 in all, 2 with an alert ⚠; shown: the 15 strongest and the 1 next strongest without an alert. 26 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 4153.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +10.7 | 6e-24 | 41/48 (SW480, NCI-H460, …) | all doses, stronger at high dose | cell-cycle shift (explains ~18% here) |
| [[Artesunate (drug)]] 5 µM |  | **1.89×** | +10.3 | 2e-22 | 39/48 (SNU-1, SW480, …) | rises with dose | cell-cycle shift (explains ~0% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.37×** | +9.9 | 1e-20 | 42/48 (SW480, A549, …) | all doses, stronger at high dose | cell-cycle shift (explains ~17% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.16×** | +8.8 | 2e-16 | 40/48 (SW480, A549, …) | rises with dose | cell-cycle shift (explains ~20% here) |
| [[Auranofin (drug)]] 5 µM |  | **2.10×** | +8.5 | 3e-15 | 40/48 (LOX-IMVI, LoVo, …) | top dose only |  |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **2.04×** | +8.1 | 4e-14 | 38/48 (SNU-423, AsPC-1, …) | inconsistent across doses |  |
| [[Artesunate (drug)]] 0.5 µM |  | **2.02×** | +8.0 | 7e-14 | 38/48 (SNU-1, SW480, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 5 µM |  | **1.69×** | +6.0 | 2e-07 | 36/47 (C32, NCI-H460, …) | rises with dose |  |
| [[5-Azacytidine (drug)]] 5 µM |  | **1.66×** | +5.8 | 4e-07 | 35/47 (C-33 A, SW480, …) | top dose only |  |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **1.57×** | +5.2 | 1e-05 | 31/48 (NCI-H2030, SW480, …) | two highest doses |  |
| [[Abemaciclib (drug)]] 5 µM |  | **2.27×** | +4.9 | 5e-05 | 32/48 (NCI-H460, A-427, …) | rises with dose | noisy plate (z scaled) |
| [[venetoclax (drug)]] 5 µM |  | **2.08×** | +4.4 | 5e-04 | 29/47 (PANC-1, LOX-IMVI, …) | top dose only | noisy plate (z scaled) |
| [[Neratinib (maleate) (drug)]] 5 µM |  | **1.31×** | +4.4 | 5e-04 | 27/48 (LoVo, A-427, …) | rises with dose |  |
| [[Dihydroartemisinin (drug)]] 0.5 µM |  | **1.46×** | +4.3 | 6e-04 | 28/48 (SNU-1, C-33 A, …) | rises with dose |  |
| [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | **1.30×** | +4.2 | 0.001 | 23/49 (SNU-1, A-427, …) | top dose only |  |
| [[Neratinib (maleate) (drug)]] 0.5 µM |  | **1.42×** | +4.0 | 0.002 | 26/48 (LoVo, SNU-1, …) | rises with dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 3 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 4153.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Harringtonine (drug)]] 0.5 µM |  | **0.606×** | -5.8 | 5e-06 | 30/48 (PANC-1, HT-29, …) | inconsistent across doses | cell-cycle shift (explains ~0% here) |
| [[Harringtonine (drug)]] 0.05 µM |  | **0.588×** | -5.6 | 5e-06 | 29/47 (LoVo, A-427, …) | inconsistent across doses | low cells (technical?) |
| [[Homoharringtonine (drug)]] 0.05 µM |  | **0.621×** | -5.0 | 9e-05 | 29/48 (PANC-1, A-427, …) | inconsistent across doses |  |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.649×** | -5.0 | 9e-05 | 28/48 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Cobimetinib (drug)]] 5 µM |  | **0.668×** | -4.5 | 9e-04 | 29/47 (HepG2/C3A, SW480, …) | rises with dose |  |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.672×** | -4.2 | 0.002 | 24/44 (PANC-1, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Trametinib (drug)]] 0.05 µM |  | **0.784×** | -3.9 | 0.008 | 29/48 (HepG2/C3A, SW480, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 0.05 µM |  | **0.732×** | -3.3 | 0.066 | 19/48 (KATO III, RKO, …) | inconsistent across doses |  |
| [[Bimiralisib (drug)]] 5 µM |  | **0.582×** | -3.2 | 0.073 | 20/50 (HepG2/C3A, A-427, …) | rises with dose | plate-row cell shift; noisy plate (z scaled) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.751×** | -3.2 | 0.083 | 21/46 (A-427, RKO, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.753×** | -3.2 | 0.083 | 22/41 (LoVo, HT-29, …) | all doses, flat | cell-cycle shift (explains ~0% here); composition shift |
| [[Pyridoxine (hydrochloride) (drug)]] 5 µM |  | 0.831× | -3.0 | 0.11 | 19/48 (HEC-1-A, NCI-H2347, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.29 per unit of S-phase module lfc, +0.00 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 4153. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HepG2_C3A (line)]] | wt | 220 | 0 | 13 (4 ⚠) | — | [[Homoharringtonine (drug)]] 5 µM 0.203× (z -19.7) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Cobimetinib (drug)]] 5 µM 0.166× (z -15.1) |
| [[PANC-1 (line)]] | alt | 236 | 0 | 10 (8 ⚠) | — | [[Harringtonine (drug)]] 0.5 µM 0.144× (z -15.2) |
| [[A-427 (line)]] | wt | 147 | 2 | 7 (4 ⚠) | [[Chlorhexidine (diacetate) (drug)]] 5 µM 2.05× (z +9.0) | [[Homoharringtonine (drug)]] 5 µM 0.332× (z -13.9) ⚠ cell-cycle shift, explains ~0% of this change · without an alert: [[Homoharringtonine (drug)]] 0.05 µM 0.265× (z -10.9) |
| [[HT-29 (line)]] | alt | 136 | 0 | 6 (5 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.190× (z -12.3) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.224× (z -11.0) |
| [[LoVo (line)]] | wt | 93.0 | 3 | 3 (1 ⚠) | [[Auranofin (drug)]] 5 µM 3.69× (z +10.7) | [[Dinaciclib (drug)]] 5 µM 0.146× (z -15.1) ⚠ toxic; transcription drop · without an alert: [[Harringtonine (drug)]] 0.5 µM 0.261× (z -11.0) |
| [[SW480 (line)]] | alt | 64.4 | 5 | 1 (1 ⚠) | [[Panobinostat (drug)]] 5 µM 3.13× (z +11.8) | [[Dinaciclib (drug)]] 5 µM 0.357× (z -10.3) ⚠ toxic; transcription drop |
| [[HOP62 (line)]] | alt | 46.6 | 4 (1 ⚠) | 0 | [[Panobinostat (drug)]] 0.5 µM 3.18× (z +9.4) | — |
| [[SNU-1 (line)]] | wt | 63.0 | 4 | 0 | [[Artesunate (drug)]] 5 µM 4.88× (z +13.5) | — |
| [[A549 (line)]] | wt | 28.3 | 3 | 0 | [[Panobinostat (drug)]] 0.5 µM 4.75× (z +9.8) | — |
| [[LOX-IMVI (line)]] | wt | 23.9 | 3 | 0 | [[Auranofin (drug)]] 5 µM 5.67× (z +11.1) | — |
| [[AsPC-1 (line)]] | alt | 37.4 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 4.40× (z +8.9) | — |
| [[HCT15 (line)]] | alt | 75.2 | 2 | 0 | [[Artesunate (drug)]] 5 µM 2.94× (z +9.9) | — |
| [[NCI-H460 (line)]] | wt | 39.0 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 3.85× (z +10.1) | — |
| [[RKO (line)]] | wt | 53.9 | 1 | 1 (1 ⚠) | [[Artesunate (drug)]] 5 µM 2.88× (z +8.5) | [[Homoharringtonine (drug)]] 5 µM 0.306× (z -9.4) ⚠ cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 75.0 | 2 (1 ⚠) | 0 | [[Digitoxin (drug)]] 5 µM 2.86× (z +8.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~69% of this change · without an alert: [[Artesunate (drug)]] 5 µM 2.05× (z +8.5) | — |
| [[SW48 (line)]] | wt | 86.9 | 2 | 0 | [[Artesunate (drug)]] 5 µM 3.19× (z +9.9) | — |
| [[C-33 A (line)]] | alt | 37.5 | 1 | 0 | [[5-Azacytidine (drug)]] 5 µM 8.08× (z +12.1) | — |
| [[C32 (line)]] | wt | 27.4 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.91× (z +10.2) | — |
| [[J82 (line)]] | alt | 24.9 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.45× (z +8.5) | — |
| [[KATO III (line)]] | alt | 73.8 | 0 | 1 | — | [[Harringtonine (drug)]] 0.5 µM 0.248× (z -8.8) |
| [[NCI-H2030 (line)]] | alt | 59.6 | 1 | 0 | [[Artesunate (drug)]] 5 µM 3.12× (z +9.4) | — |
| [[Panc 03.27 (line)]] | alt | 43.5 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 3.31× (z +12.6) ⚠ cell-cycle shift, explains ~0% of this change | — |
| [[SW 900 (line)]] | alt | 47.8 | 1 | 0 | [[Auranofin (drug)]] 5 µM 3.08× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 115 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.05 µM 0.317× (z -8.6) ⚠ toxic; transcription drop |
| [[A-172 (line)]] | wt | 29.0 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 52.7 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 65.7 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 42.9 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 43.1 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 26.6 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 58.1 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 63.2 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 39.9 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 34.6 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 41.4 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 23.7 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 59.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 86.7 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 52.2 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 32.3 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 49.1 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 61.0 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 58.7 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 64.3 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 35.7 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 48.4 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 50.7 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 35.8 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 23.2 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 4153), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*100 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[ASNS]] | +0.82 | +0.82 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 969 |
| [[SESN2]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[CHAC1]] | +0.82 | +0.72 / +0.83 | both halves | 7e-06 | **novel candidate** |
| [[CARS1]] | +0.81 | +0.77 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[TRIB3]] | +0.81 | +0.73 / +0.82 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[GARS1]] | +0.80 | +0.77 / +0.79 | both halves | 7e-06 |  |
| [[AARS1]] | +0.75 | +0.74 / +0.76 | both halves | 7e-06 |  |
| [[GPT2]] | +0.74 | +0.70 / +0.70 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 984 |
| [[MARS1]] | +0.74 | +0.72 / +0.73 | both halves | 7e-06 | pathway: Metabolism of amino acids and derivatives; STRING 466 |
| [[MTHFD2]] | +0.73 | +0.76 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |
| [[PHGDH]] | +0.73 | +0.73 / +0.72 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING; STRING 444 |
| [[SLC1A4]] | +0.73 | +0.69 / +0.74 | both halves | 7e-06 | pathway: HALLMARK_MTORC1_SIGNALING |

## Genes that move opposite

None among its nearest partners: everything close to it moves the same way.

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*1 arrow, 1 of them with an alert ⚠; grade A 0, B 1, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[CTH]] | B | CTH activity raises GOT1's level | lines that do not express CTH (6) vs lines expressing it (44) | 1.68× lower at baseline in the lines without CTH | 0.080 | ⚠ within organs, on part of the lines; also absent: SLC35F2, POLR3G; maybe low, not absent |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 063]] — ISR ATF4; 77 genes; every member is in the + arm (projection on the module's main direction 0.821). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.33; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-17.4, 48.6); signed map (-12.9, 25.0). **Vector** length 151, 52.7% of its response variance represented; |z| ≥ 3 in 1,315 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *ISR ATF4* (control, mean cos +0.71 to 16); *Cytosolic tRNA aminoacylation* (reactome, mean cos +0.70 to 9); *tRNA Aminoacylation* (reactome, mean cos +0.70 to 9).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Artesunate (drug)]] 5 µM |  | +9.7 | +10.3 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +8.7 | +5.8 |
|  | [[Artesunate (drug)]] 0.5 µM |  | +6.6 | +8.0 |
|  | [[Neratinib (maleate) (drug)]] 0.5 µM |  | +6.4 | +4.0 |
|  | [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | +6.3 | +8.1 |
|  | [[Auranofin (drug)]] 5 µM |  | +6.3 | +8.5 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | +6.1 | +4.4 |
|  | [[Chlorhexidine (diacetate) (drug)]] 5 µM |  | +5.5 | +4.2 |
| fall | [[Harringtonine (drug)]] 0.5 µM |  | -7.0 | -5.8 |
|  | [[Homoharringtonine (drug)]] 0.05 µM |  | -6.5 | -5.0 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | -5.7 | -4.2 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.7 | -1.2 |
|  | [[Harringtonine (drug)]] 0.05 µM |  | -5.5 | -5.6 |
|  | [[Cobimetinib (drug)]] 5 µM |  | -4.5 | -4.5 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -4.3 | -2.5 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -4.0 | -2.7 |

## What is on record

|  |  |
|---|---|
| Name | glutamic-oxaloacetic transaminase 1 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 10q24.2 — chr10:99,396,870-99,430,624 (-) |
| Ensembl biotype | protein_coding |
| Also known as | AST1, SGOT, AST |
| Gene groups (HGNC) | Glutamic-oxaloacetic transaminase family |
| Hallmark sets | GLYCOLYSIS, MTORC1_SIGNALING |
| Reactome | 7 pathways, smallest: Aspartate and asparagine metabolism; Methionine salvage pathway; Malate-aspartate shuttle |
| Matched by | ensembl_id |

**Function**, from UniProt [P17174](https://www.uniprot.org/uniprotkb/P17174) (Aspartate aminotransferase, cytoplasmic):

> Biosynthesis of L-glutamate from L-aspartate or L-cysteine. Important regulator of levels of glutamate, the major excitatory neurotransmitter of the vertebrate central nervous system. Acts as a scavenger of glutamate in brain neuroprotection. The aspartate aminotransferase activity is involved in hepatic glucose synthesis during development and in adipocyte glyceroneogenesis. Using L-cysteine as substrate, regulates levels of mercaptopyruvate, an important source of hydrogen sulfide. …

**Summary**, from NCBI Gene [2805](https://www.ncbi.nlm.nih.gov/gene/2805):

> Glutamic-oxaloacetic transaminase is a pyridoxal phosphate-dependent enzyme which exists in cytoplasmic and mitochondrial forms, GOT1 and GOT2, respectively. GOT plays a role in amino acid metabolism and the urea and tricarboxylic acid cycles. The two enzymes are homodimeric and show close homology. [provided by RefSeq, Jul 2008]

**Accessions** — [HGNC:4432](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4432) · Entrez [2805](https://www.ncbi.nlm.nih.gov/gene/2805) · UniProt [P17174](https://www.uniprot.org/uniprotkb/P17174) · Ensembl [ENSG00000120053](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000120053)

## Data

Gene col 4153: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 4153); `tables/drug_effects.parquet` (38 rows, flagged included); `relations/gene_relations.parquet` (col_a == 4153, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 4153]; `tensor/DDL_lfc|DDL_z.npy` [4153]; `embed/gene_vectors.npy` [4153]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 4153 or target_col == 4153). Every well: [[GOT1 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/GOT1.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
