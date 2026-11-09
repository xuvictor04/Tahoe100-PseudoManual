---
symbol: "MEF2B"
type: "gene"
col: 13160
ensembl_id: "ENSG00000213999"
name: "myocyte enhancer factor 2B"
location: "19p13.11"
module: 36
arm: "+"
pooled_cpm: 14.46
n_lines_expressing: 50
n_dd_up: 14
n_dd_down: 11
n_dd_up_clean: 11
n_dd_down_clean: 3
in_vector_space: true
direction_upstream: 2
direction_downstream: 0
tags: ["gene", "module/036", "written"]
generated_by: "tahoemap"
---

# MEF2B

*myocyte enhancer factor 2B* — 19p13.11

> [!summary] In one line
> MEF2B is the divergent member of the MEF2 family — named for muscle because of the DNA-binding domain it shares with its paralogues, but best established as a germinal-centre B-cell factor that activates BCL6 and is recurrently mutated in lymphoma.

## What it is

MEF2B shares the N-terminal MADS-box and MEF2 domain with [[MEF2A]], MEF2C and MEF2D, and therefore binds the same A/T-rich consensus. Outside that domain it diverges from the other three, and it was flagged as the unusual member of the family when the mouse gene was first characterised. The family name is a statement about a shared binding site, not about where each member works.

The best-supported biology for MEF2B is in B cells, not muscle. It is expressed in germinal-centre B cells, where it directly activates *BCL6*, the factor on which the germinal-centre reaction and the lymphomas derived from it depend; losing MEF2B impairs proliferation of those B cells, and raising BCL6 compensates only partly, implying targets beyond BCL6. MEF2B is recurrently mutated in diffuse large B-cell and follicular lymphoma, at roughly one case in nine. The mutations fall into two classes: N-terminal changes raise its transcriptional activity and BCL6 with it, some by disrupting binding to the corepressor CABIN1, others by altering dimerisation; C-terminal changes truncate the protein and remove regulatory phosphorylation and SUMOylation sites, raising both activity and stability. Conditional mouse work places MEF2B as an instructor of germinal-centre development and an oncogene in B-cell lymphomagenesis, and expression surveys show a germinal-centre-associated pattern, though not one restricted to germinal-centre-derived tumours.

MEF2B is expressed in the early cardiac and skeletal muscle lineages of the mouse embryo and is a potent transactivator there, so its muscle credentials are more than family membership. But a MEF2B-specific *requirement* in striated muscle, demonstrated by loss of function, is not something I can point to.

## What is uncertain

Treating MEF2B as a muscle transcription factor is the weakest link here. The name and the shared DNA-binding domain justify grouping it with its paralogues; the functional literature does not place it in the myogenic programme as it does MEF2A and MEF2C.

Nothing I can cite puts MEF2B protein at the TRIM72 promoter: the promoter study identified a MEF2 site, without resolving which paralogue occupies it in muscle, let alone elsewhere.

Paralogue-specific activity inference is intrinsically hard here because all four members read the same consensus: an inferred "MEF2B activity" may report shared MEF2-site occupancy rather than MEF2B — a property of the method applied to this family, not a defect of this dataset.

Class IIa HDACs and the HUCA corepressor complex do restrain MEF2B — the commonest lymphoma mutant, D83V, works partly by escaping both — so that much is established. What is not is whether the gating is quantitatively like MEF2A's: the family is usually described with a single regulatory model, and MEF2B's divergent C-terminus is a reason not to transfer it wholesale.

## References

- Molkentin et al., 1996, Molecular and Cellular Biology — MEF2B is a potent transactivator expressed in the early myogenic lineages.
- Morisaki et al., 1997, Journal of Biochemistry — characterised mouse *Mef2b* as the unique member of the MEF2 gene family.
- Jung & Ko, 2010, Biochemical and Biophysical Research Communications — identified a conserved MEF2 site adjacent to an E-box in the TRIM72 promoter, activated by MyoD/myogenin and MEF2 together.
- Ying et al., 2013, Nature Immunology — MEF2B directly activates BCL6 in germinal-centre B cells, and MEF2B mutations in DLBCL and follicular lymphoma deregulate BCL6.
- Krenács et al., 2015, Virchows Archiv — surveyed MEF2B expression across lymphoid tissues and malignant lymphomas.
- Brescia et al., 2018, Cancer Cell — MEF2B instructs germinal-centre development and acts as an oncogene in B-cell lymphomagenesis.
- Yu et al., 2024, Nature Communications — MEF2B C-terminal mutations enhance transcriptional activity and protein stability to drive B-cell lymphomagenesis.

