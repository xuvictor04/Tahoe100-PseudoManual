---
symbol: "CRKL"
type: "gene"
col: 1832
ensembl_id: "ENSG00000099942"
name: "CRK like proto-oncogene, adaptor protein"
location: "22q11.21"
module: 20
arm: "+"
pooled_cpm: 57.22
n_lines_expressing: 50
n_dd_up: 9
n_dd_down: 0
n_dd_up_clean: 7
n_dd_down_clean: 0
in_vector_space: true
direction_upstream: 0
direction_downstream: 0
tags: ["gene", "module/020"]
generated_by: "tahoemap"
---

# CRKL

*CRK like proto-oncogene, adaptor protein* — 22q11.21

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 9 drug-doses (2 with an alert ⚠); the strongest is [[TAK-901 (drug)]] 5 µM: 10.4× (z +13.8, q 2e-40, up in 49 of 49 measured lines).
> No drug-dose lowers it significantly in the pooled (median-over-lines) data.
> In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.142×, NCI-H1573 0.191×, HepG2/C3A 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.152×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Bimiralisib (drug)]] 0.5 µM in 1 line (CHP-212 0.0819×); [[Furosemide (drug)]] 0.5 µM in 1 line (SW 1271 0.0945×).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 0 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[PGAM1]] (+0.78, fdr 7e-06), [[BPNT2]] (+0.69, fdr 7e-06), [[CIPC]] (+0.66, fdr 7e-06); moves opposite to [[CROCCP2-1]] (-0.59, fdr 7e-06), [[RBM25]] (-0.53, fdr 3e-05), [[MSX1]] (-0.52, fdr 9e-06).
> It sits in the **+** arm of [[Module 020]] (Cap-dependent Translation Initiation).

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 10 in all, 3 with an alert ⚠. 9 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 2 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 1832.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[TAK-901 (drug)]] 5 µM |  | **10.4×** | +13.8 | 2e-40 | 49/49 (SW480, NCI-H2030, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~0% here); composition shift; noisy plate (z scaled) |
| [[PH-797804 (drug)]] 5 µM |  | **4.35×** | +8.7 | 1e-15 | 40/48 (C32, LS 180, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Ouabain (Octahydrate) (drug)]] 5 µM |  | **2.06×** | +8.1 | 8e-14 | 47/48 (LS 180, KATO III, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here); composition shift |
| [[Digitoxin (drug)]] 0.5 µM |  | **1.87×** | +7.0 | 3e-10 | 44/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.5 µM |  | **1.54×** | +4.8 | 2e-04 | 39/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Adagrasib (drug)]] 0.05 µM | ⚠ position not correctable | 1.13× | +4.7 | 2e-04 | 1/49 (MIA PaCa-2) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **1.51×** | +4.7 | 3e-04 | 34/48 (NCI-H460, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[Ouabain (Octahydrate) (drug)]] 0.05 µM |  | **1.42×** | +4.0 | 0.005 | 26/48 (NCI-H460, PANC-1, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |
| [[c-Kit-IN-1 (drug)]] 0.05 µM | ⚠ unreliable plate only | **1.41×** | +3.9 | 0.007 | 31/48 (Hs 766T, Panc 03.27, …) | inconsistent across doses |  |
| [[Digitoxin (drug)]] 0.05 µM |  | **1.37×** | +3.6 | 0.021 | 26/47 (NCI-H460, SW480, …) | all doses, stronger at high dose | cell-cycle shift (explains ~0% here) |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 3 in all, 2 with an alert ⚠. 0 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), none with an alert. ⚠ as above. `tables/drug_effects.parquet` col == 1832.*

