---
symbol: "H2AX"
type: "gene"
col: 12014
ensembl_id: "ENSG00000188486"
name: "H2A.X variant histone"
location: "11q23.3"
module: 22
arm: "+"
pooled_cpm: 6.83
n_lines_expressing: 50
n_dd_up: 16
n_dd_down: 3
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/022"]
generated_by: "tahoemap"
---

# H2AX

*H2A.X variant histone* — 11q23.3

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 16 drug-doses (14 with an alert ⚠); the strongest is [[Homoharringtonine (drug)]] 5 µM: 2.38× (z +10.1, q 4e-21, up in 30 of 42 measured lines) ⚠ cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[Topotecan (hydrochloride) (drug)]] 0.5 µM: 1.51× (z +3.4, q 0.030, up in 14 of 47 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 11.8×, A498 5.02×, CFPAC-1 5.04×; ⚠ cell-cycle shift, explains ~51% of this change).
> Pooled over the cell lines (median), lowered significantly by 3 drug-doses (none with an alert); the strongest is [[Idarubicin (hydrochloride) (drug)]] 5 µM: 0.588× (z -6.2, q 3e-07, down in 26 of 43 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[NCAPH]] (+0.71, fdr 7e-06), [[MAD2L1]] (+0.70, fdr 7e-06), [[CCNA2]] (+0.69, fdr 7e-06); moves opposite to [[RHOQ-AS1]] (-0.62, fdr 7e-06), [[EOGT-DT]] (-0.61, fdr 1e-05), [[MRPL33]] (-0.61, fdr 2e-05).
> It is in [[Module 022]], a single-armed module (G2/M checkpoint).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 16 in all, 14 with an alert ⚠. 16 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 14 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 12014.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Homoharringtonine (drug)]] 5 µM in 3 lines (AsPC-1 11.8×, A498 5.02×, CFPAC-1 5.04×; ⚠ cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | **2.38×** | +10.1 | 4e-21 | 30/42 (AsPC-1, A498, …) | rises with dose | composition shift; position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | **2.53×** | +7.4 | 5e-11 | 23/32 (HT-29, SW480, …) | rises with dose | cell-cycle shift (explains ~6% here); position effect removed |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~46% of this change | **2.22×** | +6.6 | 9e-09 | 30/47 (SW480, NCI-H2347, …) | all doses, stronger at high dose | position effect removed |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~41% of this change | **2.17×** | +6.4 | 3e-08 | 33/47 (LOX-IMVI, SW480, …) | all doses, stronger at high dose | position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~56% of this change | **2.15×** | +6.3 | 4e-08 | 28/47 (PANC-1, SW1417, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | **1.98×** | +5.6 | 2e-06 | 25/46 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Belinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~59% of this change | **1.82×** | +4.9 | 7e-05 | 23/47 (SW480, KATO III, …) | top dose only |  |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~50% of this change | **1.80×** | +4.8 | 1e-04 | 20/46 (PANC-1, SW1417, …) | all doses, stronger at high dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~72% of this change | **1.76×** | +4.5 | 5e-04 | 19/46 (AsPC-1, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | **1.71×** | +4.4 | 6e-04 | 17/33 (PANC-1, Panc 03.27, …) | inconsistent across doses | low cells (technical?) |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~89% of this change | **1.60×** | +3.9 | 0.006 | 15/43 (SW1417, PANC-1, …) | all doses, stronger at high dose |  |
| [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~32% of this change | **1.60×** | +3.8 | 0.006 | 15/40 (HS-578T, C32, …) | rises with dose | position effect removed |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~43% of this change | **1.35×** | +3.5 | 0.021 | 10/48 (SW480, HT-29, …) | top dose only | position effect removed |
| [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | **1.51×** | +3.4 | 0.030 | 14/47 (J82, SW480, …) | rises with dose | cell-cycle shift (explains ~11% here); position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~75% of this change | **1.49×** | +3.1 | 0.065 | 10/31 (HS-578T, CFPAC-1, …) | top dose only | position effect removed |
| [[Retinoic acid (drug)]] 0.05 µM |  | **1.46×** | +3.1 | 0.067 | 8/47 (KATO III, LOX-IMVI, …) | inconsistent across doses | position effect removed |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 6 in all, none with an alert. 3 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 12014.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **0.588×** | -6.2 | 3e-07 | 26/43 (SW1417, NCI-H23, …) | top dose only | cell-cycle shift (explains ~0% here) |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | **0.582×** | -4.3 | 0.005 | 17/39 (HEC-1-A, C-33 A, …) | top dose only | cell-cycle shift (explains ~0% here); position effect removed |
| [[Cytarabine (hydrochloride) (drug)]] 0.5 µM |  | **0.645×** | -3.6 | 0.051 | 17/47 (NCI-H2030, SNU-423, …) | two highest doses | cell-cycle shift (explains ~9% here) |
| [[Saquinavir (drug)]] 5 µM |  | 0.751× | -3.4 | 0.10 | 19/44 (H4, LS 180, …) | top dose only |  |
| [[Celecoxib (drug)]] 0.5 µM |  | 0.596× | -3.1 | 0.22 | 16/44 (PANC-1, H4, …) | inconsistent across doses | noisy plate (z scaled) |
| [[Osimertinib (mesylate) (drug)]] 5 µM |  | 0.694× | -3.0 | 0.22 | 15/47 (LOX-IMVI, SW1417, …) | top dose only | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.47 per unit of S-phase module lfc, +0.53 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 12014. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[HEC-1-A (line)]] | alt | 8.10 | 0 | 2 | — | [[Doxorubicin (hydrochloride) (drug)]] 5 µM 0.0540× (z -11.7) |
| [[SHP-77 (line)]] | alt | 6.13 | 0 | 2 (1 ⚠) | — | [[Tolcapone (drug)]] 0.05 µM 0.0642× (z -9.2) |
| [[A498 (line)]] | wt | 3.95 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.02× (z +8.9) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[AsPC-1 (line)]] | alt | 3.71 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 11.8× (z +10.5) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[CFPAC-1 (line)]] | alt | 5.74 | 1 (1 ⚠) | 0 | [[Homoharringtonine (drug)]] 5 µM 5.04× (z +8.5) ⚠ cell-cycle shift, explains ~51% of this change | — |
| [[H4 (line)]] | wt | 10.4 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 0.05 µM 0.0444× (z -9.5) |
| [[NCI-H23 (line)]] | alt | 5.91 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.151× (z -9.6) |
| [[Panc 03.27 (line)]] | alt | 9.05 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.0966× (z -8.6) |
| [[SW1417 (line)]] | alt | 14.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.244× (z -9.8) |
| [[SW480 (line)]] | alt | 12.5 | 0 | 1 | — | [[Idarubicin (hydrochloride) (drug)]] 5 µM 0.324× (z -9.4) |
| [[A-172 (line)]] | wt | 4.24 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 3.69 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 7.19 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 6.20 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 7.37 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 2.71 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 4.57 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 3.44 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 3.03 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 6.12 | 0 | 0 | — | — |
| [[Hs 766T (line)]] | wt | 3.97 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 3.18 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 10.2 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 3.31 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 7.75 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 17.4 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 6.41 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 6.09 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 7.76 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 5.71 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 6.46 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 2.70 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 9.53 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 3.56 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 5.66 | 0 | 0 | — | — |
| [[NCI-H460 (line)]] | wt | 4.03 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 4.21 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 7.79 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 7.76 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 9.23 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 5.12 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 3.35 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 5.89 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 4.16 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 5.21 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 9.74 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 5.23 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.4 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 12014), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*85 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NCAPH]] | +0.71 | +0.71 / +0.65 | both halves | 7e-06 |  |
| [[MAD2L1]] | +0.70 | +0.64 / +0.70 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[CCNA2]] | +0.69 | +0.67 / +0.65 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 777 |
| [[SKA3]] | +0.68 | +0.68 / +0.64 | both halves | 7e-06 |  |
| [[ANLN]] | +0.68 | +0.65 / +0.64 | both halves | 7e-06 | STRING 421 |
| [[UBE2S]] | +0.67 | +0.59 / +0.69 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS |
| [[HASPIN]] | +0.67 | +0.71 / +0.67 | both halves | 7e-06 |  |
| [[ERCC6L]] | +0.67 | +0.74 / +0.59 | both halves | 7e-06 | pathway: Cell Cycle Checkpoints |
| [[KIF23]] | +0.67 | +0.67 / +0.61 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT; STRING 441 |
| [[MKI67]] | +0.67 | +0.71 / +0.59 | both halves | 7e-06 | pathway: HALLMARK_E2F_TARGETS; STRING 468 |
| [[ARHGAP11A]] | +0.66 | +0.66 / +0.62 | both halves | 7e-06 |  |
| [[KIF11]] | +0.65 | +0.66 / +0.63 | both halves | 7e-06 | pathway: HALLMARK_G2M_CHECKPOINT |