## At a glance

> [!summary] In this data
> Pooled over the cell lines (median), raised significantly by 14 drug-doses (3 with an alert ⚠); the strongest is [[Panobinostat (drug)]] 5 µM: 2.55× (z +12.9, q 3e-35, up in 44 of 48 measured lines).
> Pooled over the cell lines (median), lowered significantly by 11 drug-doses (8 with an alert ⚠); the strongest is [[Niclosamide (olamine) (drug)]] 5 µM: 0.448× (z -10.6, q 1e-23, down in 33 of 45 measured lines) ⚠ toxic. The strongest without an alert is [[TAK-901 (drug)]] 5 µM: 0.587× (z -3.8, q 0.012, down in 11 of 48 measured lines).
> Its strongest partners by |cos| (100 of its 100 nearest are replicated: the same sign with fdr ≤ 0.10 in two random halves of the compounds; 1 carry an alert, ⚠ + the reason: not replicated, same locus, or the partner in the vector space only through flagged drug-doses): it moves with [[FBXO36]] (+0.66, fdr 7e-06), [[NPLOC4]] (+0.66, fdr 9e-06), [[LIN52]] (+0.63, fdr 1e-05); moves opposite to [[AMOT]] (-0.61, fdr 5e-05), [[ISOC1]] (-0.60, fdr 4e-05), [[CREG1]] (-0.60, fdr 1e-05).
> It sits in the **+** arm of [[Module 036]].
> Probable direction (from the cell lines, not proof of direct regulation): 2 arrows point to it, the strongest [[ADAM22]] → it (grade B ⚠); none goes from it. See Direction (probable) below.

## Drugs that raise it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 14 in all, 3 with an alert ⚠. 14 of them raise it significantly (**bold**: q < 0.10, ≥ 1.2×), 3 with an alert ⚠. ⚠ = an artifact flag on the drug-dose or on this gene: the change may come from cell death, a drop in transcription, a shift in the cell-cycle mix, a plate that does not reproduce or a well-position problem rather than from regulation of this gene; it is shown, not left out. `tables/drug_effects.parquet` col == 13160.*