In single lines (per-line |z| ≥ 8.4, all drug-doses: 4 here, 2 with an alert ⚠; `tables/drug_line_top.parquet`), these lower it: [[Dinaciclib (drug)]] 0.5 µM in 3 lines (SK-MEL-2 0.142×, NCI-H1573 0.191×, HepG2/C3A 0.239×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change); [[Dinaciclib (drug)]] 5 µM in 1 line (NCI-H1792 0.152×; ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change); [[Bimiralisib (drug)]] 0.5 µM in 1 line (CHP-212 0.0819×); [[Furosemide (drug)]] 0.5 µM in 1 line (SW 1271 0.0945×).

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change | 0.725× | -3.6 | 0.12 | 26/49 (SK-MEL-2, NCI-H1573, …) | two highest doses | composition shift |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~13% of this change | 0.802× | -3.5 | 0.12 | 22/49 (NCI-H23, NCI-H460, …) | top dose only |  |
| [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | 0.748× | -3.3 | 0.19 | 26/48 (SW 900, HCT15, …) | inconsistent across doses | position effect removed |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: -0.13 per unit of S-phase module lfc, -0.01 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 1832. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[NCI-H460 (line)]] | wt | 54.2 | 5 (1 ⚠) | 0 | [[TAK-901 (drug)]] 5 µM 12.1× (z +11.7) | — |
| [[LS 180 (line)]] | wt | 52.1 | 3 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 4.47× (z +12.0) | — |
| [[SW480 (line)]] | alt | 53.2 | 3 | 0 | [[TAK-901 (drug)]] 5 µM 18.3× (z +14.0) | — |
| [[C32 (line)]] | wt | 49.9 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 33.0× (z +12.7) | — |
| [[HEC-1-A (line)]] | alt | 50.4 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 9.98× (z +10.0) | — |
| [[HOP62 (line)]] | alt | 47.3 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.8× (z +10.0) | — |
| [[KATO III (line)]] | alt | 50.7 | 2 | 0 | [[Ouabain (Octahydrate) (drug)]] 5 µM 3.88× (z +10.2) | — |
| [[LoVo (line)]] | wt | 51.0 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 14.6× (z +11.9) | — |
| [[NCI-H1573 (line)]] | alt | 84.2 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 21.0× (z +11.7) | [[Dinaciclib (drug)]] 0.5 µM 0.191× (z -12.3) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[NCI-H1792 (line)]] | alt | 59.9 | 1 | 1 (1 ⚠) | [[TAK-901 (drug)]] 5 µM 10.3× (z +9.0) | [[Dinaciclib (drug)]] 5 µM 0.152× (z -13.4) ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change |
| [[NCI-H2030 (line)]] | alt | 59.7 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 18.0× (z +12.3) | — |
| [[NCI-H2347 (line)]] | alt | 84.5 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 8.89× (z +10.0) | — |
| [[PANC-1 (line)]] | alt | 45.2 | 2 | 0 | [[TAK-901 (drug)]] 5 µM 10.3× (z +11.7) | — |
| [[SW48 (line)]] | wt | 61.0 | 2 | 0 | [[PH-797804 (drug)]] 5 µM 28.2× (z +10.2) | — |
| [[A-427 (line)]] | wt | 31.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 17.6× (z +11.3) | — |
| [[A549 (line)]] | wt | 44.8 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.3× (z +10.0) | — |
| [[AsPC-1 (line)]] | alt | 54.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.0× (z +9.6) | — |
| [[CFPAC-1 (line)]] | alt | 70.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.58× (z +8.5) | — |
| [[CHP-212 (line)]] | wt | 73.1 | 0 | 1 | — | [[Bimiralisib (drug)]] 0.5 µM 0.0819× (z -8.7) |
| [[COLO 205 (line)]] | alt | 47.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 25.6× (z +11.4) | — |
| [[HepG2_C3A (line)]] | wt | 61.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.239× (z -8.9) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[Hs 766T (line)]] | wt | 61.3 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.7× (z +9.1) | — |
| [[HS-578T (line)]] | alt | 62.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 12.8× (z +9.7) | — |
| [[HT-29 (line)]] | alt | 84.2 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 11.7× (z +10.3) | — |
| [[LOX-IMVI (line)]] | wt | 39.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 13.4× (z +9.7) | — |
| [[MIA PaCa-2 (line)]] | alt | 91.4 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.8× (z +9.5) | — |
| [[NCI-H23 (line)]] | alt | 62.5 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 10.9× (z +10.3) | — |
| [[Panc 03.27 (line)]] | alt | 85.9 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 14.0× (z +11.7) | — |
| [[RKO (line)]] | wt | 66.7 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 16.8× (z +10.1) | — |
| [[SK-MEL-2 (line)]] | alt | 32.1 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.142× (z -13.0) ⚠ toxic; transcription drop; cell-cycle shift, explains ~33% of this change |
| [[SW 1271 (line)]] | alt | 64.7 | 0 | 1 | — | [[Furosemide (drug)]] 0.5 µM 0.0945× (z -8.6) |
| [[SW 900 (line)]] | alt | 60.6 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 9.79× (z +8.6) | — |
| [[SW1417 (line)]] | alt | 76.0 | 1 | 0 | [[TAK-901 (drug)]] 5 µM 8.72× (z +9.3) | — |
| [[A-172 (line)]] | wt | 41.8 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 51.2 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 63.8 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 44.3 | 0 | 0 | — | — |
| [[C-33 A (line)]] | alt | 68.2 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 46.9 | 0 | 0 | — | — |
| [[HCT15 (line)]] | alt | 84.8 | 0 | 0 | — | — |
| [[hTERT-HPNE (line)]] | wt | 47.5 | 0 | 0 | — | — |
| [[J82 (line)]] | alt | 46.5 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 61.6 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 56.2 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 71.8 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 59.3 | 0 | 0 | — | — |
| [[SHP-77 (line)]] | alt | 50.9 | 0 | 0 | — | — |
| [[SNU-1 (line)]] | wt | 43.7 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 51.6 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 53.9 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 1832), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*90 of its nearest partners move with it, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[PGAM1]] | +0.78 | +0.80 / +0.77 | both halves | 7e-06 | **novel candidate** |
| [[BPNT2]] | +0.69 | +0.75 / +0.66 | both halves | 7e-06 |  |
| [[CIPC]] | +0.66 | +0.64 / +0.72 | both halves | 7e-06 |  |
| [[ANKRD30BL]] | +0.64 | +0.55 / +0.69 | both halves | 1e-05 |  |
| [[WRNIP1]] | +0.63 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[RPL18A]] | +0.63 | +0.59 / +0.60 | both halves | 7e-06 |  |
| [[EIF4H]] | +0.63 | +0.59 / +0.68 | both halves | 7e-06 |  |
| [[RPL10]] | +0.62 | +0.67 / +0.61 | both halves | 7e-06 |  |
| [[CCAR2]] | +0.62 | +0.64 / +0.59 | both halves | 7e-06 |  |
| [[SZRD1]] | +0.62 | +0.57 / +0.62 | both halves | 9e-06 |  |
| [[EOLA2]] | +0.61 | +0.65 / +0.58 | both halves | 7e-06 |  |
| [[RPSA]] | +0.61 | +0.53 / +0.63 | both halves | 1e-05 |  |

