---
symbol: "NCAPH2"
type: "gene"
col: 364
ensembl_id: "ENSG00000025770"
name: "non-SMC condensin II complex subunit H2"
location: "22q13.33"
module: 6
arm: "+"
pooled_cpm: 9.92
n_lines_expressing: 50
n_dd_up: 13
n_dd_down: 10
n_dd_up_clean: 2
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/006"]
generated_by: "tahoemap"
---

# NCAPH2

*non-SMC condensin II complex subunit H2* — 22q13.33

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 13 drug-doses (11 with an alert ⚠); the strongest is [[Dinaciclib (drug)]] 0.5 µM: 2.15× (z +11.4, q 3e-27, up in 23 of 33 measured lines) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 2.80× (z +8.0, q 2e-13, up in 32 of 46 measured lines).
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).
> Pooled over the cell lines (median), lowered significantly by 10 drug-doses (7 with an alert ⚠); the strongest is [[Tucidinostat (drug)]] 5 µM: 0.785× (z -5.1, q 1e-04, down in 21 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 2 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[MCM2]] (+0.82, fdr 7e-06), [[RECQL4]] (+0.81, fdr 7e-06), [[HAUS5]] (+0.78, fdr 7e-06); moves opposite to [[NACA4P]] (-0.60, fdr 1e-05, ⚠ NACA4P in the vector space only through flagged drug-doses).
> It sits in the **+** arm of [[Module 006]] (E2F targets).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 15 in all, 13 with an alert ⚠. 13 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 11 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 364.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 1 here, 1 with an alert ⚠; `tables/drug_line_top.parquet`), these raise it: [[Dinaciclib (drug)]] 0.5 µM in 1 line (NCI-H460 4.91×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change).

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | **2.15×** | +11.4 | 3e-27 | 23/33 (NCI-H460, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | **2.12×** | +10.3 | 1e-22 | 18/28 (HEC-1-A, PANC-1, …) | all doses, flat | composition shift; position effect removed |
| [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | **1.78×** | +8.2 | 5e-14 | 10/17 (SW480, SNU-423, …) | all doses, flat | composition shift; position effect removed |
| [[TAK-901 (drug)]] 5 µM |  | **2.80×** | +8.0 | 2e-13 | 32/46 (SW480, RKO, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~14% here); composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **1.48×** | +5.8 | 8e-07 | 22/47 (SHP-77, SW480, …) | rises with dose | composition shift |
| [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | **1.46×** | +5.6 | 2e-06 | 19/47 (RKO, SW480, …) | rises with dose | position effect removed |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~62% of this change | **1.44×** | +5.4 | 5e-06 | 19/45 (SW480, NCI-H460, …) | rises with dose |  |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~49% of this change | **1.40×** | +5.0 | 5e-05 | 15/46 (PANC-1, SHP-77, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~87% of this change | **1.39×** | +4.9 | 7e-05 | 16/47 (NCI-H460, LoVo, …) | rises with dose | position effect removed |
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~58% of this change | **1.34×** | +4.2 | 0.002 | 14/38 (LoVo, SNU-423, …) | top dose only | position effect removed |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.09× | +4.1 | 0.002 | 1/48 (Hs 766T) | inconsistent across doses |  |
| [[PH-797804 (drug)]] 5 µM |  | **1.67×** | +4.0 | 0.004 | 15/43 (LS 180, HEC-1-A, …) | rises with dose | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~69% of this change | **1.21×** | +3.9 | 0.004 | 18/44 (NCI-H460, NCI-H1573, …) | top dose only | composition shift |
| [[Lonafarnib (drug)]] 5 µM | ⚠ toxic | **1.57×** | +3.5 | 0.018 | 4/21 (HEC-1-A, SNU-423, …) | top dose only | noisy plate (z scaled) |
| [[Raltitrexed (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~58% of this change | 1.17× | +3.3 | 0.043 | 6/48 (RKO, J82, …) | rises with dose |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 12 in all, 7 with an alert ⚠. 10 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 7 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 364.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Tucidinostat (drug)]] 5 µM |  | **0.785×** | -5.1 | 1e-04 | 21/48 (A498, LS 180, …) | rises with dose |  |
| [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | **0.787×** | -5.1 | 1e-04 | 23/48 (A498, hTERT-HPNE, …) | all doses, stronger at high dose | low cells (technical?) |
| [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | **0.716×** | -5.0 | 1e-04 | 22/45 (Hs 766T, A498, …) | all doses, stronger at high dose |  |
| [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | **0.744×** | -4.2 | 0.004 | 14/44 (NCI-H23, HCT15, …) | inconsistent across doses |  |
| [[palbociclib (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~55% of this change | **0.716×** | -3.6 | 0.041 | 7/48 (LOX-IMVI, KATO III, …) | two highest doses | noisy plate (z scaled); position effect removed |
| [[Carbidopa (monohydrate) (drug)]] 0.05 µM | ⚠ unreliable plate only; position not correctable | **0.794×** | -3.5 | 0.046 | 7/47 (SHP-77, NCI-H23, …) | inconsistent across doses |  |
| [[Temsirolimus (drug)]] 5 µM |  | 0.851× | -3.4 | 0.046 | 12/48 (A549, NCI-H23, …) | top dose only | position effect removed |
| [[Cobimetinib (drug)]] 5 µM |  | **0.794×** | -3.3 | 0.061 | 13/45 (SNU-1, C-33 A, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | **0.804×** | -3.3 | 0.063 | 12/45 (SHP-77, C32, …) | rises with dose |  |
| [[Selinexor (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~54% of this change | **0.808×** | -3.2 | 0.078 | 9/48 (SW 1271, SW480, …) | all doses, stronger at high dose |  |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **0.810×** | -3.2 | 0.079 | 5/47 (NCI-H23, AsPC-1, …) | top dose only |  |
| [[Trametinib (drug)]] 0.5 µM |  | 0.837× | -3.1 | 0.11 | 11/48 (NCI-H23, HCT15, …) | inconsistent across doses | noisy plate (z scaled); position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.48 per unit of S-phase module lfc, +0.08 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 364. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[BT-474 (line)]] | alt | 8.54 | 0 | 1 | — | [[Bosentan (hydrate) (drug)]] 0.05 µM 0.104× (z -8.6) |
| [[Hs 766T (line)]] | wt | 8.82 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 0.5 µM 0.142× (z -8.8) ⚠ cell-cycle shift, explains ~53% of this change |
| [[NCI-H23 (line)]] | alt | 9.92 | 0 | 1 | — | [[Dapagliflozin ((2S)-1,2-propanediol, hydrate) (drug)]] 0.05 µM 0.161× (z -8.6) |
| [[NCI-H460 (line)]] | wt | 6.20 | 1 (1 ⚠) | 0 | [[Dinaciclib (drug)]] 0.5 µM 4.91× (z +8.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | — |
| [[A-172 (line)]] | wt | 7.88 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 9.69 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 14.6 | 0 | 0 | — | — |
| [[A549 (line)]] | wt | 7.40 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[C32 (line)]] | wt | 10.1 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 11.0 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 7.61 | 0 | 0 | — | — |
| [[COLO 205 (line)]] | alt | 10.6 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 9.54 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 13.7 | 0 | 0 | — | — |
| [[HEC-1-A (line)]] | alt | 15.9 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 5.83 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 8.17 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 15.6 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 6.21 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 6.47 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 9.94 | 0 | 0 | — | — |
| [[KATO III (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[LoVo (line)]] | wt | 9.16 | 0 | 0 | — | — |
| [[LOX-IMVI (line)]] | wt | 5.06 | 0 | 0 | — | — |
| [[LS 180 (line)]] | wt | 8.64 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 6.04 | 0 | 0 | — | — |
| [[NCI-H1573 (line)]] | alt | 17.9 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 6.79 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 12.6 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 9.30 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 10.7 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 9.85 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 11.6 | 0 | 0 | — | — |
| [[Panc 03.27 (line)]] | alt | 6.77 | 0 | 0 | — | — |
| [[PANC-1 (line)]] | alt | 6.49 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.4 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 10.5 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 27.2 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 6.07 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 7.38 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 8.28 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 8.25 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 8.39 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 8.21 | 0 | 0 | — | — |
| [[SW1417 (line)]] | alt | 9.12 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 9.86 | 0 | 0 | — | — |
| [[SW480 (line)]] | alt | 9.55 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 364), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*99 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[MCM2]] | +0.82 | +0.78 / +0.81 | both halves | 7e-06 | **novel candidate** |
| [[RECQL4]] | +0.81 | +0.80 / +0.80 | both halves | 7e-06 | **novel candidate** |
| [[HAUS5]] | +0.78 | +0.72 / +0.76 | both halves | 7e-06 | **novel candidate** |
| [[TONSL]] | +0.76 | +0.70 / +0.79 | both halves | 7e-06 |  |
| [[MCM4]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[MYBL2]] | +0.76 | +0.69 / +0.77 | both halves | 7e-06 |  |
| [[MCM5]] | +0.76 | +0.71 / +0.80 | both halves | 7e-06 |  |
| [[POLE]] | +0.75 | +0.69 / +0.76 | both halves | 7e-06 |  |
| [[ZWINT]] | +0.74 | +0.70 / +0.73 | both halves | 7e-06 |  |
| [[HAT1]] | +0.74 | +0.65 / +0.76 | both halves | 7e-06 |  |
| [[TCF19]] | +0.73 | +0.70 / +0.74 | both halves | 7e-06 |  |
| [[POLD1]] | +0.73 | +0.68 / +0.71 | both halves | 7e-06 |  |

## Genes that move opposite

*1 of its nearest partners move opposite, 1 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[NACA4P]] ⚠ | -0.60 | -0.51 / -0.64 | both halves | 1e-05 | ⚠ in the vector space only through flagged drug-doses |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 006]] — E2F targets; 236 genes; this gene is in the **+** arm (projection on the module's main direction 0.742). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.33).
- **Nodal map** (x, y) = (-35.1, -42.8); signed map (-36.1, -46.0). **Vector** length 72.8, 12.5% of its response variance represented; |z| ≥ 3 in 867 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *E2F targets* (hallmark, mean cos +0.58 to 65); *DNA strand elongation* (reactome, mean cos +0.61 to 28); *DNA Replication* (reactome, mean cos +0.59 to 40).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~36% of this change | +5.7 | +10.3 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~51% of this change | +5.6 | +11.4 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~63% of this change | +5.5 | +8.2 |
|  | [[Panobinostat (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~89% of this change | +2.7 | +5.6 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +2.4 | +3.0 |
|  | [[Topotecan (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.9 |
|  | [[Pyridoxine (hydrochloride) (drug)]] 0.05 µM |  | +1.4 | +0.5 |
|  | [[Belumosudil (drug)]] 5 µM |  | +1.2 | +1.8 |
|  | [[Demeclocycline (drug)]] 5 µM |  | +1.2 | +1.3 |
|  | [[PH-797804 (drug)]] 5 µM |  | +1.2 | +4.0 |
| fall | [[Selinexor (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~53% of this change | -4.0 | -5.0 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~52% of this change | -3.4 | -5.1 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift, explains ~37% of this change | -3.4 | -4.2 |
|  | [[Tucidinostat (drug)]] 5 µM |  | -2.8 | -5.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~40% of this change | -2.5 | -3.3 |
|  | [[Vinblastine (sulfate) (drug)]] 5 µM |  | -2.4 | -1.5 |
|  | [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | -1.6 | -3.2 |
|  | [[Neratinib (maleate) (drug)]] 5 µM |  | -1.6 | -1.2 |
|  | [[Peretinoin (drug)]] 5 µM |  | -1.6 | -1.8 |

## What is on record

|  |  |
|---|---|
| Name | non-SMC condensin II complex subunit H2 |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q13.33 — chr22:50,508,224-50,524,780 (+) |
| Ensembl biotype | protein_coding |
| Also known as | 384D8-2, hCAP-H2, CAP-H2 |
| Gene groups (HGNC) | Condensin II subunits |
| Hallmark sets | FATTY_ACID_METABOLISM |
| Reactome | 5 pathways, smallest: Condensation of Prophase Chromosomes; Mitotic Prophase; M Phase |
| Matched by | ensembl_id |

**Function**, from UniProt [Q6IBW4](https://www.uniprot.org/uniprotkb/Q6IBW4) (Condensin-2 complex subunit H2):

> Regulatory subunit of the condensin-2 complex, a complex that seems to provide chromosomes with an additional level of organization and rigidity and in establishing mitotic chromosome architecture. May promote the resolution of double-strand DNA catenanes (intertwines) between sister chromatids. Condensin-mediated compaction likely increases tension in catenated sister chromatids, providing directionality for type II topoisomerase-mediated strand exchanges toward chromatid decatenation. …

**Summary**, from NCBI Gene [29781](https://www.ncbi.nlm.nih.gov/gene/29781):

> This gene encodes one of the non-SMC subunits of the condensin II complex. This complex plays an essential role in mitotic chromosome assembly. Alternate splicing of this gene results in multiple transcript variants.[provided by RefSeq, May 2010]

**Accessions** — [HGNC:25071](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:25071) · Entrez [29781](https://www.ncbi.nlm.nih.gov/gene/29781) · UniProt [Q6IBW4](https://www.uniprot.org/uniprotkb/Q6IBW4) · Ensembl [ENSG00000025770](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000025770)

## Data

Gene col 364: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 364); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 364, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 364]; `tensor/DDL_lfc|DDL_z.npy` [364]; `embed/gene_vectors.npy` [364]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 364 or target_col == 364). Every well: [[NCAPH2 — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/NCAPH2.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