## Genes that move opposite

*15 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest and the 1 next strongest without an alert.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[RHOQ-AS1]] | -0.62 | -0.61 / -0.58 | both halves | 7e-06 |  |
| [[EOGT-DT]] | -0.61 | -0.62 / -0.53 | both halves | 1e-05 |  |
| [[MRPL33]] | -0.61 | -0.48 / -0.63 | both halves | 2e-05 |  |
| [[GOLGA8B]] | -0.60 | -0.47 / -0.64 | both halves | 2e-05 |  |
| [[BIRC6-AS2-1]] | -0.59 | -0.51 / -0.59 | both halves | 1e-05 |  |
| [[RFNG]] | -0.58 | -0.40 / -0.64 | both halves | 5e-05 | pathway: Pre-NOTCH Expression and Processing |
| [[TICAM2-AS1]] | -0.57 | -0.51 / -0.54 | both halves | 1e-05 |  |
| [[NSA2]] | -0.57 | -0.59 / -0.52 | both halves | 1e-05 |  |
| [[CTBP1-AS]] ⚠ | -0.56 | -0.45 / -0.58 | both halves | 3e-05 | ⚠ in the vector space only through flagged drug-doses |
| [[ATP6V1E1]] | -0.56 | -0.50 / -0.55 | both halves | 1e-05 |  |
| [[C2CD5-AS1]] | -0.56 | -0.49 / -0.49 | both halves | 1e-05 |  |
| [[PIN4]] | -0.55 | -0.41 / -0.53 | both halves | 4e-05 |  |
| [[ZRANB2-AS1]] | -0.55 | -0.48 / -0.48 | both halves | 2e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 022]] — G2/M checkpoint; 185 genes; every member is in the + arm (projection on the module's main direction 0.627). A single-armed module: the two sides of its main direction do not form two opposite arms (mean cos between them -0.26; a − arm needs ≥ 5 genes on its side and a mean cos ≤ -0.2), so all its genes count as +.
- **Nodal map** (x, y) = (-37.3, -53.6); signed map (-47.0, -43.6). **Vector** length 89.9, 18.5% of its response variance represented; |z| ≥ 3 in 1,092 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *DREAM G2/M down* (control, mean cos +0.55 to 28); *Resolution of Sister Chromatid Cohesion* (reactome, mean cos +0.50 to 33); *Mitotic Spindle Checkpoint* (reactome, mean cos +0.50 to 31).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic | +3.3 | +7.4 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~61% of this change | +2.8 | +4.4 |
|  | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~51% of this change | +2.7 | +10.1 |
|  | [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~45% of this change | +2.6 | +5.6 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.5 µM |  | +2.6 | +3.4 |
|  | [[Filgotinib (drug)]] 5 µM |  | +2.3 | +2.5 |
|  | [[Retinoic acid (drug)]] 0.05 µM |  | +2.1 | +3.1 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.8 | +2.7 |
|  | [[Palmatine (chloride) (drug)]] 0.05 µM |  | +1.6 | +1.4 |
|  | [[Busulfan (drug)]] 0.05 µM |  | +1.4 | +0.7 |
| fall | [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | -6.3 | -6.2 |
|  | [[Doxorubicin (hydrochloride) (drug)]] 5 µM |  | -5.3 | -4.3 |
|  | [[Epirubicin (hydrochloride) (drug)]] 5 µM |  | -4.8 | -2.8 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.5 | -0.5 |
|  | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift | -2.9 | -2.1 |
|  | [[Ipatasertib (drug)]] 0.5 µM |  | -2.8 | -2.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -2.1 |
|  | [[Verteporfin (drug)]] 5 µM |  | -2.3 | -2.3 |
|  | [[Celecoxib (drug)]] 0.5 µM |  | -2.2 | -3.1 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | -2.1 | -1.5 |

## What is on record

|  |  |
|---|---|
| Name | H2A.X variant histone |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 11q23.3 — chr11:119,093,874-119,095,465 (-) |
| Ensembl biotype | protein_coding |
| Also known as | ; previously H2AFX |
| Gene groups (HGNC) | H2A histones |
| Hallmark sets | UNFOLDED_PROTEIN_RESPONSE, UV_RESPONSE_UP, G2M_CHECKPOINT, E2F_TARGETS |
| Reactome | 122 pathways, smallest: Replacement of protamines by nucleosomes in the male pronucleus; ChAHP complex assembly; DNA methylation |
| Matched by | ensembl_id |

**Function**, from UniProt [P16104](https://www.uniprot.org/uniprotkb/P16104) (Histone H2AX):

> Variant histone H2A which replaces conventional H2A in a subset of nucleosomes. Nucleosomes wrap and compact DNA into chromatin, limiting DNA accessibility to the cellular machineries which require DNA as a template. Histones thereby play a central role in transcription regulation, DNA repair, DNA replication and chromosomal stability. DNA accessibility is regulated via a complex set of post-translational modifications of histones, also called histone code, and nucleosome remodeling. Required …

**Summary**, from NCBI Gene [3014](https://www.ncbi.nlm.nih.gov/gene/3014):

> Histones are basic nuclear proteins that are responsible for the nucleosome structure of the chromosomal fiber in eukaryotes. Two molecules of each of the four core histones (H2A, H2B, H3, and H4) form an octamer, around which approximately 146 bp of DNA is wrapped in repeating units, called nucleosomes. The linker histone, H1, interacts with linker DNA between nucleosomes and functions in the compaction of chromatin into higher order structures. This gene encodes a replication-independent …

**Accessions** — [HGNC:4739](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:4739) · Entrez [3014](https://www.ncbi.nlm.nih.gov/gene/3014) · UniProt [P16104](https://www.uniprot.org/uniprotkb/P16104) · Ensembl [ENSG00000188486](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000188486)

## Data

Gene col 12014: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 12014); `tables/drug_effects.parquet` (22 rows, flagged included); `relations/gene_relations.parquet` (col_a == 12014, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 12014]; `tensor/DDL_lfc|DDL_z.npy` [12014]; `embed/gene_vectors.npy` [12014]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 12014 or target_col == 12014). Every well: [[H2AX — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/H2AX.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