## Genes that move opposite

*10 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated).*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[CROCCP2-1]] | -0.59 | -0.62 / -0.61 | both halves | 7e-06 |  |
| [[RBM25]] | -0.53 | -0.52 / -0.44 | both halves | 3e-05 |  |
| [[MSX1]] | -0.52 | -0.58 / -0.57 | both halves | 9e-06 |  |
| [[EIF5B]] | -0.52 | -0.59 / -0.57 | both halves | 1e-05 |  |
| [[OFD1]] | -0.52 | -0.53 / -0.52 | both halves | 1e-05 |  |
| [[JMJD1C]] | -0.52 | -0.39 / -0.42 | both halves | 5e-05 |  |
| [[DHRSX]] | -0.51 | -0.52 / -0.39 | both halves | 6e-05 |  |
| [[NEMF]] | -0.51 | -0.46 / -0.48 | both halves | 2e-05 |  |
| [[TCF25]] | -0.50 | -0.49 / -0.43 | both halves | 3e-05 |  |
| [[THG1L]] | -0.50 | -0.62 / -0.42 | both halves | 4e-05 |  |

## Direction (probable)

No arrow points to or from this gene in this run (how the arrows are made: [[Probable direction]]).

## Where it sits

- **Module**: [[Module 020]] — Cap-dependent Translation Initiation; 191 genes; this gene is in the **+** arm (projection on the module's main direction 0.617). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.29).
- **Nodal map** (x, y) = (-25.2, -23.4); signed map (-21.9, -35.7). **Vector** length 89.9, 25.1% of its response variance represented; |z| ≥ 3 in 753 contexts (`embed/genes.parquet`).
- **Candidate new member** (not annotated, but close to the annotated members of its arm; `validation/novel_members.csv`): *Eukaryotic Translation Elongation* (reactome, mean cos +0.52 to 10); *Peptide chain elongation* (reactome, mean cos +0.53 to 9); *PELO:HBS1L and ABCE1 dissociate a ribosome on a non-stop mRNA* (reactome, mean cos +0.53 to 8).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[TAK-901 (drug)]] 5 µM |  | +5.7 | +13.8 |
|  | [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift | +5.2 | +1.6 |
|  | [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop; cell-cycle shift | +4.9 | -0.8 |
|  | [[Dinaciclib (drug)]] 5 µM | ⚠ toxic; transcription drop; cell-cycle shift, explains ~43% of this change | +3.9 | -2.5 |
|  | [[PH-797804 (drug)]] 5 µM |  | +3.7 | +8.7 |
|  | [[Ponatinib (drug)]] 5 µM |  | +2.5 | -0.1 |
|  | [[Trametinib (DMSO_TF solvate) (drug)]] 0.05 µM |  | +2.0 | +1.2 |
|  | [[Lopinavir (drug)]] 5 µM |  | +2.0 | +1.5 |
|  | [[Bosentan (hydrate) (drug)]] 5 µM |  | +1.9 | +1.7 |
| fall | [[Homoharringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.6 | +0.0 |
|  | [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift | -5.4 | -2.7 |
|  | [[Homoharringtonine (drug)]] 0.5 µM | ⚠ cell-cycle shift | -4.4 | -0.7 |
|  | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | -3.7 | +0.2 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | -3.6 | -0.0 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | -2.5 | +0.6 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | -2.4 | -0.5 |
|  | [[Temsirolimus (drug)]] 0.05 µM |  | -2.4 | -2.7 |
|  | [[Rapamycin (drug)]] 5 µM |  | -2.2 | -1.7 |
|  | [[Gallic acid (hydrate) (drug)]] 0.05 µM |  | -2.0 | -3.3 |

## What is on record

|  |  |
|---|---|
| Name | CRK like proto-oncogene, adaptor protein |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 22q11.21 — chr22:20,917,407-20,953,747 (+) |
| Ensembl biotype | protein_coding |
| Gene groups (HGNC) | SH2 domain containing; SH3 domain containing |
| Reactome | 18 pathways, smallest: MET receptor recycling; MET activates RAP1 and RAC1; Frs2-mediated activation |
| Matched by | ensembl_id |

**Function**, from UniProt [P46109](https://www.uniprot.org/uniprotkb/P46109) (Crk-like protein):

> May mediate the transduction of intracellular signals.

**Summary**, from NCBI Gene [1399](https://www.ncbi.nlm.nih.gov/gene/1399):

> This gene encodes a protein kinase containing SH2 and SH3 (src homology) domains which has been shown to activate the RAS and JUN kinase signaling pathways and transform fibroblasts in a RAS-dependent fashion. It is a substrate of the BCR-ABL tyrosine kinase, plays a role in fibroblast transformation by BCR-ABL, and may be oncogenic.[provided by RefSeq, Jan 2009]

**Accessions** — [HGNC:2363](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:2363) · Entrez [1399](https://www.ncbi.nlm.nih.gov/gene/1399) · UniProt [P46109](https://www.uniprot.org/uniprotkb/P46109) · Ensembl [ENSG00000099942](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000099942)

## Data

Gene col 1832: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 1832); `tables/drug_effects.parquet` (13 rows, flagged included); `relations/gene_relations.parquet` (col_a == 1832, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 1832]; `tensor/DDL_lfc|DDL_z.npy` [1832]; `embed/gene_vectors.npy` [1832]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 1832 or target_col == 1832). Every well: [[CRKL — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. No written note yet: write `tahoemap/vault_seed/genes/CRKL.md` and rerun `tahoe vault`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