| Drug-dose | Alert | Fold | z | q | Lines up / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Panobinostat (drug)]] 5 µM |  | **2.55×** | +12.9 | 3e-35 | 44/48 (SW480, LoVo, …) | all doses, stronger at high dose | cell-cycle shift (explains ~15% here) |
| [[Panobinostat (drug)]] 0.5 µM |  | **2.46×** | +12.4 | 7e-33 | 45/47 (SW480, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~13% here) |
| [[Idarubicin (hydrochloride) (drug)]] 5 µM |  | **1.80×** | +11.5 | 3e-28 | 37/47 (PANC-1, SK-MEL-2, …) | rises with dose | cell-cycle shift (explains ~16% here) |
| [[Belinostat (drug)]] 5 µM |  | **2.17×** | +10.7 | 2e-24 | 44/47 (SW480, LoVo, …) | rises with dose | cell-cycle shift (explains ~13% here) |
| [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | **1.52×** | +5.6 | 3e-06 | 21/41 (MIA PaCa-2, NCI-H460, …) | rises with dose |  |
| [[Doxorubicin (hydrochloride) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~31% of this change | **1.49×** | +5.3 | 1e-05 | 23/46 (NCI-H2030, SNU-423, …) | rises with dose |  |
| [[Belinostat (drug)]] 0.5 µM |  | **1.45×** | +5.1 | 3e-05 | 22/45 (LS 180, NCI-H2030, …) | rises with dose | cell-cycle shift (explains ~7% here) |
| [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | **1.29×** | +5.0 | 4e-05 | 19/48 (CFPAC-1, NCI-H2030, …) | rises with dose |  |
| [[Panobinostat (drug)]] 0.05 µM |  | **1.41×** | +4.6 | 3e-04 | 17/48 (LoVo, LS 180, …) | all doses, stronger at high dose | cell-cycle shift (explains ~5% here) |
| [[Fedratinib (hydrochloride hydrate) (drug)]] 5 µM |  | **1.27×** | +3.3 | 0.055 | 14/47 (Panc 03.27, RKO, …) | top dose only |  |
| [[Ponatinib (drug)]] 0.5 µM |  | **1.27×** | +3.3 | 0.055 | 15/47 (LoVo, A-172, …) | two highest doses |  |
| [[Dihydroartemisinin (drug)]] 0.05 µM |  | **1.27×** | +3.2 | 0.067 | 8/47 (NCI-H1573, NCI-H460, …) | inconsistent across doses |  |
| [[Idarubicin (hydrochloride) (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~60% of this change | **1.25×** | +3.1 | 0.079 | 5/47 (LoVo, BT-474, …) | rises with dose |  |
| [[Clobetasol propionate (drug)]] 0.05 µM |  | **1.26×** | +3.1 | 0.079 | 8/47 (SW48, AsPC-1, …) | inconsistent across doses |  |

## Drugs that lower it

*Pooled over the cell lines (median). Every drug-dose with |z| ≥ 3 or q < 0.10, strongest first: 13 in all, 8 with an alert ⚠. 11 of them lower it significantly (**bold**: q < 0.10, ≥ 1.2×), 8 with an alert ⚠. ⚠ as above. `tables/drug_effects.parquet` col == 13160.*

| Drug-dose | Alert | Fold | z | q | Lines down / measured | Dose pattern | Caveats |
|---|---|---|---|---|---|---|---|
| [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | **0.448×** | -10.6 | 1e-23 | 33/45 (PANC-1, hTERT-HPNE, …) | rises with dose | cell-cycle shift (explains ~5% here); position effect removed |
| [[Ouabain (Octahydrate) (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~30% of this change | **0.663×** | -5.7 | 4e-06 | 23/48 (SW480, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Digitoxin (drug)]] 5 µM | ⚠ toxic; transcription drop | **0.696×** | -5.0 | 1e-04 | 22/46 (COLO 205, NCI-H460, …) | rises with dose | cell-cycle shift (explains ~22% here) |
| [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | **0.716×** | -4.6 | 6e-04 | 21/38 (A549, NCI-H1573, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[TAK-901 (drug)]] 5 µM |  | **0.587×** | -3.8 | 0.012 | 11/48 (A-427, SW 900, …) | top dose only | plate-row cell shift; cell-cycle shift (explains ~19% here); composition shift; noisy plate (z scaled) |
| [[Dinaciclib (drug)]] 0.05 µM | ⚠ toxic; transcription drop | **0.743×** | -3.8 | 0.012 | 15/33 (PANC-1, MIA PaCa-2, …) | inconsistent across doses | cell-cycle shift (explains ~0% here); composition shift |
| [[PH-797804 (drug)]] 5 µM |  | **0.591×** | -3.8 | 0.012 | 17/45 (NCI-H23, NCI-H2030, …) | top dose only | plate-row cell shift; composition shift; noisy plate (z scaled) |
| [[Digitoxin (drug)]] 0.5 µM | ⚠ cell-cycle shift, explains ~23% of this change | **0.764×** | -3.7 | 0.014 | 16/47 (BT-474, NCI-H460, …) | rises with dose |  |
| [[Harringtonine (drug)]] 5 µM | ⚠ cell-cycle shift, explains ~86% of this change | **0.768×** | -3.5 | 0.029 | 19/46 (Panc 03.27, PANC-1, …) | all doses, stronger at high dose | composition shift |
| [[Docetaxel (drug)]] 0.05 µM | ⚠ transcription drop; cell-cycle shift, explains ~75% of this change | **0.792×** | -3.2 | 0.071 | 18/44 (SW1417, SK-MEL-2, …) | inconsistent across doses | low cells (technical?) |
| [[Niclosamide (olamine) (drug)]] 0.5 µM |  | **0.799×** | -3.1 | 0.098 | 10/48 (MIA PaCa-2, A-172, …) | rises with dose | position effect removed |
| [[Tucidinostat (drug)]] 5 µM |  | 0.856× | -3.1 | 0.10 | 14/48 (HEC-1-A, H4, …) | rises with dose |  |
| [[Clopidogrel (drug)]] 0.05 µM |  | 0.794× | -3.0 | 0.10 | 4/48 (MIA PaCa-2, HS-578T, …) | inconsistent across doses |  |

*`cell-cycle shift`: the drug-dose moved its cells into or out of S or G2/M. Its alert says how much of this gene's change that shift would explain (`cc_share`), from the gene's own slopes on the S-phase and G2/M modules (`tables/genes.parquet`: +0.34 per unit of S-phase module lfc, -0.49 per unit of G2/M module lfc). Fitted slopes are attenuated by noise, so the rule multiplies them by 2: a row keeps the alert when the shift would then explain 50% of the change or more, or leave less than a 1.2× change unexplained (an alert's ~N% is the share at the fitted slopes). `cell-cycle shift (explains ~N% here)` = the shift explains only about N% of this change, and even with the slopes multiplied by 2 less than 50%, so for this gene it is no artifact and carries no alert.*

## In which cell lines

*`tables/line_effects.parquet` col == 13160. CPM = the line's own level (n.m. = not measured: the line does not express it, or below 0.25 × its pooled level, where its reads are mostly ambient RNA; no per-line values). Up / down = drug-doses moving it ≥ 1.5× at per-line |z| ≥ 8.4 (calibrated on this run, `tables/info.json`; about 0.0492 such calls per gene and line are expected by chance over the 1,026 clean drug-doses), all of them; in brackets how many of those carry an alert (⚠: an artifact flag on the drug-dose or on this gene). The strongest of them is shown, with its alert, and after it the strongest without an alert when that is another one. Most responsive lines first.*

| Line | TP53 | CPM | Up | Down | Strongest up | Strongest down |
|---|---|---|---|---|---|---|
| [[PANC-1 (line)]] | alt | 14.8 | 1 | 3 (3 ⚠) | [[Idarubicin (hydrochloride) (drug)]] 5 µM 2.07× (z +8.6) | [[Niclosamide (olamine) (drug)]] 5 µM 0.278× (z -10.3) ⚠ toxic |
| [[SW480 (line)]] | alt | 15.9 | 2 | 2 (2 ⚠) | [[Panobinostat (drug)]] 5 µM 3.51× (z +10.5) | [[Ouabain (Octahydrate) (drug)]] 5 µM 0.293× (z -10.4) ⚠ cell-cycle shift, explains ~30% of this change |
| [[LS 180 (line)]] | wt | 9.36 | 2 | 0 | [[Panobinostat (drug)]] 5 µM 5.46× (z +8.9) | — |
| [[SW1417 (line)]] | alt | 13.9 | 0 | 2 (2 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.198× (z -9.6) ⚠ toxic; transcription drop |
| [[A549 (line)]] | wt | 12.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.114× (z -12.0) ⚠ toxic; transcription drop |
| [[C-33 A (line)]] | alt | 23.4 | 0 | 1 | — | [[Harringtonine (drug)]] 0.05 µM 0.179× (z -8.5) |
| [[C32 (line)]] | wt | 12.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.175× (z -8.8) ⚠ toxic; transcription drop |
| [[COLO 205 (line)]] | alt | 21.5 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.0726× (z -14.5) ⚠ toxic; transcription drop |
| [[HCT15 (line)]] | alt | 15.6 | 0 | 1 | — | [[Thymol (drug)]] 0.5 µM 0.130× (z -9.5) |
| [[HEC-1-A (line)]] | alt | 18.7 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.219× (z -10.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[Hs 766T (line)]] | wt | 9.35 | 0 | 1 | — | [[Gallic acid (hydrate) (drug)]] 0.5 µM 0.0647× (z -13.1) |
| [[hTERT-HPNE (line)]] | wt | 12.6 | 0 | 1 (1 ⚠) | — | [[Niclosamide (olamine) (drug)]] 5 µM 0.0956× (z -9.7) ⚠ toxic |
| [[J82 (line)]] | alt | 15.0 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.106× (z -13.8) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[KATO III (line)]] | alt | 9.74 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.172× (z -8.8) ⚠ toxic; transcription drop |
| [[LoVo (line)]] | wt | 13.7 | 1 | 0 | [[Panobinostat (drug)]] 5 µM 3.57× (z +8.9) | — |
| [[LOX-IMVI (line)]] | wt | 15.4 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.179× (z -9.6) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[NCI-H1573 (line)]] | alt | 16.3 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.172× (z -11.6) ⚠ toxic; transcription drop |
| [[NCI-H460 (line)]] | wt | 12.9 | 0 | 1 (1 ⚠) | — | [[Digitoxin (drug)]] 5 µM 0.256× (z -9.7) ⚠ toxic; transcription drop |
| [[Panc 03.27 (line)]] | alt | 30.5 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 5 µM 0.254× (z -9.7) ⚠ toxic; transcription drop; cell-cycle shift, explains ~0% of this change |
| [[SHP-77 (line)]] | alt | 16.9 | 0 | 1 (1 ⚠) | — | [[Dinaciclib (drug)]] 0.5 µM 0.218× (z -8.7) ⚠ toxic; transcription drop |
| [[SNU-1 (line)]] | wt | 16.0 | 0 | 1 (1 ⚠) | — | [[Selinexor (drug)]] 5 µM 0.224× (z -8.6) ⚠ cell-cycle shift, explains ~0% of this change |
| [[A-172 (line)]] | wt | 21.9 | 0 | 0 | — | — |
| [[A-427 (line)]] | wt | 22.5 | 0 | 0 | — | — |
| [[A498 (line)]] | wt | 13.1 | 0 | 0 | — | — |
| [[AN3 CA (line)]] | alt | 13.3 | 0 | 0 | — | — |
| [[AsPC-1 (line)]] | alt | 7.40 | 0 | 0 | — | — |
| [[BT-474 (line)]] | alt | 10.8 | 0 | 0 | — | — |
| [[CFPAC-1 (line)]] | alt | 12.7 | 0 | 0 | — | — |
| [[CHP-212 (line)]] | wt | 15.0 | 0 | 0 | — | — |
| [[H4 (line)]] | wt | 17.7 | 0 | 0 | — | — |
| [[HepG2_C3A (line)]] | wt | 10.6 | 0 | 0 | — | — |
| [[HOP62 (line)]] | alt | 11.2 | 0 | 0 | — | — |
| [[HS-578T (line)]] | alt | 16.2 | 0 | 0 | — | — |
| [[HT-29 (line)]] | alt | 12.3 | 0 | 0 | — | — |
| [[MIA PaCa-2 (line)]] | alt | 18.6 | 0 | 0 | — | — |
| [[NCI-H1792 (line)]] | alt | 12.9 | 0 | 0 | — | — |
| [[NCI-H2030 (line)]] | alt | 10.0 | 0 | 0 | — | — |
| [[NCI-H2122 (line)]] | alt | 13.6 | 0 | 0 | — | — |
| [[NCI-H23 (line)]] | alt | 21.5 | 0 | 0 | — | — |
| [[NCI-H2347 (line)]] | alt | 8.65 | 0 | 0 | — | — |
| [[NCI-H596 (line)]] | alt | 14.1 | 0 | 0 | — | — |
| [[NCI-H661 (line)]] | alt | 13.0 | 0 | 0 | — | — |
| [[RKO (line)]] | wt | 10.7 | 0 | 0 | — | — |
| [[RPMI-7951 (line)]] | alt | 15.5 | 0 | 0 | — | — |
| [[SK-MEL-2 (line)]] | alt | 14.2 | 0 | 0 | — | — |
| [[SNU-423 (line)]] | alt | 16.9 | 0 | 0 | — | — |
| [[SW 1088 (line)]] | alt | 11.7 | 0 | 0 | — | — |
| [[SW 1271 (line)]] | alt | 24.9 | 0 | 0 | — | — |
| [[SW 900 (line)]] | alt | 9.89 | 0 | 0 | — | — |
| [[SW48 (line)]] | wt | 10.6 | 0 | 0 | — | — |

## Genes that move with it

*Strongest of its 100 nearest partners by |cos| (`relations/gene_relations.parquet` col_a == 13160), and any of the 12 strongest without an alert below them; halves = cos in the spaces fitted on two random halves of the compounds (a hash split of the compound names). Evidence: `both halves` = replicated: the same sign in both, |cos| ≥ 0.2 in each and fdr ≤ 0.10; ⚠ `one half` = strong in one of the two random halves only — not replicated, no error estimate; ⚠ `not reproduced` = neither. Other alerts: ⚠ same locus / read-through risk (neighbours on the genome can correlate for that reason alone), and `GENE ⚠` = the partner is in the vector space only through flagged drug-doses (all its evidence carries an artifact flag for it). A partner with an alert is shown in its place, not left out. A correlation across drugs and lines, not evidence that one gene regulates the other.*

*83 of its nearest partners move with it, 1 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[FBXO36]] | +0.66 | +0.66 / +0.59 | both halves | 7e-06 |  |
| [[NPLOC4]] | +0.66 | +0.57 / +0.59 | both halves | 9e-06 |  |
| [[LIN52]] | +0.63 | +0.52 / +0.64 | both halves | 1e-05 |  |
| [[C19orf25]] | +0.62 | +0.54 / +0.64 | both halves | 1e-05 |  |
| [[ENDOV]] | +0.61 | +0.54 / +0.66 | both halves | 1e-05 |  |
| [[HIRA]] | +0.61 | +0.32 / +0.67 | both halves | 2e-04 |  |
| [[ZNF500]] | +0.61 | +0.48 / +0.67 | both halves | 2e-05 |  |
| [[TMEM11-DT]] | +0.60 | +0.59 / +0.64 | both halves | 7e-06 |  |
| [[FBXL18]] | +0.60 | +0.61 / +0.63 | both halves | 7e-06 |  |
| [[TRAPPC10]] | +0.60 | +0.36 / +0.56 | both halves | 9e-05 |  |
| [[C1orf159]] | +0.59 | +0.61 / +0.53 | both halves | 1e-05 |  |
| [[VPS9D1]] | +0.59 | +0.44 / +0.61 | both halves | 3e-05 |  |

## Genes that move opposite

*17 of its nearest partners move opposite, 0 of them with an alert (⚠; 0 not replicated); shown: the 12 strongest.*

| Gene | cos | Halves | Evidence | fdr | Notes |
|---|---|---|---|---|---|
| [[AMOT]] | -0.61 | -0.40 / -0.58 | both halves | 5e-05 |  |
| [[ISOC1]] | -0.60 | -0.42 / -0.55 | both halves | 4e-05 |  |
| [[CREG1]] | -0.60 | -0.49 / -0.59 | both halves | 1e-05 |  |
| [[CD83]] | -0.58 | -0.41 / -0.56 | both halves | 4e-05 |  |
| [[SLC25A30]] | -0.57 | -0.43 / -0.55 | both halves | 3e-05 |  |
| [[CYB5A]] | -0.55 | -0.50 / -0.53 | both halves | 1e-05 |  |
| [[DMXL2]] | -0.55 | -0.44 / -0.46 | both halves | 3e-05 |  |
| [[ENPP4]] | -0.53 | -0.39 / -0.56 | both halves | 6e-05 |  |
| [[TBL1XR1]] | -0.53 | -0.46 / -0.61 | both halves | 3e-05 |  |
| [[PEG10]] | -0.53 | -0.28 / -0.55 | both halves | 3e-04 |  |
| [[ABCG2]] | -0.53 | -0.32 / -0.53 | both halves | 2e-04 |  |
| [[ABLIM1]] | -0.52 | -0.37 / -0.60 | both halves | 8e-05 |  |

## Direction (probable)

*Arrows SOURCE → TARGET of the direction stage (`direction/edges.parquet`), each from a test (q < 0.10 in its family of tests: over the whole table, or for a lead - grade C - within its own group) of a recorded mutation, a natural knockout (lines that do not express a gene), compounds that target a gene, or a gene's natural level. A probable direction, from the screen's cell lines: not proof of direct regulation. Grades: A strong, B read its alerts, C a glimpse; ⚠ = a reason for doubt, shown in place. How to read them, and this run's controls: [[Probable direction]].*

### Upstream of this gene

*2 arrows, 2 of them with an alert ⚠; grade A 0, B 2, C 0.*

| Source | Grade | Direction (probable) | Evidence | Effect | q | Alerts |
|---|---|---|---|---|---|---|
| [[ADAM22]] | B | ADAM22 activity raises MEF2B's level | lines that do not express ADAM22 (12) vs lines expressing it (38) | 1.31× lower at baseline in the lines without ADAM22 | 0.019 | ⚠ within organs, on part of the lines; also absent: ASGR1; maybe low, not absent |
| [[TOP2A]] | B | TOP2A activity lowers MEF2B's level | compounds that target TOP2A: 3 of 5 raise it (Doxorubicin, Idarubicin, Mitoxantrone) | 60% of the class's compounds vs 2.8% of all compounds | 0.071 | ⚠ off-target possible; 3 compounds; artifact flags |

### Downstream of this gene

None: no arrow goes from this gene (to a gene, or to the cells under a drug-dose).

## Where it sits

- **Module**: [[Module 036]]; 135 genes; this gene is in the **+** arm (projection on the module's main direction 0.564). Its + and − arms move opposite to each other under the same drugs (mean cos between them -0.23).
- **Nodal map** (x, y) = (-15.3, -1.9); signed map (-19.7, 0.4). **Vector** length 65.1, 10.9% of its response variance represented; |z| ≥ 3 in 982 contexts (`embed/genes.parquet`).

**Predicted by the vector space**: the drug-doses whose vectors predict the largest rise and fall (gene vector · drug-dose vector, in z units), next to the observed z (`atlas/effects/DD_z.npy`): the 5 strongest predictions over all drug-doses and the 5 strongest of those without an artifact flag, together. ⚠ = an artifact flag on the drug-dose (or on this gene, where `tables/drug_effects.parquet` has the pair): its observed z may come from what the drug-dose did to the cells.

|  | Drug-dose | Alert | Predicted z | Observed z |
|---|---|---|---|---|
| rise | [[Ixazomib citrate (drug)]] 5 µM | ⚠ cell-cycle shift | +3.5 | +2.5 |
|  | [[Bortezomib (drug)]] 0.05 µM | ⚠ cell-cycle shift | +3.4 | +2.9 |
|  | [[Ixazomib citrate (drug)]] 0.5 µM |  | +3.2 | +1.1 |
|  | [[Ouabain (Octahydrate) (drug)]] 0.5 µM | ⚠ cell-cycle shift | +1.5 | -2.7 |
|  | [[Topotecan (hydrochloride) (drug)]] 5 µM | ⚠ toxic; cell-cycle shift, explains ~42% of this change | +1.5 | +5.6 |
|  | [[Mitoxantrone (dihydrochloride) (drug)]] 5 µM |  | +1.4 | +5.0 |
|  | [[Bortezomib (drug)]] 0.5 µM |  | +1.4 | +0.3 |
|  | [[Cabozantinib (S-malate) (drug)]] 0.05 µM |  | +1.3 | +1.7 |
|  | [[5-Azacytidine (drug)]] 5 µM |  | +1.3 | +0.6 |
| fall | [[Tucidinostat (drug)]] 5 µM |  | -7.5 | -3.1 |
|  | [[Tucidinostat (drug)]] 0.5 µM | ⚠ cell-cycle shift | -6.2 | -2.4 |
|  | [[Selinexor (drug)]] 5 µM | ⚠ cell-cycle shift | -4.2 | -0.3 |
|  | [[Niclosamide (olamine) (drug)]] 5 µM | ⚠ toxic | -3.8 | -10.6 |
|  | [[Dinaciclib (drug)]] 0.5 µM | ⚠ toxic; transcription drop | -3.4 | -4.6 |
|  | [[Tucidinostat (drug)]] 0.05 µM |  | -2.2 | -1.9 |
|  | [[Auranofin (drug)]] 5 µM |  | -1.6 | -2.0 |
|  | [[Terfenadine (drug)]] 0.5 µM |  | -1.6 | -1.5 |
|  | [[Diammonium Glycyrrhizinate (drug)]] 0.5 µM |  | -1.5 | -1.3 |

## What is on record

|  |  |
|---|---|
| Name | myocyte enhancer factor 2B |
| Locus type | gene with protein product (protein-coding gene) |
| Location | 19p13.11 — chr19:19,145,567-19,192,131 (-) |
| Ensembl biotype | protein_coding |
| Also known as | RSRFR2 |
| Gene groups (HGNC) | Myocyte enhancer factor 2 proteins; MADS box family |
| Reactome | 5 pathways, smallest: Myogenesis; Somatic hypermutation of immunoglobulin genes; Affinity selection of immunoglobulins |
| Matched by | ensembl_id |

**Function**, from UniProt [Q02080](https://www.uniprot.org/uniprotkb/Q02080) (Myocyte-specific enhancer factor 2B):

> Transcriptional activator which binds specifically to the MEF2 element, 5'-YTA[AT](4)TAR-3', found in numerous muscle-specific genes. Activates transcription via this element. May be involved in muscle-specific and/or growth factor-related transcription.

**Summary**, from NCBI Gene [100271849](https://www.ncbi.nlm.nih.gov/gene/100271849):

> The product of this gene is a member of the MADS/MEF2 family of DNA binding proteins. The protein is thought to regulate gene expression, including expression of the smooth muscle myosin heavy chain gene. This region undergoes considerable alternative splicing, with transcripts supporting two non-overlapping loci (GeneID 729991 and 100271849) as well as numerous read-through transcripts that span both loci (annotated as GeneID 4207). Several isoforms of this protein are expressed from either …

**Accessions** — [HGNC:6995](https://www.genenames.org/data/gene-symbol-report/#!/hgnc_id/HGNC:6995) · Entrez [100271849](https://www.ncbi.nlm.nih.gov/gene/100271849) · UniProt [Q02080](https://www.uniprot.org/uniprotkb/Q02080) · Ensembl [ENSG00000213999](https://www.ensembl.org/Homo_sapiens/Gene/Summary?g=ENSG00000213999)

## Data

Gene col 13160: `tables/genes.parquet`, `tables/line_effects.parquet` (50 rows) and `tables/drug_line_top.parquet` (col == 13160); `tables/drug_effects.parquet` (27 rows, flagged included); `relations/gene_relations.parquet` (col_a == 13160, 100 rows); `atlas/effects/DD_lfc|DD_z|DD_qup|DD_qdn.npy` [:, 13160]; `tensor/DDL_lfc|DDL_z.npy` [13160]; `embed/gene_vectors.npy` [13160]; `graph/nodes.parquet`; `direction/edges.parquet` (source_col == 13160 or target_col == 13160). Every well: [[MEF2B — plates]].

## Sources

Generated by `tahoemap vault` (v4) from the tables of the run; do not edit this note, it is rebuilt on every run. The written part above is `tahoemap/vault_seed/genes/MEF2B.md`.
Registry text: `reference/annotations.parquet` (HGNC, Ensembl GRCh38, UniProt, NCBI Gene; download dates in `reference/sources.json`). Paths are relative to the run folder.
